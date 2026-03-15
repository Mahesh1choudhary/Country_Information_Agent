import json
from app.commons.service_logger import setup_logger
from app.commons.query_model import Query
from app.agent.state import AgentState

logger = setup_logger()
class QueryService():
    def __init__(self, graph):
        self.graph = graph


    async def generate_query_response(self, query:Query):
        try:
            query_question = query.query
            logger.info(f"Starting Graph for query: {query_question}")

            result:AgentState = await self.graph.ainvoke({"query": query_question})
            logger.info(f"Graph Execution Completed for query: {query_question}")
            logger.debug(f"For query: {query_question}, Final result: {result}")

            final_result = []
            for country_data in result['api_data']:
                data = {}
                for field, field_data in country_data.data.items():
                    if field == "name":
                        data["country_name"] = field_data["official"]
                    else:
                        data[field] = field_data

                final_result.append(data)
            return final_result
        except Exception as exc:
            logger.error(f"Error generating query response. Error:{exc}", exc_info=True)
            raise exc


