from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import ResearchState

from agents import technology_agent
from agents import business_agent
from agents import future_agent
from agents import report_generator


builder = StateGraph(ResearchState)

# Nodes

builder.add_node(
    "technology",
    technology_agent
)

builder.add_node(
    "business",
    business_agent
)

builder.add_node(
    "future",
    future_agent
)

builder.add_node(
    "report",
    report_generator
)

# Fan-out

builder.add_edge(
    START,
    "technology"
)

builder.add_edge(
    START,
    "business"
)

builder.add_edge(
    START,
    "future"
)

# Fan-in

builder.add_edge(
    "technology",
    "report"
)

builder.add_edge(
    "business",
    "report"
)

builder.add_edge(
    "future",
    "report"
)

builder.add_edge(
    "report",
    END
)

graph = builder.compile()