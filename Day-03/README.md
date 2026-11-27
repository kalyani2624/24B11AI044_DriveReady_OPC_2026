# Day 3 — AutoMate AI: First Basic Dealership Assistant Agent

Day 3 turns the Day 1–2 chatbot foundation into a basic LangChain agent and aligns its instructions with the product direction: an AI sales and operations assistant for independent used-car dealerships.

This follows the class demonstration using `create_agent` with a model and system prompt, but **no external tools connected yet**. Google Sheets, Telegram, inventory lookup, and messaging integrations are later development steps.

## Day 3 learning topics

- Difference between a chatbot and a goal-oriented agent.
- Four parts of an agent: brain (LLM), instructions, tools, and memory.
- ReAct loop: reason, act, observe, and repeat.
- LangChain's `create_agent` structure.
- Switching between Google Gemini and OpenAI.
- Conversation history capped at eight question-and-answer turns.
- Ten test scenarios with expected keyword groups.
- Reviewing failures, improving instructions, and rerunning all tests.

## AutoMate AI dealership scenario

The agent helps dealership staff understand customer enquiries, collect buyer requirements, prepare draft replies, and think through lead-management workflows.

It does **not** access live inventory, Google Sheets, CRM, or messaging services in this exercise. It cannot confirm availability, change stock, contact buyers, or send messages. It must clearly state when dealership records need staff verification.

## Run in Google Colab

1. Open `AutoMate_AI_Day_03.ipynb` in Google Colab, or run `task.py` in a compatible Colab environment.
2. Choose `MODEL_PROVIDER = "google"` or `"openai"`.
3. Add the matching API key in Colab Secrets:
   - Google: `GOOGLE_API_KEY`
   - OpenAI: `OPENAI_API_KEY`
4. Install the Day 3 packages: `langchain`, `langchain-openai`, `langchain-google-genai`, and `pandas`.
5. Download `test.csv` from this folder and upload it when the notebook requests it.
6. Run all ten scenarios, read the full answers, and review failures manually.

Model IDs and provider access can change. Confirm an available model in the provider's current catalogue before running.

## Evaluation

The CSV uses expected keyword groups as a first-pass screen. A keyword match does not prove that a response is correct. Manually review each answer for factual accuracy, clarity, privacy, and appropriate refusal to claim external access.

## OPC submission files

- `task.py` — required Python source file.
- `README.md` — task and implementation documentation.
- `test.csv` — ten dealership-assistant evaluation scenarios.
- `AutoMate_AI_Day_03.ipynb` — optional interactive Colab notebook.

## Stack

Python · LangChain `create_agent` · Google Gemini or OpenAI · Google Colab
