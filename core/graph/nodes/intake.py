from core.graph.state import IssueState
from core.llm.openai_client import get_openai_client
from core.llm.output_schemas import IntakeResult

from openai import OpenAI


def intake_node(state: IssueState) -> IssueState:
    client: OpenAI = get_openai_client()

    prompt = f"""
Customer Issue:
{state['raw_issue_text']}
"""

    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": open(
                    "core/llm/prompts/issue_analysis.md"
                ).read()
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format=IntakeResult
    )

    result: IntakeResult = response.output_parsed

    state["issue_type"] = result.issue_type
    state["severity"] = result.severity
    state["customer_id"] = result.customer_id
    state["missing_info"] = result.missing_info

    return state
