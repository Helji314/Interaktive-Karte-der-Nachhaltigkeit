"""
Export dimension scores from sustainability_index.csv into separate files.
Creates 4 files (one per dimension + overall index) with columns: DW_NAME, VALUE
Suitable for web visualization and Datawrapper integration.
"""

import pandas as pd
import json
from pathlib import Path

def main():
    # Load processed data
    input_file = Path("data/processed/sustainability_index.csv")
    output_dir = Path("public/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not input_file.exists():
        print(f"Error: {input_file} not found")
        return
    
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} countries from {input_file}")
    
    # Define dimensions to export
    dimensions = {
        "social_score": "social_sustainability",
        "environmental_score": "environmental_sustainability",
        "economic_score": "economic_sustainability",
        "sustainability_index": "overall_sustainability"
    }
    
    for score_column, output_name in dimensions.items():
        if score_column not in df.columns:
            print(f"Warning: Column '{score_column}' not found, skipping...")
            continue
        
        # Create export dataframe with DW_NAME and VALUE
        export_df = pd.DataFrame({
            "DW_NAME": df["Entity"],
            "VALUE": df[score_column]
        })
        
        # Remove rows with missing values
        export_df = export_df.dropna(subset=["VALUE"])
        export_df = export_df.sort_values("VALUE", ascending=False).reset_index(drop=True)
        
        # Save as CSV
        csv_file = output_dir / f"{output_name}.csv"
        export_df.to_csv(csv_file, index=False)
        print(f"✓ Saved {len(export_df)} countries to {csv_file}")
        
        # Save as JSON (for web integration)
        json_file = output_dir / f"{output_name}.json"
        json_data = export_df.to_dict(orient="records")
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(export_df)} countries to {json_file}")
    
    print(f"\n✓ All exports complete in {output_dir}")

if __name__ == "__main__":
    main()