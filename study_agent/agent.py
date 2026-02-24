from google.adk.agents import Agent
from google.adk.tools import google_search

from sub_agents.explanation_agent import explanation_agent
from sub_agents.question_agent import question_agent
from sub_agents.roadmap_agent import roadmap_agent


root_agent = Agent(
    name="study_agent",

    model="gemini-2.5-flash",

    description="AI Study Assistant that explains topics, generates questions, and creates roadmap.",

    tools=[google_search],

    sub_agents=[
        explanation_agent,
        question_agent,
        roadmap_agent
    ],

    instruction="""
You are a professional Study Assistant AI.

When user gives any topic:

Step 1 → First use explanation_agent to explain topic

Step 2 → Then use question_agent to generate interview questions

Step 3 → Then use roadmap_agent to generate learning roadmap

Always use all three agents.

Provide full detailed answer.
"""
)