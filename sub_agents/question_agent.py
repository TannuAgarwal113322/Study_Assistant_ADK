import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from google.adk.agents import Agent
from tools.question_tool import generate_questions

question_agent = Agent(
    name="question_agent",
    model="gemini-2.5-flash",
    tools=[generate_questions],
    instruction="Generate questions"
)