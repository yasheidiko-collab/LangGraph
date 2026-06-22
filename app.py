from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    query: str
    result: str

def math_node(state):

    expression = state["query"].replace("calculate", "").strip()

    try:
        answer = eval(expression)
        state["result"] = f"Math Answer: {answer}"

    except:
        state["result"] = "Invalid Math Expression"

    return state

def search_node(state):

    state["result"] = (
        f"Searching for: {state['query']}"
    )

    return state


def chat_node(state):

    state["result"] = (
        f"Chat Response: {state['query']}"
    )

    return state


def router(state):

    query = state["query"].lower()

    if "calculate" in query:
        return "math"

    elif "search" in query:
        return "search"

    else:
        return "chat"
    

builder = StateGraph(State)

builder.add_node("math_node", math_node)
builder.add_node("search_node", search_node)
builder.add_node("chat_node", chat_node)

builder.set_entry_point("router")



def router_node(state):
    return state

builder.add_node("router", router_node)



builder.add_conditional_edges(
    "router",
    router,
    {
        "math": "math_node",
        "search": "search_node",
        "chat": "chat_node"
    }
)


builder.add_edge("math_node", END)
builder.add_edge("search_node", END)
builder.add_edge("chat_node", END)

graph = builder.compile()




result = graph.invoke({
    "query": "calculate 25 + 75"
})

print(result["result"])

result = graph.invoke({
    "query": "search latest AI news"
})

print(result["result"])

result = graph.invoke({
    "query": "write a poem"
})

print(result["result"])