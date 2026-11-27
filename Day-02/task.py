"""AutoMate AI — Day 2 task source code.

This script follows the Drive Ready OPC Day 2 learning task.
It is designed to run in Google Colab; configure the required API key
in Colab Secrets before execution. See README.md in this folder.
"""

# Required package (run in a Colab cell before running this file):
# %pip install -U langchain langchain-groq


import os
import json
from functools import wraps
from typing import Any, Callable

from google.colab import userdata
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool

api_key = userdata.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("Please add GROQ_API_KEY in Google Colab Secrets and enable notebook access.")

os.environ["GROQ_API_KEY"] = api_key
print("AutoMate AI Day 2 environment is ready.")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

print("Model configured.")

AUTOMATE_SYSTEM = """
ROLE
You are AutoMate AI, an unbiased automotive information assistant.
Respond only in English, regardless of the language used by the user. Do not switch to Hindi, Telugu, or any other language.

FACTS
- This prototype has no live vehicle catalogue, dealer inventory, or price feed.
- The assistant can explain general automotive concepts and help structure decisions.
- Model-specific price, variant, mileage, safety rating, recall, and availability details
  must be verified against current official sources.

RULES
- Never invent current prices, specifications, mileage, crash-test results, or availability.
- Ask for the user's budget and driving needs when they are essential to a recommendation.
- Separate general guidance from facts that need verification.
- For a used vehicle, recommend document checks and an independent mechanical inspection.
- Do not claim to have searched live listings or contacted a dealer.
- Do not present the assistant's response as professional mechanical or financial advice.

FORMAT
- Be polite, concise, practical, and easy to understand.
- Use short headings or bullet points when useful.
- State uncertainty clearly instead of guessing.
"""

print("System instructions defined.")

intent_examples = [
    {"input": "Suggest a reliable family car for my budget.", "output": "recommendation"},
    {"input": "Compare two SUVs for city driving.", "output": "comparison"},
    {"input": "Why does my car battery keep losing charge?", "output": "maintenance"},
    {"input": "What is the purpose of ABS?", "output": "safety"},
    {"input": "I want to sell my old car.", "output": "other"},
]

few_shot_prompt = ChatPromptTemplate.from_messages([
    ("system", "Classify the user's automotive request. Return only one label: recommendation, comparison, maintenance, safety, or other."),
    ("human", "Examples:\n" + "\n".join(f"Request: {x['input']} -> {x['output']}" for x in intent_examples) + "\n\nClassify this request: {question}"),
])

intent_chain = few_shot_prompt | llm | StrOutputParser()

def classify_request(question: str) -> str:
    """Classify an automotive request using the few-shot examples."""
    return intent_chain.invoke({"question": question}).strip().lower()

print(classify_request("Can you compare petrol and hybrid cars for city use?"))

json_prompt = ChatPromptTemplate.from_messages([
    ("system", """
Extract the user's car enquiry as valid JSON only. Do not include Markdown fences or extra text.
Use exactly these keys:
{{
  "intent": "recommendation | comparison | maintenance | safety | other",
  "budget_inr": number or null,
  "vehicle_type": string or null,
  "fuel_preference": string or null,
  "use_case": string or null,
  "missing_information": [string]
}}
Use null when information is not provided. Do not invent values.
"""),
    ("human", "Enquiry: {question}"),
])

json_chain = json_prompt | llm | StrOutputParser()

def extract_enquiry(question: str) -> dict[str, Any]:
    """Return a validated Python dictionary extracted from a car enquiry."""
    raw_output = json_chain.invoke({"question": question})
    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError as error:
        raise ValueError("The model did not return valid JSON. Please try again.") from error

    required_keys = {
        "intent", "budget_inr", "vehicle_type",
        "fuel_preference", "use_case", "missing_information"
    }
    if not isinstance(data, dict) or set(data.keys()) != required_keys:
        raise ValueError("The JSON response does not match the expected structure.")
    return data

enquiry = extract_enquiry("I have ₹9 lakh and need a small petrol car for daily city travel.")
print(json.dumps(enquiry, indent=2, ensure_ascii=False))

vehicle_notes = {
    "hatchback": "Often compact and convenient for city use.",
    "suv": "Often offers a higher seating position; compare size and running costs.",
    "sedan": "Often offers a separate boot and a lower seating position.",
}

vehicle_type = "donut"
description = vehicle_notes.get(vehicle_type, "No note available for this vehicle type.")
print(description)

def estimate_total(price_per_unit: float, quantity: int = 1) -> float:
    """Calculate a simple total from a supplied unit price and quantity.

    This is a generic arithmetic example, not a live vehicle quotation.
    """
    if price_per_unit < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")
    return price_per_unit * quantity

print(estimate_total(1500.0, 3))
print(estimate_total.__doc__)

def log_call(function: Callable) -> Callable:
    """Log a function call while preserving its original return value."""
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"{function.__name__} completed")
        return result
    return wrapper

@log_call
def get_vehicle_note(vehicle_type: str) -> str:
    """Get a general note for a vehicle body type."""
    return vehicle_notes.get(vehicle_type.lower(), "No note available.")

print(get_vehicle_note("suv"))

@tool
def get_vehicle_category_guide(vehicle_type: str) -> str:
    """Return a general, non-commercial explanation of a vehicle body category."""
    return vehicle_notes.get(
        vehicle_type.lower(),
        "No category guide is available for that vehicle type."
    )

print("Tool name:", get_vehicle_category_guide.name)
print("Tool description:", get_vehicle_category_guide.description)
print("Tool result:", get_vehicle_category_guide.invoke({"vehicle_type": "hatchback"}))

MAX_TURNS = 8
chat_history = []

memory_prompt = ChatPromptTemplate.from_messages([
    ("system", AUTOMATE_SYSTEM),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])
memory_chain = memory_prompt | llm | StrOutputParser()

def ask_automate(question: str) -> str:
    """Ask AutoMate AI and retain no more than eight conversation turns."""
    if not question.strip():
        raise ValueError("Question cannot be empty.")

    answer = memory_chain.invoke({"history": chat_history, "question": question})
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=answer))
    del chat_history[:-MAX_TURNS * 2]
    return answer

def clear_memory() -> None:
    """Clear all stored conversation messages for this notebook session."""
    chat_history.clear()
    print("Memory cleared.")

print(ask_automate("I mostly drive in the city and my budget is ₹9 lakh."))
print("Stored messages:", len(chat_history))

def safe_ask(question: str) -> str:
    """Call AutoMate AI and return a user-friendly message on failure."""
    try:
        return ask_automate(question)
    except ValueError as error:
        return f"Input issue: {error}"
    except Exception as error:
        print(f"Technical detail: {type(error).__name__}: {error}")
        return "AutoMate AI could not complete that request. Check the API key, model availability, connection, and API limits, then try again."

print(safe_ask("What should I check before buying a used car?"))

print("🚗 AutoMate AI — Day 2")
print("English-first automotive assistant")
print(f"Conversation memory: last {MAX_TURNS} turns")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit", "bye"}:
        print("AutoMate AI: Thanks for chatting. Drive safe!")
        break

    if user_input.lower() == "reset":
        clear_memory()
        continue

    response = safe_ask(user_input)
    print("\nAutoMate AI:", response, "\n")
