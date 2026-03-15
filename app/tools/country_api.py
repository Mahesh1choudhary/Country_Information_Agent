import httpx

from app.config.config_constants import CountryAPIConfigs


async def get_country_data(country:str):
    url = f"{CountryAPIConfigs.CountryAPIBaseUrl}{country}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()[0]
        else:
            return ValueError("Country not found")

