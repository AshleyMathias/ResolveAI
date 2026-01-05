from langgraph.graph import StateGraph, END
from core.graph.state import IssueState

from core.graph.nodes.intake import intake_node
from core.graph.nodes.rag_node import rag_node
from core.graph.nodes.mcp_node import mcp_node
from core.graph.nodes.reasoning import reasoning_node
from core.graph.nodes.rule_validation import rule_validation_node
from core.graph.nodes.final_decision import final_decision_node
from core.graph.edges import needs_escalation


def build_issue_graph():
    graph = StateGraph(IssueState)

    graph.add_node("intake", intake_node)
    graph.add_node("rag", rag_node)
    graph.add_node("mcp", mcp_node)
    graph.add_node("reasoning", reasoning_node)
    graph.add_node("rule_validation", rule_validation_node)
    graph.add_node("finalize", final_decision_node)

    graph.set_entry_point("intake")

    graph.add_edge("intake", "rag")
    graph.add_edge("rag", "mcp")
    graph.add_edge("mcp", "reasoning")
    graph.add_edge("reasoning", "rule_validation")

    graph.add_conditional_edges(
        "rule_validation",
        needs_escalation,
        {
            "finalize": "finalize",
            "escalate": END
        }
    )

    graph.add_edge("finalize", END)

    return graph.compile()
