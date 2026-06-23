from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver


# -------------------------------------------------
# State
# -------------------------------------------------

class EmployeeState(TypedDict):
    employee_name: str
    docs_collected: bool
    access_setup: bool
    orientation_scheduled: bool
    status: str


# -------------------------------------------------
# Node 1
# -------------------------------------------------

def document_collection(state: EmployeeState):

    print("\n📄 Collecting Documents...")

    return {
        "docs_collected": True,
        "status": "Documents Collected"
    }


# -------------------------------------------------
# Node 2
# -------------------------------------------------

def system_access_setup(state: EmployeeState):

    print("\n💻 Creating System Access...")

    return {
        "access_setup": True,
        "status": "Access Created"
    }


# -------------------------------------------------
# Node 3
# -------------------------------------------------

def orientation_scheduling(state: EmployeeState):

    print("\n📅 Scheduling Orientation...")

    return {
        "orientation_scheduled": True,
        "status": "Employee Onboarding Completed"
    }


# -------------------------------------------------
# Build Graph
# -------------------------------------------------

builder = StateGraph(EmployeeState)

builder.add_node("document_collection", document_collection)
builder.add_node("system_access_setup", system_access_setup)
builder.add_node("orientation_scheduling", orientation_scheduling)

builder.add_edge(START, "document_collection")
builder.add_edge("document_collection", "system_access_setup")
builder.add_edge("system_access_setup", "orientation_scheduling")
builder.add_edge("orientation_scheduling", END)


# -------------------------------------------------
# PostgreSQL Connection
# -------------------------------------------------

DB_URI = (
    "postgresql://yash:password123@localhost:5432/langgraph_db"
)


with PostgresSaver.from_conn_string(DB_URI) as checkpointer:

    # Creates required tables
    checkpointer.setup()

    graph = builder.compile(
        checkpointer=checkpointer
    )

    # ---------------------------------------------
    # User Input
    # ---------------------------------------------

    employee_name = input("Enter Employee Name : ")

    employee_id = input("Enter Employee ID : ")

    config = {
        "configurable": {
            "thread_id": employee_id
        }
    }

    # ---------------------------------------------
    # Invoke
    # ---------------------------------------------

    result = graph.invoke(

        {

            "employee_name": employee_name,

            "docs_collected": False,

            "access_setup": False,

            "orientation_scheduled": False,

            "status": "Started"

        },

        config=config

    )

    print("\n==============================")
    print("FINAL RESULT")
    print("==============================")

    print(result)

    # ---------------------------------------------
    # Read Saved State
    # ---------------------------------------------

    saved_state = graph.get_state(config)

    print("\n==============================")
    print("SAVED STATE FROM POSTGRES")
    print("==============================")

    print(saved_state.values)