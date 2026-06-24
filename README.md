# 🚀 Parallel Research Agent using LangGraph

## 📌 Overview

The **Parallel Research Agent** is a multi-agent AI application built with **LangGraph** that demonstrates **Fan-out / Fan-in** and **Parallel Execution**.

Given a research topic, the system launches multiple specialized AI agents simultaneously:

* **Technology Research Agent**
* **Business Research Agent**
* **Future Trends Research Agent**

Each agent independently researches the topic from its own perspective. Their outputs are then merged by a **Report Generator Agent**, which produces a structured research report.

---

# 🎯 Objectives

* Learn LangGraph fundamentals
* Understand Fan-out / Fan-in patterns
* Implement Parallel AI Agents
* Work with Shared State
* Generate structured AI reports
* Build an interview-ready LangGraph project

---

# 🏗️ Project Architecture

```text
                               START
                                  │
                                  ▼
                          User Research Topic
                                  │
                                  ▼
                           Shared State Created
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
 Technology Agent         Business Agent          Future Trends Agent
        │                         │                         │
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  ▼
                        Report Generator Agent
                                  │
                                  ▼
                                 END
```

---

# 📁 Project Structure

```text
ParallelResearchAgent/

│
├── app.py
├── graph.py
├── agents.py
├── state.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM
* python-dotenv

---

# 📦 Installation

## 1. Clone or create the project

```bash
mkdir ParallelResearchAgent
cd ParallelResearchAgent
```

---

## 2. Create a virtual environment

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

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Running the Project

Execute:

```bash
python app.py
```

---

# 💻 Example

### Input

```text
Enter research topic:

Artificial Intelligence
```

---

### Execution Flow

```text
User Input
     │
     ▼
Create Shared State
     │
     ▼
==========================

      Fan-out

==========================

Technology Agent

Business Agent

Future Agent

==========================

 Parallel Processing

==========================

Technology Research

Business Research

Future Research

==========================

       Fan-in

==========================

Report Generator

     │
     ▼

Final Research Report

     │
     ▼

END
```

---

# 📊 Shared State

```python
ResearchState

topic: str

technology_research: str

business_research: str

future_research: str

final_report: str
```

Each node reads from and writes to the shared state.

---

# 🧠 Agents

## Technology Agent

Researches:

* Overview
* Architecture
* Advantages
* Challenges

---

## Business Agent

Researches:

* Market
* Companies
* Adoption
* Revenue Opportunities

---

## Future Trends Agent

Researches:

* Innovations
* Future Scope
* Risks
* Predictions

---

## Report Generator

Combines all research into a professional report with:

* Title
* Summary
* Technology Analysis
* Business Analysis
* Future Trends
* Conclusion

---

# 🔄 LangGraph Concepts Demonstrated

✅ StateGraph

✅ Shared State

✅ Nodes

✅ Edges

✅ Fan-out

✅ Fan-in

✅ Parallel Agent Design

✅ Multi-Agent Collaboration

✅ Report Generation

---

# 🎓 Learning Outcomes

After completing this project, you will understand:

* How LangGraph models workflows
* How multiple agents can work together
* How Fan-out creates parallel branches
* How Fan-in merges multiple results
* How shared state enables communication between nodes
* How AI orchestration differs from a simple LLM call

---

# 🚀 Future Enhancements

* Planner Agent
* Critic Agent
* Web Search Integration
* Streaming with `graph.stream()`
* Memory & Checkpointing
* Markdown/PDF Export
* Streamlit User Interface
* Human-in-the-loop Approval

---

# 📈 Interview Questions

### What is Fan-out?

Fan-out is a workflow pattern where one node triggers multiple independent nodes that can execute simultaneously.

---

### What is Fan-in?

Fan-in is the process of merging outputs from multiple parallel branches into a single downstream node.

---

### Why use Parallel Agents?

* Faster execution
* Independent research
* Better information coverage
* Modular architecture
* Improved scalability

---

### Why LangGraph?

LangGraph provides:

* Stateful workflows
* Conditional routing
* Parallel execution
* Multi-agent orchestration
* Checkpointing
* Streaming support

making it ideal for building production-ready AI systems.

---

# ⭐ Resume Description

**Parallel Multi-Agent Research Assistant using LangGraph**

Built a LangGraph-based AI research system that orchestrates multiple specialized research agents using Fan-out/Fan-in and parallel execution patterns. The application generates structured research reports by combining technology, business, and future trend analyses into a single synthesized output.
