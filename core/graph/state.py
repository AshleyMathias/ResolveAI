from typing import TypedDict, Optional, List, Dict, Any


class IssueState(TypedDict, total=False):
    # Raw input
    issue_id: Optional[str]
    raw_issue_text: str
    source: str

    # Extracted understanding
    issue_type: Optional[str]
    severity: Optional[str]
    customer_id: Optional[str]
    missing_info: List[str]

    # Context
    rag_context: List[Dict[str, Any]]
    mcp_data: Dict[str, Any]

    # Reasoning and decision
    proposed_actions: List[Dict[str, Any]]
    validated_actions: List[Dict[str, Any]]
    explanation: Optional[str]
    confidence_score: Optional[float]

    # Control flags
    requires_escalation: bool
    errors: List[str]