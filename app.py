from graph import graph


def main():

    print("\n" + "=" * 60)
    print("      HR MULTI-AGENT SYSTEM")
    print("=" * 60)

    while True:

        print("\nAvailable Queries:")

        print("1. Apply for Job")
        print("2. Salary Details")
        print("3. Salary Change")
        print("4. Leave Request")
        print("5. Exit")

        query = input("\nEnter your request: ")
        

        if query == "5":

            print("\nThank you!")

            break

        state = {

            "messages": [query],

            "current_agent": "",

            "task_complete": False,

            "approved": True

        }

        graph.invoke(state)

        print("\nWorkflow Completed")


if __name__ == "__main__":

    main()