from core.graph.state import IssueState


def rag_node(state: IssueState) -> IssueState:
    """
    Retrieve relevant SOPs / past tickets
    """
    # Placeholder – will connect vector DB later
    state["rag_context"] = [
        {
            "source": "Billing-Refund-v3.2",
            "summary": "Duplicate charge handling procedure"
        }
    ]
    return state
