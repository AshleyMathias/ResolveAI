import os
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

    # Read the system prompt
    prompt_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "llm", "prompts", "decision_reasoning.md"
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
                "content": f"{context}"
            }
        ],
        response_format=ReasoningResult
    )

    result: ReasoningResult = response.choices[0].message.parsed

    state["proposed_actions"] = [
        action.model_dump() for action in result.actions
    ]
    state["confidence_score"] = result.confidence

    return state
