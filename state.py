from typing import TypedDict


class SupportState(TypedDict):
    user_message: str
    category: str
    response: str
    logs: str