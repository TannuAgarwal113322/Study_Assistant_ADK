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

```
Study_Assistant_ADK
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
```

---

# ⚙ Installation & Setup

## Step 1 — Clone Repository

```bash
git clone https://github.com/TannuAgarwal113322/Study_Assistant_ADK.git

cd Study_Assistant_ADK
```

---

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Add API Key

Create `.env` file inside study_agent folder and add:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Step 4 — Run the Agent

```bash
py -m google.adk.cli web .
```

---

## Step 5 — Open in Browser

Open:

```
http://127.0.0.1:8000
```

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

# 🧠 Approach & Architecture

This project implements a Multi-Agent Study Assistant using Google ADK and Gemini API. The system consists of a root agent called study_agent and three specialized sub-agents: explanation_agent, question_agent, and roadmap_agent. The root agent coordinates all tasks and ensures each sub-agent performs its role sequentially. The explanation_agent explains the topic, the question_agent generates interview questions, and the roadmap_agent creates a learning roadmap. Custom tools are used for structured output generation. The built-in Google search tool enhances responses with relevant information. This modular architecture improves scalability, maintainability, and performance, providing students with a complete and structured learning experience.

---

# 👩‍💻 Author

Tannu Agarwal  
NIT Kurukshetra  

---

# 🏆 Built for Google ADK Challenge
