# 🤖 Agentic AI Hub

> A practical Agentic AI application built with Python, Agno, Groq, and Streamlit.

Agentic AI Hub is an interactive AI application that brings multiple specialized AI agents into a single Streamlit workspace.

The project demonstrates how AI agents can combine LLMs, external tools, structured instructions, memory, and multi-agent workflows to perform practical tasks.

## 🚀 Features

### 🎥 YouTube Video Analyzer

The YouTube Agent analyzes YouTube videos using available video metadata and captions.

It can provide:

- Video overview
- Main topics
- Content structure
- Important sections
- Key learning points
- Practical takeaways
- Tools and technologies mentioned
- Structured Markdown reports

The agent is instructed to avoid inventing unsupported information or timestamps.

### 📈 Finance Research Agent

The Finance Agent performs financial research using external tools.

It can research:

- Stock prices
- Company fundamentals
- Analyst recommendations
- Technical indicators
- Recent financial news
- General financial information

The results are presented in structured Markdown with sections and tables where appropriate.

> ⚠️ This application is intended for financial research and informational purposes only. It does not provide personalized financial advice.

### 👥 Multi-Agent Teams

The project includes an example of multiple specialized agents working together using Agno Teams.

Example architecture:

```text
                    User Request
                         │
                         ▼
                    Agent Team
                   /           \
                  ▼             ▼
          Research Agent   Finance Agent
                  │             │
                  └──────┬──────┘
                         ▼
                  Combined Response
````

### 🧠 Agent Memory

The project demonstrates agent memory using local SQLite storage.

The memory example explores:

- User memories
- Conversation history
- Persistent storage
- Retrieving stored information

### 🖥️ Streamlit Interface

The agents are available through a Streamlit interface.

The application includes:

- Agentic AI Hub home page
- Sidebar navigation
- YouTube Agent
- Finance Agent
- Quick finance research options
- Input validation
- Loading states
- Error handling
- Structured reports
- Responsive layout

## 🧠 Agentic AI Architecture

The core idea of the project is:

```text
             ┌─────────────────┐
             │      USER       │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  STREAMLIT UI   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │      AGENT      │
             └────────┬────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       MODEL        TOOLS    INSTRUCTIONS
          │           │
          │           ├── YFinance
          │           ├── DuckDuckGo
          │           └── YouTube
          │
          └───────────┬───────────┘
                      ▼
             ┌─────────────────┐
             │ AGENT RESPONSE  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  STREAMLIT UI   │
             └─────────────────┘
```

The project demonstrates the basic Agentic AI pattern:

```text
LLM
 +
Instructions
 +
Tools
 +
Task
 =
AI Agent
```

## 🛠️ Technology Stack

| Category                | Technology                        |
| ----------------------- | --------------------------------- |
| Programming Language    | Python                            |
| Agent Framework         | Agno                              |
| LLM Provider            | Groq                              |
| Web Interface           | Streamlit                         |
| Financial Data          | YFinance / Agno YFinanceTools     |
| Web Search              | DuckDuckGo / Agno DuckDuckGoTools |
| YouTube Analysis        | Agno YouTubeTools                 |
| Environment Management  | python-dotenv                     |
| Local Database          | SQLite                            |
| Version Control         | Git                               |
| Repository              | GitHub                            |
| Development Environment | VS Code                           |

## 📁 Project Structure

```text
agentic-ai-hub/
│
├── .env.example
├── .gitignore
│
├── agent.py
├── finance.py
├── memory.py
├── team.py
├── ui.py
└── youtube_analyzer.py
```

### `ui.py`

Main Streamlit application.

Handles:

- Application layout
- Navigation
- Agent selection
- User input
- YouTube URL validation
- Finance quick queries
- Agent execution
- Report display
- Error handling

### `finance.py`

Contains the Finance Research Agent.

The agent combines an LLM with financial data and web-search tools to research financial questions.

### `youtube_analyzer.py`

Contains the YouTube Video Analyzer Agent.

The agent uses YouTube tools to work with available video metadata and captions and generate a structured analysis.

### `team.py`

Demonstrates an Agno multi-agent team with specialized agents working together.

### `memory.py`

Demonstrates agent memory and conversation history using local SQLite storage.

### `agent.py`

Contains a basic Agno agent example demonstrating the fundamental agent structure.

## ⚙️ Installation

### 1. Clone the repository

Clone the repository and enter the project directory:

```bash
git clone https://github.com/azizch2618/agentic-ai-hub.git
cd agentic-ai-hub
```

### 2. Create a virtual environment

For macOS and Linux:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install the main project dependencies:

```bash
pip install -U agno groq streamlit python-dotenv yfinance youtube-transcript-api
```

If your environment reports another missing package required by an Agno tool, install the package reported by the error.

## 🔐 Environment Variables

Create a local `.env` file in the project root.

For Groq:

```env
GROQ_API_KEY=your_groq_api_key_here
```

If you use the OpenAI-based examples included during development:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

A template is included in:

```text
.env.example
```

### Important

Never commit your real `.env` file or API keys to GitHub.

The project's `.gitignore` is configured to exclude environment files and other local development files.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run ui.py
```

