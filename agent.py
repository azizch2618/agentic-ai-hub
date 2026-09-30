from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools




load_dotenv()

def build_agent():
    return Agent(
        model=OpenAIResponses(id="gpt-5-mini"),  # cutoff knowledge of gpt-5-mini => June 2024
        tools=[DuckDuckGoTools()],  # websearch
        markdown=True,  # proper formatted output
        instructions="You are a helpful and expert travel agent.",  # travel agent
        add_datetime_to_context=True  # adding current date and time for context
    )

openai_agent = build_agent()

openai_agent.print_response("What is your knowledge cutoff")
