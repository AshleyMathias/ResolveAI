from core.graph.state import IssueState


def mcp_node(state: IssueState) -> IssueState:
    """
    Fetch live data via MCP tools
    """
    # Placeholder for MCP calls
    state["mcp_data"] = {
        "customer_status": "active",
        "last_payment": "failed"
    }
    return state
