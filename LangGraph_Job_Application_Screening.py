from typing import TypedDict
from langgraph.graph import StateGraph


# ---------------------------------
# Define State
# ---------------------------------
class JobApplicationState(TypedDict):
    name: str
    role: str
    experience: int
    decision: str


# ---------------------------------
# Node 1: Receive Application
# ---------------------------------
def receive_application(state: JobApplicationState):
    print("\n===== Receiving Application =====")
    print(f"Applicant : {state['name']}")
    print(f"Role      : {state['role']}")
    print(f"Experience: {state['experience']} years")

    return {}


# ---------------------------------
# Node 2: Screen Resume
# ---------------------------------
def screen_resume(state: JobApplicationState):
    print("\n===== Screening Resume =====")

    if state["experience"] > 2:
        print("Resume Passed Screening")
        return {"decision": "Selected"}

    print("Resume Failed Screening")
    return {"decision": "Rejected"}


# ---------------------------------
# Node 3: Send Decision
# ---------------------------------
def send_decision(state: JobApplicationState):
    print("\n===== Final Decision =====")
    print(f"{state['name']} : {state['decision']}")

    return {}


# ---------------------------------
# Build Graph
# ---------------------------------
builder = StateGraph(JobApplicationState)

builder.add_node("receive_application", receive_application)
builder.add_node("screen_resume", screen_resume)
builder.add_node("send_decision", send_decision)

builder.set_entry_point("receive_application")

builder.add_edge("receive_application", "screen_resume")
builder.add_edge("screen_resume", "send_decision")

builder.set_finish_point("send_decision")

graph = builder.compile()


# ---------------------------------
# Execute Graph
# ---------------------------------
result = graph.invoke(
    {
        "name": "Yash",
        "role": "Python Developer",
        "experience": 3,
        "decision": ""
    }
)

print("\n===== Final State =====")
print(result)
