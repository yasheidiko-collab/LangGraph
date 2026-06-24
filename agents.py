from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


# -----------------------------------
# Technology Research Agent
# -----------------------------------

def technology_agent(state):

    topic = state["topic"]

    prompt = f"""
    You are an expert technology researcher.

    Research the following topic:

    {topic}

    Include:

    - Overview
    - Architecture
    - Advantages
    - Challenges

    Give concise notes.
    """

    response = llm.invoke(prompt)

    return {

        "technology_research": response.content

    }


# -----------------------------------
# Business Research Agent
# -----------------------------------

def business_agent(state):

    topic = state["topic"]

    prompt = f"""
    You are a business analyst.

    Research:

    {topic}

    Include:

    - Market
    - Companies
    - Adoption
    - Revenue opportunities

    Give concise notes.
    """

    response = llm.invoke(prompt)

    return {

        "business_research": response.content

    }


# -----------------------------------
# Future Trends Agent
# -----------------------------------

def future_agent(state):

    topic = state["topic"]

    prompt = f"""
    You are a futurist.

    Research:

    {topic}

    Include:

    - Future scope
    - Innovations
    - Risks
    - Predictions

    Give concise notes.
    """

    response = llm.invoke(prompt)

    return {

        "future_research": response.content

    }


# -----------------------------------
# Report Generator
# -----------------------------------

def report_generator(state):

    prompt = f"""

Create a professional research report.

Topic

{state["topic"]}

Technology Research

{state["technology_research"]}

Business Research

{state["business_research"]}

Future Research

{state["future_research"]}

Generate:

Title

Summary

Technology Section

Business Section

Future Section

Conclusion

"""

    response = llm.invoke(prompt)

    return {

        "final_report": response.content

    }