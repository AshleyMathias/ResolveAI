from typing import TypedDict, Optional, List, Dict, Any


class IssueState(TypedDict):
    #raw input
    issue_id: str
    raw_issue_text: str
    source: str

    # Extracted understanding
    issue_type: Optional[str]
    severity: Optional[str]
    customer_id: Optional[str]
    missing_info: List[str]

    #context
    raw_context: List[Dict[str, Any]]
    mcp_data: Dict[str, Any]


    #Reasoning and decision
    proposed_actions: List[Dict[str, Any]]
    validated_actions: List[Dict[str, Any]]
    explanation: Optional[str]
    confidence_score: Optional[float]

    #control flags
    requires_escalation: bool
    erros: List[str]