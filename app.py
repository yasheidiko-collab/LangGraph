from graph import graph

topic = input(

    "\nEnter research topic : "

)

result = graph.invoke(

    {

        "topic": topic

    }

)

print("\n")

print("=" * 80)

print(result["final_report"])

print("=" * 80)