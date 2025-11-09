# ai_agent/sub_agents/search_agent/agent.py

import arxiv
from google.adk.agents import Agent

def search_stem_cell_papers() -> dict:
    """
    Searches arXiv for 10 recent papers specifically on stem cell therapy.
    Returns metadata + truncated abstracts for manageable processing.
    """
    query = "stem cell therapy"
    print(f"--- Tool: search_stem_cell_papers called ---")

    try:
        search = arxiv.Search(
            query=query,
            max_results=10,  # limit to top 10 papers to reduce token count
            sort_by=arxiv.SortCriterion.Relevance,
        )

        results = []
        for result in search.results():
            results.append({
                "title": result.title,
                "authors": [a.name for a in result.authors],
                "published": str(result.published.date()),
                "url": result.entry_id,
                "abstract": result.summary[:400] + "..."  # truncate abstract to first 400 chars
            })

        return {"status": "success", "results": results}

    except Exception as e:
        return {"status": "error", "error_message": str(e)}


# Define the Search Agent
search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    description="Agent that retrieves recent and relevant research papers on stem cell therapy.",
    instruction="""
    You are a literature search assistant specialized in stem cell therapy.
    When asked to fetch papers:
    1. Use the search_stem_cell_papers tool to retrieve up to 10 relevant research papers.
    2. Return metadata only: title, authors, publication date, URL, and a short abstract (max 400 chars).
    """,
    tools=[search_stem_cell_papers],
)
