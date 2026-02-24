# 🎓 AI Study Assistant using Google ADK

A Multi-Agent AI Study Assistant built using **Google Agent Development Kit (ADK)** and **Gemini API**.

It helps students:

• 📖 Understand any topic
• ❓ Generate interview questions
• 🗺️ Get a complete learning roadmap


---

# 🤖 Agents Architecture

## Root Agent

study_agent

## Sub Agents

• explanation_agent → Explains topic
• question_agent → Generates interview questions
• roadmap_agent → Generates learning roadmap

---

# 🛠 Tools Used

• Google ADK
• Gemini 2.5 Flash
• Python
• Google Generative AI

---

# 📂 Folder Structure

study_assistant
│
├── study_agent
│   ├── agent.py
│   ├── sub_agents
│
├── tools
│
├── requirements.txt
│
└── README.md

---

# ⚙ Installation & Setup

## Step 1 — Clone repo

git clone https://github.com/TannuAgarwal113322/Study_Assistant_ADK.git

cd study_assistant

## Step 2 — Install dependencies

pip install -r requirements.txt

## Step 3 — Add API key

Create .env file

GOOGLE_API_KEY=your_api_key

## Step 4 — Run project

py -m google.adk.cli web .

---

# 🎯 Features

✅ Multi-Agent System
✅ Explanation Generator
✅ Interview Questions Generator
✅ Learning Roadmap Generator
✅ Gemini AI Integration

---

# 🧠 Example

Input:

Teach me DBMS

Output:

✔ Explanation
✔ Interview Questions
✔ Learning Roadmap

---

# 👩‍💻 Author

Tannu Agarwal
NIT Kurukshetra

---

# 🏆 Built for Google ADK Challenge
