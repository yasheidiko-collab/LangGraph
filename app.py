from fastapi import FastAPI

from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from graph import graph

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str
    message: str


async def stream_response(
    session_id,
    message
):

    config = {
        "configurable": {
            "thread_id": session_id
        }
    }

    for event in graph.stream(
        {
            "user_message": message,
            "category": "",
            "response": "",
            "logs": ""
        },
        config=config
    ):

        yield f"{event}\n"


@app.post("/support/chat")
async def support_chat(
    request: ChatRequest
):

    return StreamingResponse(
        stream_response(
            request.session_id,
            request.message
        ),
        media_type="text/plain"
    )

