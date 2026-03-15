from app.agent.state import AgentState
from app.tools.country_api import get_country_data


async def fetch_related_data(state:AgentState) -> AgentState:
    try:
        data = await get_country_data(state["country"])
        state['api_data'] = data
    except Exception as exc:
        state["error"] = str(exc)

    return state
