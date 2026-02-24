import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from google.adk.agents import Agent
from tools.explain_tool import explain_topic

explanation_agent = Agent(
    name="explanation_agent",
    model="gemini-2.5-flash",
    tools=[explain_topic],
    instruction="Explain study topics"
)