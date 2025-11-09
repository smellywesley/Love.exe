# ai_agent/sub_agents/researcher_agent/agent.py
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from PyPDF2 import PdfReader
import os

def summarize_content(content: str, tool_context: ToolContext) -> dict:
    """
    Summarize and analyze provided content (plain text or PDF file path) into a structured format:
    - Key points / highlights
    - Important findings
    - Notable methodologies
    - Applications
    """
    # --- If content is a PDF file path, extract text ---
    if os.path.isfile(content) and content.lower().endswith(".pdf"):
        reader = PdfReader(content)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    else:
        text = content

    if not text.strip():
        return {"status": "error", "error_message": "No content to summarize."}

    # --- Summarization logic ---
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    key_points = lines[:10]  # top 10 sentences
    summary_text = " ".join(key_points)

    structured_summary = {
        "summary_text": summary_text,
        "key_points": key_points,
        "important_findings": key_points[:5],  # first 5 as findings
        "methodologies": [lp for lp in lines if "method" in lp.lower() or "protocol" in lp.lower()],
        "applications": [lp for lp in lines if "therapy" in lp.lower() or "clinical" in lp.lower()],
    }

    # Store in agent state
    if tool_context:
        tool_context.state["last_summary"] = structured_summary

    return {"status": "success", "summary": structured_summary}

# --- Create the Researcher Agent ---
researcher_agent = Agent(
    name="researcher_agent",
    model="gemini-2.0-flash",
    description=(
        "Reads and summarizes PDFs or search result text, extracting key points, "
        "important findings, methodologies, and applications."
    ),
    instruction="""
    You are the Researcher Agent.
    1. Receive content from Manager Agent (either PDF file path or plain text).
    2. Extract text if PDF, then summarize key points clearly.
    3. Highlight important findings, methodologies, and applications.
    4. Return structured summary suitable for Reviewer and Synthesizer Agents.
    """,
    tools=[summarize_content],
)
