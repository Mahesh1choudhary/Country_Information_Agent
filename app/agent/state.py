from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    query: str
    countries: Optional[List[str]]
    fields: Optional[List[str]]
    api_data: Optional[List[CountryAPIData]]
    answer: Optional[str]



class CountryAPIData():
    is_error:bool
    data: dict|str


