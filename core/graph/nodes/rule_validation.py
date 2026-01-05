from core.graph.state import IssueState


def rule_validation_node(state: IssueState) -> IssueState:
    """
    Enforce enterprise rules & policies
    """
    validated = []

    proposed_actions = state.get("proposed_actions", [])
    for action in proposed_actions:
        # Simple placeholder rule
        if action.get("action") != "initiate_refund":
            validated.append(action)

    state["validated_actions"] = validated
    state["requires_escalation"] = len(validated) == 0
    return state
