# ai_agent/tools/tools.py
import requests
from PyPDF2 import PdfReader
from io import BytesIO

def pdf_reader(pdf_url: str) -> str:
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        with BytesIO(response.content) as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def analyze_papers(papers: list) -> dict:
    """
    Analyze a list of paper metadata (title, summary, url).
    Summarize each paper and return results.
    """
    results = []
    for paper in papers:
        title = paper.get("title")
        summary = paper.get("summary")
        url = paper.get("url")

        results.append({
            "title": title,
            "summary": summary,
            "url": url,
        })

    return {"status": "success", "results": results}
