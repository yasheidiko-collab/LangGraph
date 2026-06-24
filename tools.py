def submit_application(name, role):

    return f"""
==================================

Application Submitted Successfully

Candidate : {name}

Role : {role}

Status : Under Review

==================================
"""


def salary_details(employee):

    return f"""
==================================

Employee : {employee}

Basic Salary : ₹50,000

Bonus : ₹5,000

Total Salary : ₹55,000

==================================
"""


def update_salary(employee, amount):

    return f"""
==================================

Salary Updated Successfully

Employee : {employee}

New Salary : ₹{amount}

==================================
"""


def leave_request(employee, days):

    return f"""
==================================

Leave Request Submitted

Employee : {employee}

Days Requested : {days}

Status : Pending Manager Approval

==================================
"""