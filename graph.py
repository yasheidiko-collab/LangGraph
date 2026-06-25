from langgraph.graph import StateGraph, END

from state import ResearchState

from agents import (
    manager_agent,
    technical_researcher,
    business_researcher,
    merge_agent,
    summarizer_agent,
    reviewer_agent,
    retry_node,
    final_report_agent,
    review_router
)

builder = StateGraph(ResearchState)

builder.add_node("manager", manager_agent)

builder.add_node("technical", technical_researcher)

builder.add_node("business", business_researcher)

builder.add_node("merge", merge_agent)

builder.add_node("summarizer", summarizer_agent)

builder.add_node("reviewer", reviewer_agent)

builder.add_node("retry", retry_node)

builder.add_node("final", final_report_agent)

builder.set_entry_point("manager")


# MANAGER → RESEARCHERS

builder.add_edge("manager", "technical")

builder.add_edge("manager", "business")


# BOTH RESEARCHERS → MERGE

builder.add_edge("technical", "merge")

builder.add_edge("business", "merge")


# MERGE → SUMMARIZER

builder.add_edge("merge", "summarizer")


# SUMMARIZER → REVIEWER

builder.add_edge("summarizer", "reviewer")


# REVIEW ROUTING

builder.add_conditional_edges(
    "reviewer",
    review_router,
    {
        "retry": "retry",
        "approved": "final"
    }
)


# RETRY LOOP

builder.add_edge("retry", "technical")

builder.add_edge("retry", "business")


# FINAL → END

builder.add_edge("final", END)

graph = builder.compile()