# 🚀 HR Multi-Agent System using LangGraph

## 📌 Project Overview

The **HR Multi-Agent System** is a LangGraph-based application that demonstrates how multiple specialized AI agents can collaborate to automate Human Resource tasks.

The system uses a **Supervisor Agent** that analyzes the user's request and routes it to the appropriate specialized agent.

The project also demonstrates **Human-in-the-Loop (HITL)** by requiring HR Manager approval before processing any salary change request.

---

# 🎯 Objectives

* Learn LangGraph fundamentals
* Understand Multi-Agent Architecture
* Implement Supervisor Pattern
* Use Conditional Routing
* Implement Human-in-the-Loop (HITL)
* Build an enterprise-style AI workflow

---

# 🏗️ System Architecture

```text
                          START
                             │
                             ▼
                     User HR Request
                             │
                             ▼
                     Supervisor Agent
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 Recruitment Agent     Payroll Agent       Leave Agent
                              │
                              ▼
                    Salary Change Request?
                       │                │
                      YES               NO
                       │                │
                       ▼                ▼
              HR Manager Approval      END
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         Approved             Rejected
             │                   │
             ▼                   ▼
      Update Salary         Stop Workflow
             │
             ▼
            END
```

---

# 📂 Project Structure

```text
HRMultiAgent/

│
├── app.py
├── graph.py
├── agents.py
├── tools.py
├── state.py
├── requirements.txt
├── README.md
└── .env (optional)
```

---

# 📋 Features

* ✅ Supervisor Agent
* ✅ Recruitment Agent
* ✅ Payroll Agent
* ✅ Leave Agent
* ✅ Conditional Routing
* ✅ Shared State
* ✅ Human-in-the-Loop (HITL)
* ✅ Modular Design
* ✅ CLI Based Interface

---

# 🛠 Technologies Used

* Python
* LangGraph
* TypedDict
* StateGraph
* Conditional Edges

---

# 📦 Installation

## Step 1

Clone or create the project directory.

```bash
mkdir HRMultiAgent
cd HRMultiAgent
```

---

## Step 2

Create a virtual environment.

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

```bash
python app.py
```

---

# 📊 State Definition

The application uses a shared state.

```python
class HRState(TypedDict):

    messages: list[str]

    current_agent: str

    task_complete: bool

    approved: bool
```

---

# 🧠 Agents

## 1. Supervisor Agent

### Responsibilities

* Receives user request
* Identifies request type
* Routes workflow

### Example

```text
Apply for Python Developer

↓

Recruitment Agent
```

---

## 2. Recruitment Agent

Handles:

* Job Applications
* Resume Submission
* Candidate Registration

### Example

```text
Candidate Name : Rahul

Role : Python Developer

↓

Application Submitted Successfully
```

---

## 3. Payroll Agent

Handles:

* Salary Details
* Bonus Information
* Compensation Queries

### Example

```text
Employee : Rahul

Salary : ₹55,000
```

---

## 4. Leave Agent

Handles:

* Leave Requests
* Vacation Requests
* Holiday Applications

### Example

```text
Employee : Rahul

Leave Days : 3

↓

Leave Request Submitted
```

---

# 👨‍💼 Human-in-the-Loop (HITL)

Any salary modification requires HR Manager approval.

Workflow:

```text
Employee

↓

Payroll Agent

↓

Salary Change?

↓

YES

↓

HR Manager Approval

↓

Approve?

↓

YES → Update Salary

NO → Reject Request
```

---

# 🔄 Execution Flow

```text
User Input

↓

Supervisor Agent

↓

Conditional Routing

↓

Recruitment Agent
OR
Payroll Agent
OR
Leave Agent

↓

(HITL for Salary Change)

↓

Task Complete

↓

END
```

---

# 🔀 Conditional Routing

Supervisor decides the next node.

```text
Job Query

↓

Recruitment Agent
```

```text
Salary Query

↓

Payroll Agent
```

```text
Leave Query

↓

Leave Agent
```

---

# 💡 Sample Execution

## Recruitment Flow

```text
User:

Apply for Job

↓

Supervisor Agent

↓

Recruitment Agent

↓

Enter Candidate Name

↓

Enter Role

↓

Application Submitted

↓

END
```

---

## Payroll Flow

```text
User:

Show Salary

↓

Supervisor Agent

↓

Payroll Agent

↓

Display Salary Details

↓

END
```

---

## Payroll with HITL

```text
User:

Increase Salary

↓

Supervisor Agent

↓

Payroll Agent

↓

Salary Change Detected

↓

HR Manager Approval

↓

Approve? yes

↓

Enter Employee Name

↓

Enter New Salary

↓

Salary Updated

↓

END
```

---

## Leave Flow

```text
User:

Apply Leave

↓

Supervisor Agent

↓

Leave Agent

↓

Enter Employee Name

↓

Enter Leave Days

↓

Leave Request Submitted

↓

END
```

---

# 📚 LangGraph Concepts Demonstrated

* StateGraph
* Nodes
* Edges
* Conditional Edges
* Supervisor Pattern
* Multi-Agent Architecture
* Shared State
* Human-in-the-Loop (HITL)

---

# 🎓 Learning Outcomes

After completing this project, you will understand:

* How LangGraph orchestrates multiple agents
* How a Supervisor Agent routes requests
* How Conditional Routing works
* How Human-in-the-Loop improves safety
* How shared state enables agent communication
* How enterprise AI workflows are structured

---

# 🔮 Future Enhancements

* ChatGroq/OpenAI Supervisor
* Tool Calling
* graph.stream() for node streaming
* Memory & Checkpointing
* PostgreSQL State Storage
* Streamlit UI
* Authentication
* Email Notifications
* Employee Database Integration
* Mermaid Graph Visualization

---

# 📌 Interview Questions

### What is a Supervisor Agent?

A Supervisor Agent analyzes a request and routes it to the appropriate specialized agent.

---

### What is Conditional Routing?

Conditional Routing dynamically decides the next node based on the current state.

---

### What is Human-in-the-Loop?

Human-in-the-Loop (HITL) introduces manual approval into an AI workflow for sensitive operations such as salary updates.

---

### Why use a Multi-Agent System?

* Better separation of responsibilities
* Modular architecture
* Easier maintenance
* Scalability
* Enterprise-ready workflows

---

# ⭐ Resume Description

**HR Multi-Agent System using LangGraph**

Developed a multi-agent HR automation system using LangGraph featuring a Supervisor Agent, Recruitment Agent, Payroll Agent, and Leave Agent. Implemented conditional routing, shared state management, and Human-in-the-Loop approval for salary modifications, demonstrating enterprise AI workflow orchestration and stateful agent collaboration.

---

# 👨‍💻 Author

**Project:** HR Multi-Agent System using LangGraph

**Concepts Covered:** Multi-Agent Systems, Supervisor Pattern, Conditional Routing, Human-in-the-Loop, StateGraph, Shared State, Enterprise AI Workflows.
