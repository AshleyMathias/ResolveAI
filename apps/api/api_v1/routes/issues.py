from fastapi import APIRouter
from core.graph.graph_builder import build_issue_graph

router = APIRouter()

graph = build_issue_graph()  # build once at startup


@router.post("/analyze")
def analyze_issue(payload: dict):
    """
    Entry point for issue analysis
    """
    initial_state = {
        "issue_id": payload.get("issue_id"),
        "raw_issue_text": payload.get("issue_text"),
        "source": payload.get("source", "api"),

        "issue_type": None,
        "severity": None,
        "customer_id": None,
        "missing_info": [],

        "rag_context": [],
        "mcp_data": {},

        "proposed_actions": [],
        "validated_actions": [],
        "explanation": None,
        "confidence_score": None,

        "requires_escalation": False,
        "errors": []
    }

    result = graph.invoke(initial_state)
    return result
