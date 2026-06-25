from typing import TypedDict


class ResearchState(TypedDict):
    query: str

    plan: str

    technical_research: str

    business_research: str

    merged_research: str

    summary: str

    review: str

    final_report: str

    retry_count: int