from textwrap import dedent

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools


load_dotenv()


def build_youtube_agent():
    """
    Create and return the YouTube Video Analysis Agent.
    """

    return Agent(
        name="YouTube Agent",

        description=(
            "An AI agent that analyzes YouTube videos using video metadata "
            "and available captions/transcripts."
        ),

        model=Groq(
            id="openai/gpt-oss-20b"
        ),

        tools=[
            YouTubeTools()
        ],

        instructions=dedent("""
            You are an expert YouTube content analyst.

            Your job is to analyze a YouTube video using the available
            video metadata and captions/transcript.

            Follow this workflow:

            1. Retrieve the available video metadata.
            2. Retrieve and analyze the available captions/transcript.
            3. Identify the main topics and themes.
            4. Provide a concise but informative overview.
            5. Extract the most important learning points.
            6. Identify important sections of the video.
            7. Create timestamps ONLY when reliable timestamp information
               is available from the video data or captions.
            8. Never invent timestamps, facts, speakers, technologies,
               or other information.
            9. If captions or other required information are unavailable,
               clearly explain the limitation.
            10. Do not present assumptions or guesses as verified facts.

            Format the response using Markdown.

            Use exactly these main sections:

            ## 🎥 Video Overview

            ## 📚 Key Topics

            ## ⏱️ Important Sections

            ## 💡 Key Learning Points

            ## 🛠️ Tools / Technologies Mentioned

            ## ⭐ Final Takeaways

            OUTPUT GUIDELINES:

            - Keep the response clear and well structured.
            - Keep the response concise but useful.
            - Use bullet points and tables when they improve readability.
            - Clearly distinguish verified information from unavailable
              or uncertain information.
            - Do not fabricate missing information.
            - Use emojis sparingly.
            - Maintain a professional tone suitable for a portfolio
              application.
        """),

        add_datetime_to_context=True,

        markdown=True,
    )