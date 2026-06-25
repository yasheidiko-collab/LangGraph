from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


# --------------------------
# MANAGER
# --------------------------

def manager_agent(state):

    query = state["query"]

    return {
        "plan": f"""
Research Topic:
{query}

Collect:
1. Technical Information
2. Business Applications
3. Benefits
4. Limitations
"""
    }


# --------------------------
# TECHNICAL RESEARCHER
# --------------------------

def technical_researcher(state):

    query = state["query"]

    response = llm.invoke(
        f"""
Research technical aspects of:

{query}

Include:
- Architecture
- Features
- Components
- Technical Details
"""
    )

    return {
        "technical_research": response.content
    }


# --------------------------
# BUSINESS RESEARCHER
# --------------------------

def business_researcher(state):

    query = state["query"]

    response = llm.invoke(
        f"""
Research business aspects of:

{query}

Include:
- Business Value
- Use Cases
- ROI
- Adoption Challenges
"""
    )

    return {
        "business_research": response.content
    }


# --------------------------
# MERGE
# --------------------------

def merge_agent(state):

    merged = f"""
TECHNICAL RESEARCH

{state["technical_research"]}

-----------------------------------

BUSINESS RESEARCH

{state["business_research"]}
"""

    return {
        "merged_research": merged
    }


# --------------------------
# SUMMARIZER
# --------------------------

def summarizer_agent(state):

    research = state["merged_research"]

    response = llm.invoke(
        f"""
Summarize the following research.

Research:

{research}
"""
    )

    return {
        "summary": response.content
    }


# --------------------------
# REVIEWER
# --------------------------

def reviewer_agent(state):

    summary = state["summary"]

    response = llm.invoke(
        f"""
Review the report.

Check:
- Accuracy
- Completeness
- Missing Information

Return ONLY:

APPROVED

or

RESEARCH_AGAIN

Then explain why.

Report:

{summary}
"""
    )

    return {
        "review": response.content
    }


# --------------------------
# RETRY NODE
# --------------------------

def retry_node(state):

    return {
        "retry_count": state["retry_count"] + 1
    }


# --------------------------
# FINAL REPORT
# --------------------------

def final_report_agent(state):

    return {
        "final_report": state["summary"]
    }


# --------------------------
# ROUTER
# --------------------------

def review_router(state):

    review = state["review"].upper()

    retries = state["retry_count"]

    if "RESEARCH_AGAIN" in review and retries < 2:
        return "retry"

    return "approved"