import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")

LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")

LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")

from datetime import datetime

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

from langchain_groq import ChatGroq

from langfuse import Langfuse

from config import (
    GROQ_API_KEY,
    LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY,
    LANGFUSE_HOST
)

langfuse = Langfuse(
    public_key=LANGFUSE_PUBLIC_KEY,
    secret_key=LANGFUSE_SECRET_KEY,
    host=LANGFUSE_HOST
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1)
)
def call_llm(prompt):
    return llm.invoke(prompt)

def classify_node(state):

    query = state["user_message"]

    trace = langfuse.trace(
        name="classifier"
    )

    prompt = f"""
Classify this customer query.

Return only one category:

billing
technical
general

Query:
{query}
"""

    result = call_llm(prompt)

    trace.update(
        output=result.content
    )

    return {
        "category": result.content.strip()
    }

def respond_node(state):

    query = state["user_message"]

    category = state["category"]

    trace = langfuse.trace(
        name="responder"
    )

    prompt = f"""
You are a support agent.

Category:
{category}

Customer Query:
{query}

Provide a helpful answer.
"""

    result = call_llm(prompt)

    trace.update(
        output=result.content
    )

    return {
        "response": result.content
    }

def log_node(state):

    log_message = f"""
Time: {datetime.now()}

Category: {state['category']}
"""

    return {
        "logs": log_message
    }

