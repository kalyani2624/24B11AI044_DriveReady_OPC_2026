"""AutoMate AI — Day 3 task source code.

This script follows the Drive Ready OPC Day 3 learning task.
It is designed to run in Google Colab; configure the required API key
in Colab Secrets before execution. See README.md in this folder.
"""

# Required packages (run in a Colab cell before running this file):
# %pip install -U langchain langchain-openai langchain-google-genai pandas

from IPython.display import display


import os
import csv
import getpass
from pathlib import Path
from typing import Any

import pandas as pd
from google.colab import userdata, files
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage

# Choose: "google" or "openai"
MODEL_PROVIDER = "google"

# Provider model IDs; change these if your account/catalogue requires another model.
GEMINI_MODEL = "gemini-3.8-flash"
OPENAI_MODEL = "gpt-6.2-sol"

if MODEL_PROVIDER == "google":
    api_key = userdata.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Add GOOGLE_API_KEY in Colab Secrets and enable notebook access.")
    os.environ["GOOGLE_API_KEY"] = api_key
    from langchain_google_genai import ChatGoogleGenerativeAI
    model = ChatGoogleGenerativeAI(model=GEMINI_MODEL, temperature=0.3)

elif MODEL_PROVIDER == "openai":
    api_key = userdata.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Add OPENAI_API_KEY in Colab Secrets and enable notebook access.")
    os.environ["OPENAI_API_KEY"] = api_key
    from langchain_openai import ChatOpenAI
    model = ChatOpenAI(model=OPENAI_MODEL)

else:
    raise ValueError("MODEL_PROVIDER must be 'google' or 'openai'.")

print(f"Provider configured: {MODEL_PROVIDER}")

AUTOMATE_SYSTEM = """
You are AutoMate AI, an English-only AI sales and operations assistant for independent used-car dealerships.

GOAL
Help dealership staff understand customer enquiries, qualify buyer requirements, draft helpful responses, and think through lead-management workflows.

ROLE
You assist dealership owners, sales executives, and inventory coordinators. You do not replace their judgement or approval.

FACTS AND CURRENT LIMITATIONS
- This Day 3 learning agent has no external tools connected.
- You cannot access a dealership's live inventory, Google Sheets, CRM, messaging apps, or dealer systems.
- You cannot verify that a vehicle is available, reserve a vehicle, change stock, contact a buyer, or update a lead.
- You have no verified dealership-specific prices, vehicle details, policies, or customer records unless they are explicitly provided in the current conversation.

RULES
- Never invent stock availability, asking price, vehicle condition, mileage, ownership, accident history, service history, loan approval, or legal status.
- When asked about a specific vehicle in stock, explain that the live dealership inventory is not connected and ask staff to verify the approved inventory record.
- For customer enquiries, identify useful fields such as budget, preferred make/model, body type, fuel, transmission, location, purchase timeline, and contact preference.
- Ask concise follow-up questions when required details are missing.
- You may draft a customer reply or follow-up message, but clearly label it as a draft. Never claim that you sent it.
- You may explain how a lead or stock update should be recorded, but never claim that you changed an external record.
- Do not ask for passwords, OTPs, payment credentials, or unnecessary identity documents.
- Keep customer information private and recommend collecting only details needed for the enquiry.
- Be neutral and do not pressure buyers into a purchase.

FORMAT
- Respond only in English.
- Be professional, concise, and practical.
- Separate confirmed information from assumptions and items needing verification.
- Use clear headings or short bullet lists when useful.
"""

print("AutoMate AI instructions are ready.")

agent = create_agent(
    model=model,
    tools=[],
    system_prompt=AUTOMATE_SYSTEM,
)

print("AutoMate AI basic agent created.")

first_result = agent.invoke({
    "messages": [
        {"role": "user", "content": "I am a first-time car buyer. What information do you need before recommending a car?"}
    ]
})

first_answer = first_result["messages"][-1].content
print(first_answer)

MAX_TURNS = 8
conversation_history = []

def ask_automate(question: str) -> str:
    """Ask AutoMate AI and retain up to eight recent question/answer turns."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please enter a non-empty question.")

    messages = conversation_history + [HumanMessage(content=question.strip())]
    result = agent.invoke({"messages": messages})
    answer = result["messages"][-1].content

    conversation_history.append(HumanMessage(content=question.strip()))
    conversation_history.append(AIMessage(content=answer))
    del conversation_history[:-MAX_TURNS * 2]
    return answer

def reset_memory() -> None:
    """Clear AutoMate AI's current-session conversation history."""
    conversation_history.clear()
    print("Conversation memory cleared.")

print(ask_automate("My name is Rohit and my budget is ₹10 lakh."))
print("\nStored messages:", len(conversation_history))
print(ask_automate("What is my name and budget?"))

uploaded = files.upload()

if not uploaded:
    raise ValueError("Please upload the Day-03 test.csv file.")

csv_name = next(iter(uploaded))
test_df = pd.read_csv(csv_name)

required_columns = {"question", "expected_groups"}
if not required_columns.issubset(test_df.columns):
    raise ValueError("CSV must contain question and expected_groups columns.")

print(f"Loaded {len(test_df)} test cases from {csv_name}.")
display(test_df)

def evaluate_answer(answer: str, expected_groups: str) -> tuple[bool, str]:
    """Check that at least one alternative in each semicolon-separated group appears."""
    answer_lower = str(answer).lower()
    checks = []
    for group in str(expected_groups).split(";"):
        alternatives = [term.strip().lower() for term in group.split("|") if term.strip()]
        checks.append(any(term in answer_lower for term in alternatives))
    passed = all(checks) if checks else False
    return passed, f"{sum(checks)}/{len(checks)} groups matched"

test_results = []
for index, row in test_df.iterrows():
    question = str(row["question"])
    expected = str(row["expected_groups"])
    try:
        result = agent.invoke({"messages": [{"role": "user", "content": question}]})
        answer = result["messages"][-1].content
        passed, note = evaluate_answer(answer, expected)
        status = "PASS" if passed else "REVIEW"
        error = ""
    except Exception as exc:
        answer = ""
        status = "ERROR"
        note = "Agent call failed"
        error = f"{type(exc).__name__}: {exc}"

    test_results.append({
        "case": index + 1,
        "question": question,
        "status": status,
        "check": note,
        "answer": answer,
        "error": error,
    })

results_df = pd.DataFrame(test_results)
display(results_df[["case", "status", "check", "question"]])
print("PASS:", int((results_df["status"] == "PASS").sum()))
print("REVIEW:", int((results_df["status"] == "REVIEW").sum()))
print("ERROR:", int((results_df["status"] == "ERROR").sum()))

for _, row in results_df.iterrows():
    print("=" * 90)
    print(f"Case {row['case']} — {row['status']}")
    print("Question:", row["question"])
    print("Answer:", row["answer"])
    if row["error"]:
        print("Error:", row["error"])

print("🚗 AutoMate AI — Day 3 Basic Agent")
print("English-only automotive assistant. No external tools connected yet.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit", "bye"}:
        print("AutoMate AI: Thanks for chatting. Drive safe!")
        break
    if user_input.lower() == "reset":
        reset_memory()
        continue
    try:
        print("\nAutoMate AI:", ask_automate(user_input), "\n")
    except Exception as exc:
        print(f"Agent error: {type(exc).__name__}: {exc}")
        print("Check your provider API key, model access, connection, and quota.")
