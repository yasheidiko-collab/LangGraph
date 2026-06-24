from typing import TypedDict


class HRState(TypedDict):

    # User conversation

    messages: list[str]

    # Selected agent

    current_agent: str

    # Workflow completed?

    task_complete: bool

    # HR approval

    approved: bool  