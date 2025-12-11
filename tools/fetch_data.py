
import pandas as pd
import json
from pathlib import Path

def export_detailed_calculations():
    """Export detailed calculation data for each country."""
    input_file = Path("data/processed/sustainability_index.csv")
    output_dir = Path("public/data")
    
    df = pd.read_csv(input_file)
    
    # Filter to only relevant columns (Entity + all normalized & score columns)
    calc_columns = ["Entity", "Code", "Year"]
    calc_columns += [col for col in df.columns if "_normalized" in col or "_score" in col]
    
    if "sustainability_index" in df.columns:
        calc_columns.append("sustainability_index")
    
    calc_df = df[[col for col in calc_columns if col in df.columns]].copy()
    
    # Convert to list of dicts for JSON
    json_data = calc_df.to_dict(orient="records")
    
    json_file = output_dir / "calculations.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved detailed calculations to {json_file}")

# In main(), vor dem letzten print():
export_detailed_calculations()