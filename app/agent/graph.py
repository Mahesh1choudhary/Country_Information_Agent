from langgraph.graph import StateGraph, END

from app.agent.nodes import identify_intent, fetch_related_data, synthesize_answer
from app.agent.state import AgentState

workflow  = StateGraph(AgentState)

workflow.add_node("intent", identify_intent)
workflow.add_node("data_retrieval", fetch_related_data)
workflow.add_node("synthesize", synthesize_answer)

workflow.set_entry_point("intent")

workflow.add_edge("intent", "data_retrieval")
workflow.add_edge("data_retrieval", "synthesize")
workflow.add_edge("synthesize", END)


query_graph = workflow.compile()


