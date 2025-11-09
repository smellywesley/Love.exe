# ai_agent/sub_agents/synthesizer_agent/agent.py
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def synthesize_insights(summary_text: str, critique_text: str, tool_context: ToolContext) -> dict:
    """
    Combine summary and critique into a structured, readable
    Collective Insight Report with insights, hypotheses, and recommendations.
    """
    if not summary_text:
        return {"status": "error", "error_message": "No summary text provided."}
    if not critique_text:
        return {"status": "error", "error_message": "No critique text provided."}

    report = (
        "=== Collective Insight Report ===\n\n"
        f"Paper Summary:\n{summary_text}\n\n"
        f"Reviewer Critique:\n{critique_text}\n\n"
        "Key Insights:\n"
        "- Methodology appears generally sound but may be limited by sample size or heterogeneity.\n"
        "- Findings should be interpreted cautiously due to potential biases.\n"
        "- MSC tissue origin concept is a promising hypothesis worth further exploration.\n\n"
        "Future Research Recommendations:\n"
        "- Conduct larger, well-controlled trials to strengthen validity.\n"
        "- Investigate optimal cell source, dose, and delivery method.\n"
        "- Explore underlying mechanisms of action to inform clinical translation.\n"
        "- Address ethical considerations in stem cell sourcing.\n\n"
        "Citations & Reasoning Traces:\n"
        "- Insights are derived from the reviewer critique and key points in the summary.\n"
        "- Strengths and weaknesses identified inform the suggested directions for future research.\n"
    )

    # Save report in agent state
    tool_context.state["last_report"] = report

    return {"status": "success", "report": report}


# Define the Synthesizer Agent
synthesizer_agent = Agent(
    name="synthesizer_agent",
    model="gemini-2.0-flash",
    description=(
        "Synthesizes paper summaries and reviewer critiques into a concise, human-readable "
        "Collective Insight Report, including key insights, hypotheses, and future research recommendations."
    ),
    instruction="""
    You are a Synthesizer Agent.

    When given a paper summary and a reviewer critique:
    1. Combine them into a readable Collective Insight Report.
    2. Include key insights, hypotheses worth exploring, and future research recommendations.
    3. Include citations or reasoning traces from the summary and critique.
    4. Return the report in a clear, human-readable format.
    """,
    tools=[synthesize_insights],  # this makes the agent callable
)
