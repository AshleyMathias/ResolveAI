from pydantic import BaseModel
from typing import List, Optional


class IntakeResult(BaseModel):
    issue_type: str
    severity: str
    customer_id: Optional[str]
    missing_info: List[str]


class ProposedAction(BaseModel):
    action: str
    reason: str


class ReasoningResult(BaseModel):
    actions: List[ProposedAction]
    confidence: float
