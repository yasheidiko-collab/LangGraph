from typing import TypedDict
from langgraph.graph import StateGraph


# -------------------------
# Define State
# -------------------------
class MyState(TypedDict):
    name: str
    greeting: str


# -------------------------
# Node 1
# -------------------------
def greet_node(state: MyState):
    print("Running Greeting Node...")
    return {
        "greeting": f"Hello {state['name']}"
    }


# -------------------------
# Node 2
# -------------------------
def uppercase_node(state: MyState):
    print("Running Uppercase Node...")
    return {
        "greeting": state["greeting"].upper()
    }


# -------------------------
# Build Graph
# -------------------------
builder = StateGraph(MyState)

builder.add_node("greet", greet_node)
builder.add_node("uppercase", uppercase_node)

builder.set_entry_point("greet")
builder.add_edge("greet", "uppercase")
builder.set_finish_point("uppercase")

graph = builder.compile()


# -------------------------
# Run Graph
# -------------------------
result = graph.invoke(
    {
        "name": "Yash"
    }
)

print("\nFinal State:")
print(result)