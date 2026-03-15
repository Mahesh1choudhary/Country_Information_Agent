from app.service.query_service import QueryService
from app.agent.graph import query_graph


def get_query_service():
    return QueryService(query_graph)