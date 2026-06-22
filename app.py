from typing import TypedDict
from dotenv import load_dotenv

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq

load_dotenv()

# ------------------------
# LLM
# ------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ------------------------
# State
# ------------------------

class AgentState(TypedDict):
    question: str
    answer: str
    feedback: str
    score: int
    iteration: int


# ------------------------
# Generate Node
# ------------------------

def generate(state):

    print("\nGenerating Answer...\n")

    prompt = f"""
    Answer the following question.

    Question:
    {state['question']}

    Give a clear and concise answer.
    """

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ------------------------
# Reflection Node
# ------------------------

def reflect(state):

    print("\nReviewing Answer...\n")

    prompt = f"""
You are an AI reviewer.

Question:
{state['question']}

Answer:
{state['answer']}

Evaluate the answer from 1 to 10.

Return ONLY this format:

Score: <number>

Feedback:
<feedback>
"""

    response = llm.invoke(prompt)

    text = response.content

    score = 5

    try:

        for line in text.split("\n"):

            if line.lower().startswith("score"):

                score = int(line.split(":")[1].strip())

    except:

        score = 5

    return {
        "feedback": text,
        "score": score,
        "iteration": state["iteration"] + 1
    }


# ------------------------
# Improve Node
# ------------------------

def improve(state):

    print("\nImproving Answer...\n")

    prompt = f"""
Question:
{state['question']}

Current Answer:
{state['answer']}

Reviewer Feedback:
{state['feedback']}

Generate a much better answer.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ------------------------
# Router
# ------------------------

def router(state):

    print("\nChecking Quality...\n")

    print("Score:", state["score"])

    if state["score"] >= 8:

        print("\nAnswer Accepted\n")

        return "finish"

    if state["iteration"] >= 3:

        print("\nMaximum iterations reached\n")

        return "finish"

    print("\nNeeds Improvement\n")

    return "improve"


# ------------------------
# Graph
# ------------------------

builder = StateGraph(AgentState)

builder.add_node("generate", generate)
builder.add_node("reflect", reflect)
builder.add_node("improve", improve)

builder.set_entry_point("generate")

builder.add_edge("generate", "reflect")

builder.add_conditional_edges(
    "reflect",
    router,
    {
        "improve": "improve",
        "finish": END
    }
)

builder.add_edge("improve", "reflect")

graph = builder.compile()

# ------------------------
# Run
# ------------------------

question = input("\nEnter your question: ")

result = graph.invoke(
    {
        "question": question,
        "answer": "",
        "feedback": "",
        "score": 0,
        "iteration": 0
    }
)

print("\n")
print("=" * 70)
print("FINAL ANSWER")
print("=" * 70)
print(result["answer"])
print("=" * 70)





    #                User Question
    #                       |
    #                       |
    #                Generate Answer
    #                     |
    #                       |
    #                  Reflect / Review
    #                       |
    #                       |
    #                Score >= 8 ?
    #                  /           \
    #                Yes            No
    #                  |              |
    #                  |         Improve Answer
    #                  |              |
    #                  |              |
    #                  ------<---------
    #                       |
    #                       END

