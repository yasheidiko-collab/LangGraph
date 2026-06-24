from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# -----------------------
# State
# -----------------------
class State(TypedDict):
    message: str


# -----------------------
# Nodes
# -----------------------
def greet(state: State):
    print("\nExecuting Greeting Node...")
    return {
        "message": "hello langgraph"
    }


def uppercase(state: State):
    print("\nExecuting Uppercase Node...")
    return {
        "message": state["message"].upper()
    }


def add_emoji(state: State):
    print("\nExecuting Emoji Node...")
    return {
        "message": state["message"] + " 🚀"
    }


# -----------------------
# Build Graph
# -----------------------
builder = StateGraph(State)

builder.add_node("greet", greet)
builder.add_node("uppercase", uppercase)
builder.add_node("emoji", add_emoji)

builder.add_edge(START, "greet")
builder.add_edge("greet", "uppercase")
builder.add_edge("uppercase", "emoji")
builder.add_edge("emoji", END)

graph = builder.compile()


# -----------------------
# Streaming Execution
# -----------------------
print("\n===== Streaming Output =====\n")

for event in graph.stream({}):
    print(event)