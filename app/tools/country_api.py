import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from app.commons.service_logger import setup_logger
from app.config.config_constants import CountryAPIConfigs


logger = setup_logger()

@retry(
    stop = stop_after_attempt(3),
    wait = wait_exponential(multiplier=1, min=2, max=10),
    retry = retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
    reraise = True
)
async def get_country_data(country:str):
    url = f"{CountryAPIConfigs.CountryAPIBaseUrl}{country}"
    logger.info(f"API Call: Requesting data for '{country}'")
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)

        response.raise_for_status()

        logger.info(f"API Success: Received data for '{country}'")
        return response.json()[0]


