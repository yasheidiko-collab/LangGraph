from graph import graph

query = input("Enter Research Topic: ")

result = graph.invoke(
    {
        "query": query,
        "plan": "",
        "technical_research": "",
        "business_research": "",
        "merged_research": "",
        "summary": "",
        "review": "",
        "final_report": "",
        "retry_count": 0
    }
)

print("\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)
print(result["final_report"])