from core.graph.state import IssueState


def intake_node(state: IssueState) -> IssueState:
    """
    Normalize and validate incoming issue
    """

    if not state.get("raw_issue_text"):
        state["erros"].append("Empty issue text")
        return state

    #placeholder logic
    state["issue_type"] = "billing"        
    state["severity"] = "high"
    state["missing_info"] = []

    return state