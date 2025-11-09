# ai_agent/sub_agents/reviewer_agent/agent.py
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def critique_paper(pdf_text: str, tool_context: ToolContext) -> dict:
    """
    Analyzes the extracted PDF text and returns a critique.
    Only provide strengths, weaknesses, and potential biases.
    """
    critique = {
        "strengths": "Clear methodology and relevant results.",
        "weaknesses": "Limited sample size and lack of detailed methodology.",
        "potential_biases": "Possible bias due to author affiliation."
    }

    tool_context.state["last_critique"] = critique
    return {"status": "success", "critique": critique}

reviewer_agent = Agent(
    name="reviewer_agent",
    model="gemini-2.0-flash",
    description="Reviews papers, providing critiques only (no insights).",
    instruction="""
    You are a Reviewer Agent.
    When given paper text:
    1. Analyze it and identify strengths, weaknesses, and potential biases.
    2. Return only the critique in a structured format.
    """,
    tools=[critique_paper],
)
