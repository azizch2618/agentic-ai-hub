from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint


load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(
            id="qwen/qwen3.8-27b",
            max_tokens=800
        ),
        markdown=True,  # proper formatted output
        add_history_to_context=True,
        update_memory_on_run=True
    )

agent = build_agent()

user_id= "test@gmail.com"
agent.print_response("Hi, Im AZIZ & im a AI ENGINEER", user_id=user_id)
agent.print_response("Who am i?", user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)
print("MEMORIES:")
pprint(memories)
