from app.agent.state import AgentState, CountryAPIData
from app.commons.service_logger import setup_logger
from app.tools.country_api import get_country_data
from app.tools.related_fields import find_matching_fields, find_matching_countries

logger = setup_logger()
def identify_intent(state: AgentState) -> AgentState:
    query = state["query"].lower()
    query_items = query.split(" ")

    detected_fields = set()
    detected_countries = set()
    for item in query_items:
        matched_fields = find_matching_fields(item)
        detected_fields.update(matched_fields)

        matched_countries = find_matching_countries(item)
        detected_countries.update(matched_countries)

    state['fields'] = list(detected_fields)
    state['countries'] = list(detected_countries)

    logger.info(f"Intent Node: Detected {len(detected_countries)} countries and {len(detected_fields)} fields in query: {state['query']}")
    return state



async def fetch_related_data(state:AgentState) -> AgentState:
    countries = state.get("countries", [])
    api_data = []
    logger.info(f"Retrieval Node: Fetching data for {countries}")
    for country in countries:
        country_data: CountryAPIData = CountryAPIData()
        try:
            data = await get_country_data(country)
            country_data.data = data
            country_data.is_error = False
        except Exception as exc:
            country_data.is_error = True
            country_data.data = str(exc)
        api_data.append(country_data)

    state["api_data"] = api_data
    return state



def synthesize_answer(state: AgentState) -> AgentState:
    api_data = state.get("api_data",[])
    required_fields = state.get("fields", [])
    for country_data in api_data:
        if country_data.is_error:
            continue
        else:
            cleaned_data = {}
            for field, field_data in country_data.data.items():
                if field in required_fields:
                    cleaned_data[field] = field_data

            country_data.data = cleaned_data
    logger.info(f"Synthesis Node: synthesized answer for {state['query']}")
    return state