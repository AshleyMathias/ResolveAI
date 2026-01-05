from core.graph.state import IssueState


def needs_escalation(state: IssueState) -> str:
    if state["requires_escalation"]:
        return "escalate"
    return "finalize"
