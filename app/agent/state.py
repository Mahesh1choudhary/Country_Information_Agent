from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    question: str
    country: Optional[str]
    fields: Optional[List[str]]
    api_data: Optional[dict]
    answer: Optional[str]
    error: Optional[str]


