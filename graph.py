from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from state import HRState

from agents import (
    supervisor_agent,
    supervisor_router,
    recruitment_agent,
    payroll_agent,
    payroll_router,
    approval_agent,
    leave_agent,
)

# ==========================================
# Create Graph
# ==========================================

builder = StateGraph(HRState)

# ==========================================
# Add Nodes
# ==========================================

builder.add_node(
    "supervisor",
    supervisor_agent,
)

builder.add_node(
    "recruitment",
    recruitment_agent,
)

builder.add_node(
    "payroll",
    payroll_agent,
)

builder.add_node(
    "approval",
    approval_agent,
)

builder.add_node(
    "leave",
    leave_agent,
)

# ==========================================
# Start
# ==========================================

builder.add_edge(
    START,
    "supervisor",
)

# ==========================================
# Supervisor Conditional Routing
# ==========================================

builder.add_conditional_edges(
    "supervisor",
    supervisor_router,
    {

        "recruitment": "recruitment",

        "payroll": "payroll",

        "leave": "leave",

        "end": END,

    },
)

# ==========================================
# Recruitment
# ==========================================

builder.add_edge(
    "recruitment",
    END,
)

# ==========================================
# Leave
# ==========================================

builder.add_edge(
    "leave",
    END,
)

# ==========================================
# Payroll Conditional Routing
# ==========================================

builder.add_conditional_edges(
    "payroll",
    payroll_router,
    {

        "approval": "approval",

        "end": END,

    },
)

# ==========================================
# Approval
# ==========================================

builder.add_edge(
    "approval",
    END,
)

# ==========================================
# Compile Graph
# ==========================================

graph = builder.compile()