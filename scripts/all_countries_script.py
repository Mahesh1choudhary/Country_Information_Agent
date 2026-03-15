import asyncio
import httpx
from typing import Dict, List

async def get_country_name_map() -> Dict[str, List[str]]:
    # Fetching names and translations for maximum coverage
    url = "https://restcountries.com/v3.1/all?fields=name,translations"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return {}

        raw_data = response.json()
        result_map = {}

        for country in raw_data:
            name_data = country.get("name", {})
            official_name = name_data.get("official")
            if not official_name:
                continue

            official_name_key = official_name.lower()

            aliases = set()

            if "common" in name_data:
                aliases.add(name_data["common"].lower())

            aliases.discard(official_name_key)

            result_map[official_name_key] = sorted([a for a in aliases if a])

        return result_map

if __name__ == "__main__":
    countries = asyncio.run(get_country_name_map())
    import json
    print(json.dumps(countries, indent=2))