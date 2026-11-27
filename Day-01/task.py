"""AutoMate AI — Day 1 task source code.

This script follows the Drive Ready OPC Day 1 learning task.
It is designed to run in Google Colab; configure the required API key
in Colab Secrets before execution. See README.md in this folder.
"""

# Required package (run in a Colab cell before running this file):
# %pip install -U langchain langchain-groq


import os
from google.colab import userdata

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

api_key = userdata.get("GROQ_API_KEY")
if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found. Add it in Colab Secrets and enable notebook access."
    )

os.environ["GROQ_API_KEY"] = api_key
print("AutoMate AI setup complete. API key loaded securely.")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

print("Groq model configured successfully.")

system_prompt = """
You are AutoMate AI, a helpful and unbiased automotive information assistant.
Your tagline is: Your Journey. Your Intelligent Co-Pilot.
Respond only in English, regardless of the language used by the user. Do not switch to Hindi, Telugu, or any other language.

YOUR ROLE
- Help users think through car-buying decisions using budget, driving needs,
  family size, location, and preferences.
- Explain petrol, diesel, CNG, hybrid, and electric vehicles.
- Compare vehicle models at a high level when asked.
- Explain basic maintenance, safety features, and used-car inspection checks.
- Explain technical terms in simple language.

TRUTHFULNESS AND SAFETY RULES
- Ask a concise follow-up question when essential details are missing.
- Do not invent current prices, on-road costs, variant availability, mileage,
  crash-test ratings, recall status, or exact specifications.
- Say clearly when details may be outdated or need official verification.
- Do not claim to have live access to dealer inventory or manufacturer data.
- Explain trade-offs instead of presenting one vehicle as universally best.
- For used cars, recommend an independent mechanical inspection and document checks.
- Do not replace professional mechanical, legal, or financial advice.

RESPONSE STYLE
- Be friendly, practical, neutral, and concise.
- Use headings or short bullet lists when they improve clarity.
- State assumptions and ask for missing information rather than guessing.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

conversation_chain = prompt | llm | StrOutputParser()
print("AutoMate AI prompt and conversation chain are ready.")

MAX_TURNS = 8
chat_history = []

def chat_with_automate(question: str) -> str:
    """Ask AutoMate AI and retain at most eight question/answer turns."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please enter a non-empty question.")

    answer = conversation_chain.invoke({
        "history": chat_history,
        "question": question.strip(),
    })

    chat_history.append(HumanMessage(content=question.strip()))
    chat_history.append(AIMessage(content=answer))

    # One turn means one user message plus one assistant response.
    del chat_history[:-MAX_TURNS * 2]
    return answer

def reset_chat() -> None:
    """Clear the current session's conversation history."""
    chat_history.clear()
    print("Conversation history cleared.")

print(f"Conversation memory is ready (maximum {MAX_TURNS} turns).")

sample_question = (
    "I have a budget of ₹10 lakh and need a practical family car. "
    "What details should you ask me before recommending options?"
)
print("You:", sample_question)
print("\nAutoMate AI:", chat_with_automate(sample_question))

print("🚗 Welcome to AutoMate AI!")
print("Your Journey. Your Intelligent Co-Pilot.")
print(f"English-first automotive assistant | Memory: last {MAX_TURNS} turns")
print("Type 'exit', 'quit', or 'bye' to stop. Type 'reset' to clear memory.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit", "bye"}:
        print("AutoMate AI: Thanks for chatting. Drive safe!")
        break

    if user_input.lower() == "reset":
        reset_chat()
        continue

    try:
        response = chat_with_automate(user_input)
        print("\nAutoMate AI:", response, "\n")
    except Exception as error:
        print(f"\nAn error occurred: {type(error).__name__}: {error}")
        print("Check your Colab Secret, model access, and Groq API limits.\n")
