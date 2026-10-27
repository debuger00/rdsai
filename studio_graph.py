from langgraph.graph import END, START, StateGraph

from loop.nodes import agent_node, should_continue, tools_node
from loop.state import AgentState

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", tools_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END,
    },
)
builder.add_edge("tools", "agent")

graph = builder.compile()