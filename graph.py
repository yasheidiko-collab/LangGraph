from psycopg import connect

from langgraph.graph import StateGraph
from langgraph.graph import END

from langgraph.checkpoint.postgres import PostgresSaver

from state import SupportState

from agents import (
    classify_node,
    respond_node,
    log_node
)

from config import DATABASE_URL

builder = StateGraph(SupportState)

builder.add_node(
    "classify",
    classify_node
)

builder.add_node(
    "respond",
    respond_node
)

builder.add_node(
    "log",
    log_node
)

builder.set_entry_point(
    "classify"
)

builder.add_edge(
    "classify",
    "respond"
)

builder.add_edge(
    "respond",
    "log"
)

builder.add_edge(
    "log",
    END
)

conn = connect(
    DATABASE_URL
)

checkpointer = PostgresSaver(conn)

graph = builder.compile(
    checkpointer=checkpointer
)

