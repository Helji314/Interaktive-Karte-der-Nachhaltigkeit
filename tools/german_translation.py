# tools/generate_country_translations.py
import json
import pycountry
from babel import Locale
from pathlib import Path

locale = Locale('de')
out = {}
for c in pycountry.countries:
    try:
        alpha3 = c.alpha_3
        alpha2 = c.alpha_2
    except AttributeError:
        continue
    name_de = locale.territories.get(alpha2)
    if name_de:
        out[alpha3] = name_de

Path("public/data").mkdir(parents=True, exist_ok=True)
with open("public/data/countries_de.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"Saved {len(out)} translations to public/data/countries_de.json")