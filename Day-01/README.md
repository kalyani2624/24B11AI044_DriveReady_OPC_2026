# Day 1 — AutoMate AI 🚗

**Your Journey. Your Intelligent Co-Pilot.**

Day 1 is the foundational chatbot exercise for AutoMate AI. It uses LangChain to connect a structured automotive-advisor prompt to a Groq-hosted language model and practices secure API-key handling and conversation history. This is a learning exercise, not the final dealership product. The product direction is an AI sales and operations co-pilot for independent used-car dealerships.

## What it can help with

- Car-buying guidance based on a user's budget and needs.
- High-level comparisons between vehicle models.
- Explanations of petrol, diesel, CNG, hybrid, and electric vehicles.
- First-time buyer checklists.
- Basic maintenance and safety-feature explanations.
- Used-car inspection questions.

## Stack

- Python
- LangChain and LangChain Core
- LangChain-Groq (`ChatGroq`)
- Groq API — `openai/gpt-oss-120b`
- Google Colab Secrets

## Run it

1. Open `AutoMate_AI_Day_01.ipynb` in Google Colab.
2. Install the notebook dependencies using the first code cell.
3. Add a Colab Secret named `GROQ_API_KEY`, paste your Groq API key as its value, and enable notebook access.
4. Run all cells in order.
5. Use the interactive chat cell to ask automotive questions.

Create a key at <https://console.groq.com/keys> and check the current model catalogue at <https://console.groq.com/docs/models>.

## Important limitations

This is a learning prototype. It does not query a verified or live database of car prices, variants, availability, mileage, crash-test scores, recalls, or specifications. Verify model-specific details against current manufacturer documents or trusted sources. It is not a substitute for a qualified mechanic or financial advice.

## Example prompts

- `I have a budget of ₹10 lakh. Suggest a practical family car.`
- `Compare Tata Nexon and Hyundai Creta. What should I verify before deciding?`
- `Should I consider an electric car or a petrol car for city use?`
- `I am buying my first used car. Give me an inspection checklist.`
- `Explain ABS, airbags, and ADAS in simple English.`


## OPC submission file

The required Python source file for this task is `task.py`. The Colab notebook is retained as an optional interactive version. Run this task in Google Colab after installing `langchain` and `langchain-groq`, and add `GROQ_API_KEY` in Colab Secrets. The script uses the Colab `userdata` API.
