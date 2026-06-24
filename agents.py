from tools import (
    submit_application,
    salary_details,
    update_salary,
    leave_request,
)


# =====================================================
# Supervisor Agent
# =====================================================

def supervisor_agent(state):

    query = state["messages"][-1].lower()

    print("\n==============================")
    print("SUPERVISOR AGENT")
    print("==============================")

    if any(word in query for word in [
        "job",
        "apply",
        "application",
        "resume",
        "interview"
    ]):

        print("Routing -> Recruitment Agent")

        return {

            "current_agent": "recruitment"

        }

    elif any(word in query for word in [
        "salary",
        "pay",
        "bonus",
        "compensation",
        "increment",
        "increase"
    ]):

        print("Routing -> Payroll Agent")

        return {

            "current_agent": "payroll"

        }

    elif any(word in query for word in [
        "leave",
        "vacation",
        "holiday"
    ]):

        print("Routing -> Leave Agent")

        return {

            "current_agent": "leave"

        }

    print("Unable to identify request.")

    return {

        "task_complete": True

    }


# =====================================================
# Supervisor Router
# =====================================================

def supervisor_router(state):

    return state.get("current_agent", "end")


# =====================================================
# Recruitment Agent
# =====================================================

def recruitment_agent(state):

    print("\n==============================")
    print("RECRUITMENT AGENT")
    print("==============================")

    name = input("Candidate Name : ")

    role = input("Applying Role : ")

    result = submit_application(

        name,

        role

    )

    print(result)

    return {

        "task_complete": True

    }


# =====================================================
# Payroll Agent
# =====================================================

def payroll_agent(state):

    print("\n==============================")
    print("PAYROLL AGENT")
    print("==============================")

    print("\n1. View Salary")

    print("2. Change Salary")

    choice = input("\nSelect Option : ")

    # ----------------------------------

    if choice == "1":

        employee = input(

            "Employee Name : "

        )

        result = salary_details(

            employee

        )

        print(result)

        return {

            "approved": True,

            "task_complete": True

        }

    # ----------------------------------

    elif choice == "2":

        print(

            "\nSalary Change Requires HR Approval."

        )

        return {

            "approved": False,

            "task_complete": False

        }

    # ----------------------------------

    print("Invalid Choice")

    return {

        "task_complete": True

    }


# =====================================================
# Payroll Router
# =====================================================

def payroll_router(state):

    if state["approved"] is False:

        return "approval"

    return "end"


# =====================================================
# Approval Agent (HITL)
# =====================================================

def approval_agent(state):

    print("\n==============================")
    print("HR MANAGER APPROVAL")
    print("==============================")

    decision = input(

        "Approve Salary Change? (yes/no): "

    ).lower()

    if decision == "yes":

        employee = input(

            "Employee Name : "

        )

        amount = input(

            "New Salary : "

        )

        result = update_salary(

            employee,

            amount

        )

        print(result)

        return {

            "approved": True,

            "task_complete": True

        }

    print("\nSalary Change Rejected.")

    return {

        "approved": False,

        "task_complete": True

    }


# =====================================================
# Leave Agent
# =====================================================

def leave_agent(state):

    print("\n==============================")
    print("LEAVE AGENT")
    print("==============================")

    employee = input(

        "Employee Name : "

    )

    days = input(

        "Number of Leave Days : "

    )

    result = leave_request(

        employee,

        days

    )

    print(result)

    return {

        "task_complete": True

    }