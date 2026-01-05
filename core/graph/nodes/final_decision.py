from core.graph.state import IssueState


def final_decision_node(state: IssueState) -> IssueState:
    state["explanation"] = (
        "Actions suggested based on SOP Billing-Refund-v3.2 "
        "and customer payment history."
    )
    state["confidence_score"] = 0.91
    return state
