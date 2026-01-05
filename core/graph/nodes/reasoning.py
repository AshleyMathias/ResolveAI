from core.graph.state import IssueState
from core.llm.openai_client import get_openai_client
from core.llm.output_schemas import ReasoningResult
from openai import OpenAI


def reasoning_node(state: IssueState) -> IssueState:
    client: OpenAI = get_openai_client()

    context = {
        "issue_type": state["issue_type"],
        "severity": state["severity"],
        "rag_context": state["rag_context"],
        "mcp_data": state["mcp_data"]
    }

    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": open(
                    "core/llm/prompts/decision_reasoning.md"
                ).read()
            },
            {
                "role": "user",
                "content": f"{context}"
            }
        ],
        response_format=ReasoningResult
    )

    result: ReasoningResult = response.output_parsed

    state["proposed_actions"] = [
        action.model_dump() for action in result.actions
    ]
    state["confidence_score"] = result.confidence

    return state