Then open the local Streamlit URL shown in your terminal.

The application will open the:

```text
🤖 AGENTIC AI HUB
```

home page.

## 🎥 Using the YouTube Agent

1. Open the **YouTube Agent**.
2. Enter a valid YouTube URL.
3. Click **Analyze Video**.
4. The agent retrieves the available information.
5. The application generates a structured analysis report.

Example request:

```text
Analyze this YouTube video and provide:

1. Video overview
2. Main topics
3. Important sections
4. Key learning points
5. Practical takeaways
6. Tools and technologies mentioned
7. Final summary
```

The analyzer works with information available through the configured YouTube tools and captions.

## 📈 Using the Finance Agent

Open the **Finance Agent** from the application navigation.

You can enter a custom research question or use the built-in quick research options.

Example:

```text
Analyze NVDA:

- Current stock price
- Company fundamentals
- Key technical indicators
- Analyst recommendations
- Recent financial news

Present the results in clear sections and tables.
```

The Finance Agent uses configured financial and web-search tools to gather information and produce a structured research report.

> ⚠️ Financial information is provided for informational and research purposes only and should not be considered personalized financial advice.

## 🧩 Agent Workflows

### Finance Agent Workflow

```text
User Question
     │
     ▼
   Agent
     │
     ├── LLM
     │
     ├── Financial Tools
     │
     └── Web Search Tools
     │
     ▼
  Research
     │
     ▼
Structured Response
```

### YouTube Agent Workflow

```text
YouTube URL
     │
     ▼
YouTube Agent
     │
     ├── Video Metadata
     │
     └── Available Captions
     │
     ▼
Content Analysis
     │
     ▼
Structured Report
```

## 🎯 Learning Objectives

This project was built to gain practical experience with:

- Agentic AI
- AI agents
- LLM integration
- Tool calling
- Agent instructions
- Multi-agent systems
- Agent memory
- Conversation history
- External data sources
- Financial research agents
- YouTube analysis agents
- Streamlit applications
- Environment variables
- Git
- GitHub
- AI application architecture

## 📚 Agentic AI Concepts Covered

The project demonstrates the following concepts:

```text
Introduction to Agentic AI
        ↓
AI Agents
        ↓
Agent Tools
        ↓
Tool Calling
        ↓
Agent Instructions
        ↓
Finance Agent
        ↓
Multi-Agent Teams
        ↓
Agent Memory
        ↓
YouTube Agent
        ↓
Streamlit Deployment
```

## 🔮 Future Improvements

Possible future improvements include:

- Additional specialized agents
- More advanced multi-agent workflows
- Improved agent memory
- Better transcript handling
- More robust error handling
- Automated testing
- Improved observability
- More research tools
- Additional data sources
- Authentication
- Production deployment
- Improved UI/UX
- More structured agent outputs

## 📌 Project Status

Status: Active Development

The current version provides a working Agentic AI workspace containing Finance and YouTube agents, along with examples of multi-agent teams and agent memory.

## 👨‍💻 Author

### Aziz Ullah

AI/ML Developer • Python Developer • Web Developer

This project is part of my practical learning and development journey in Artificial Intelligence, Machine Learning, and Agentic AI.

GitHub: [@azizch2618](https://github.com/azizch2618)

## ⭐ Key Takeaway

Agentic AI Hub demonstrates how an LLM can move beyond simple question answering by combining:

```text
             LLM
              +
           Tools
              +
        Instructions
              +
            Memory
              +
       Multi-Agent Workflows
              │
              ▼
       Practical AI Agents
```

The goal is to understand and build AI systems that can reason through tasks, use tools, work with external information, and produce useful structured results.
