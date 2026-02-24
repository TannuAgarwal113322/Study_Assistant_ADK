import google.generativeai as genai
import os


genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def explain_topic(topic: str) -> str:

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        f"Explain {topic} in detail for a college student with examples"
    )

    return response.text