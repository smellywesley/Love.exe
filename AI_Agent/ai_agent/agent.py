# ai_agent/agent.py
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

# Import sub-agents
from .sub_agents.search_agent.agent import search_agent
from .sub_agents.researcher_agent.agent import researcher_agent
from .sub_agents.reviewer_agent.agent import reviewer_agent
from .sub_agents.synthesizer_agent.agent import synthesizer_agent

# Workflow tool: handles PDFs or search-selected content
def analyze_content_workflow(content: str, tool_context: ToolContext) -> dict:
    """
    Handles content from PDF uploads or search results.
    Workflow:
    1. Researcher → 2. Reviewer → 3. Synthesizer → final report
    """
    if not content:
        return {"status": "error", "error_message": "No content provided."}

    # 1️⃣ Researcher: summarize and extract key points
    researcher_response = researcher_agent.tools[0](content, tool_context)
    if researcher_response.get("status") != "success":
        return researcher_response
    summary = researcher_response["summary"]
    tool_context.state["summary"] = summary

    # 2️⃣ Reviewer: critique the summary
    reviewer_response = reviewer_agent.tools[0](summary, tool_context)
    if reviewer_response.get("status") != "success":
        return reviewer_response
    critique = reviewer_response["critique"]
    tool_context.state["critique"] = critique

    # 3️⃣ Synthesizer: generate final Collective Insight Report
    synthesizer_response = synthesizer_agent.tools[0](summary, critique, tool_context)
    if synthesizer_response.get("status") != "success":
        return synthesizer_response

    # 4️⃣ Return final report
    return {"status": "success", "report": synthesizer_response["report"]}

# Root/manager agent
root_agent = Agent(
    name="stemcell_manager",
    model="gemini-2.0-flash",
    description="Manager agent for stem cell therapy research, coordinating sub-agents.",
    instruction="""
    Workflow:
    1. If user provides a PDF, pass file path directly to Researcher Agent.
    2. If user requests a literature search, provide chosen paper's content to Researcher.
    3. Researcher summarizes content and extracts key points.
    4. Reviewer critiques the summary.
    5. Synthesizer generates final Collective Insight Report with insights, hypotheses, and future recommendations.
    6. Return concise, human-readable report to the user.
    """,
    sub_agents=[
        search_agent,
        researcher_agent,
        reviewer_agent,
        synthesizer_agent
    ],
    tools=[analyze_content_workflow],
)
