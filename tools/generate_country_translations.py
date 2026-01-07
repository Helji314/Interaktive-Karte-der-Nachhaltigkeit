"""
Generate German country name translations from ISO-3166-1 codes.
Uses pycountry and Babel CLDR data.
Output: public/data/countries_de.json
"""

import json
import pycountry
from babel import Locale
from pathlib import Path

def main():
    locale = Locale('de')
    translations = {}
    
    for country in pycountry.countries:
        try:
            alpha3 = country.alpha_3
            alpha2 = country.alpha_2
        except AttributeError:
            continue
        
        # Try to get German name from Babel CLDR
        name_de = locale.territories.get(alpha2)
        
        if name_de:
            translations[alpha3] = name_de
    
    # Ensure output directory exists
    output_dir = Path("public/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    output_file = output_dir / "countries_de.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Saved {len(translations)} country translations to {output_file}")

if __name__ == "__main__":
    main()
