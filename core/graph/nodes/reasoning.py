from core.graph.state import IssueState


def reasoning_node(state: IssueState) -> IssueState:
    """
    Propose actions based on context
    """
    state["proposed_actions"] = [
        {
            "action": "initiate_refund",
            "reason": "Duplicate charge detected"
        },
        {
            "action": "activate_subscription",
            "reason": "Payment retry successful"
        }
    ]
    return state
