# Love.exe
 “Mini Research Lab” tackles this problem by creating an ecosystem of research-oriented agents  that can search for papers, critique the findings and synthesize accurate insights to a profound summary. This  is designed for researchers and personnels within academia who needs rapid and structured understanding of  scientific literature.  

 🚀 Project Overview

The goal of StemCell-MultiAgent is to demonstrate how autonomous AI agents can:
1. Retrieve scientific literature,
2. Read and summarize biomedical texts,
3. Critically evaluate methodology and biases,
4. Synthesize collective insights with reasoning traces and recommendations.
5. Each agent performs a specialized role, and all are orchestrated by a central Manager Agent that ensures coherent workflow and structured output.

User → Manager Agent
       ├── Search Agent → Retrieves papers from arXiv
       ├── Researcher Agent → Summarizes content (PDFs or abstracts)
       ├── Reviewer Agent → Provides structured critique
       └── Synthesizer Agent → Generates final “Collective Insight Report”

Sequential Workflow:
Search → Research → Review → Synthesis
Each agent passes intermediate reasoning states via ToolContext.

Collective Insight Report:
Synthesizer Agent integrates research summaries and reviewer critiques into a concise, human-readable report containing:
Key insights
Hypotheses worth exploring
Future research recommendations
Reasoning traces and citations

🧪 Example Use Case

Input:
“Analyze the paper Stem Cell Therapy for Alzheimer’s Disease and generate insights.”

Workflow:
Search Agent retrieves the paper metadata.
Researcher Agent summarizes the paper.
Reviewer Agent critiques it.
Synthesizer Agent outputs a structured report with insights and future research directions.

Output:
A concise “Collective Insight Report” highlighting:

Study methodology
Limitations and biases
Key findings
Hypotheses and next research steps

🛠️ Installation
# Clone the repository
git clone https://github.com/<your-username>/StemCell-MultiAgent.git
cd StemCell-MultiAgent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

Environment Setup

Create a .env file inside ai_agent/ and include:
GOOGLE_API_KEY=your_gemini_api_key_here

▶️ Running the Project
adk run

📄 Output Example
=== Collective Insight Report ===

Paper Summary:
Explores MSC and hPSC-based stem cell therapies for neurodegenerative diseases...

Reviewer Critique:
Strengths: Relevant topic, clear methodology.
Weaknesses: Limited clinical validation, small sample size.

Key Insights:
- MSC tissue origin concept may influence therapeutic outcomes.
- Ethical and translational challenges remain critical barriers.

Future Recommendations:
- Larger randomized studies.
- Exploration of delivery mechanisms and long-term safety.

Citations & Reasoning:
Derived from combined Researcher and Reviewer outputs.

📊 Project Structure
ai_agent/
│
├── agent.py                        # Root Manager Agent
├── sub_agents/
│   ├── search_agent/agent.py       # Literature retrieval
│   ├── researcher_agent/agent.py   # Summarization and key findings
│   ├── reviewer_agent/agent.py     # Critique generation
│   └── synthesizer_agent/agent.py  # Insight synthesis
│
├── .env                            # API keys
├── requirements.txt
└── README.md

