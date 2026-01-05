import os
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

    # Read the system prompt
    prompt_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "llm", "prompts", "issue_analysis.md"
    )
    
    with open(prompt_path, "r", encoding="utf-8") as f:
        system_prompt = f.read()

    # Use beta structured outputs API
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format=IntakeResult
    )

    result: IntakeResult = response.choices[0].message.parsed

    state["issue_type"] = result.issue_type
    state["severity"] = result.severity
    state["customer_id"] = result.customer_id
    state["missing_info"] = result.missing_info

    return state
