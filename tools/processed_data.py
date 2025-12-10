"""Process sustainability index data from multiple CSV files.
- Selects the latest year for each country
- Normalizes values to 1-100 scale based on min/max
- Inverse scaling for "negative" metrics (lower is worse)
- Combines all countries into one output table
"""
import pandas as pd
import glob
import os
from pathlib import Path

# Configuration: which files should be inverse-scaled (higher value = lower score)
INVERSE_SCALING = {
    "co-emissions-per-capita.csv": True,
    "long-run-air-pollution.csv": True,
    "unemployement-rate.csv": True,
    "gdp-per-capita-worldbank.csv": False,
    "live-expectancy.csv": False,
    "total-healthcare-expenditure-gdp.csv": False,
}

def load_and_process_csv(filepath):
    """Load CSV, select latest year per country, return dataframe."""
    df = pd.read_csv(filepath)
    filename = os.path.basename(filepath)
    # Find the value column (all except Entity, Code, Year)
    value_columns = [col for col in df.columns if col not in ['Entity', 'Code', 'Year']]
    if not value_columns:
        print(f"Warning: No value column found in {filename}")
        return None
    value_col = value_columns[0]
    # Remove rows with missing values for that metric
    df = df.dropna(subset=[value_col])
    # Ensure Year is numeric and sort to pick latest per Entity
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year'])
    df = df.sort_values(['Entity', 'Year'], ascending=[True, False])
    # Keep only latest year per country (first row per Entity after sorting)
    df_latest = df.groupby('Entity', as_index=False).first()
    metric_name = filename.replace('.csv', '')
    df_latest = df_latest.rename(columns={value_col: metric_name})
    # Keep only Entity, Code, Year and the metric
    cols_to_keep = ['Entity', 'Code', 'Year', metric_name]
    cols_present = [c for c in cols_to_keep if c in df_latest.columns]
    df_latest = df_latest[cols_present]
    is_inverse = filename in INVERSE_SCALING and INVERSE_SCALING[filename]
    return df_latest, metric_name, is_inverse

def normalize_to_100(series, inverse=False):
    """Normalize series to 1-100 scale (1 = worst, 100 = best by default)."""
    min_val = series.min()
    max_val = series.max()
    if pd.isna(min_val) or pd.isna(max_val):
        return pd.Series([pd.NA] * len(series), index=series.index)
    if min_val == max_val:
        # all identical -> neutral middle value
        return pd.Series([50.0] * len(series), index=series.index)
    normalized = 1.0 + (series - min_val) / (max_val - min_val) * 99.0
    if inverse:
        normalized = 101.0 - normalized
    return normalized

def main():
    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")
    processed_dir.mkdir(exist_ok=True)
    csv_files = sorted(glob.glob(str(raw_dir / "*.csv")))
    if not csv_files:
        print(f"No CSV files found in {raw_dir}")
        return
    print(f"Found {len(csv_files)} CSV files")
    dfs = []
    metric_columns = {}
    for filepath in csv_files:
        print(f"Processing {os.path.basename(filepath)}...")
        result = load_and_process_csv(filepath)
        if result is None:
            continue
        df, metric_name, is_inverse = result
        metric_columns[metric_name] = is_inverse
        dfs.append(df)
    # Start merge with first DF (which keeps Code and Year). For subsequent merges drop Code & Year to avoid duplicate columns.
    merged = dfs[0].copy()
    for df in dfs[1:]:
        df_to_merge = df.copy()
        # drop Code and Year from right-side before merging to prevent duplicate column creation
        for c in ('Code', 'Year'):
            if c in df_to_merge.columns:
                df_to_merge = df_to_merge.drop(columns=[c])
        merged = merged.merge(df_to_merge, on='Entity', how='outer')
    # Ensure we have an Entity column
    if 'Entity' not in merged.columns:
        print("No Entity column after merge — aborting.")
        return
    # If Code is missing in merged, try to fill from any available per-df Code columns (rare)
    if 'Code' not in merged.columns:
        # try to find any Code in original dfs
        for df in dfs:
            if 'Code' in df.columns:
                merged = merged.merge(df[['Entity', 'Code']].drop_duplicates(), on='Entity', how='left')
                break
    # Normalize each metric to 1-100
    print("\\nNormalizing values...")
    normalized_metrics = {}
    for metric, is_inverse in metric_columns.items():
        if metric in merged.columns:
            normalized = normalize_to_100(merged[metric].astype(float), inverse=is_inverse)
            merged[f"{metric}_normalized"] = normalized
            print(f"  {metric}: {'inverse' if is_inverse else 'normal'} scaling")
    # Calculate dimension scores - use the expected metric base names
    print("\\nCalculating dimension scores...")
    # Social: life expectancy + healthcare expenditure
    social_candidates = []
    if "live-expectancy" in metric_columns:
        social_candidates.append("live-expectancy_normalized")
    if "total-healthcare-expenditure-gdp" in metric_columns:
        social_candidates.append("total-healthcare-expenditure-gdp_normalized")
    social_cols = [c for c in social_candidates if c in merged.columns]
    if social_cols:
        merged["social_score"] = merged[social_cols].mean(axis=1, skipna=True)
        print("  Social score calculated from:", social_cols)
    # Environmental: co-emissions + air-pollution
    env_candidates = []
    if "co-emissions-per-capita" in metric_columns:
        env_candidates.append("co-emissions-per-capita_normalized")
    if "long-run-air-pollution" in metric_columns:
        env_candidates.append("long-run-air-pollution_normalized")
    env_cols = [c for c in env_candidates if c in merged.columns]
    if env_cols:
        merged["environmental_score"] = merged[env_cols].mean(axis=1, skipna=True)
        print("  Environmental score calculated from:", env_cols)
    # Economic: gdp + unemployment
    econ_candidates = []
    if "gdp-per-capita-worldbank" in metric_columns:
        econ_candidates.append("gdp-per-capita-worldbank_normalized")
    if "unemployement-rate" in metric_columns:
        econ_candidates.append("unemployement-rate_normalized")
    econ_cols = [c for c in econ_candidates if c in merged.columns]
    if econ_cols:
        merged["economic_score"] = merged[econ_cols].mean(axis=1, skipna=True)
        print("  Economic score calculated from:", econ_cols)
    # Overall sustainability index (average of the three dimension scores that exist)
    score_cols = [c for c in ("social_score", "environmental_score", "economic_score") if c in merged.columns]
    if score_cols:
        merged["sustainability_index"] = merged[score_cols].mean(axis=1, skipna=True)
        print("  Overall sustainability index calculated from:", score_cols)
    # Sort and save
    merged = merged.sort_values("Entity").reset_index(drop=True)
    output_file = processed_dir / "sustainability_index.csv"
    merged.to_csv(output_file, index=False)
    print(f"\\n✓ Saved to {output_file}")
    print(f"  Total countries: {len(merged)}")
    print(f"  Columns: {list(merged.columns)}")

if __name__ == "__main__":
    main()