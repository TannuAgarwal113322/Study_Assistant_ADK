import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from google.adk.agents import Agent
from tools.roadmap_tool import generate_roadmap

roadmap_agent = Agent(
    name="roadmap_agent",
    model="gemini-2.5-flash",
    tools=[generate_roadmap],
    instruction="Generate roadmap"
)