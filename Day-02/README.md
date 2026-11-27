# Day 2 — AutoMate AI: Prompting and Python Foundations

Day 2 applies the concepts from the 24 November class to the automotive assistant. These are foundational prompt-engineering and Python exercises; the product's initial customer segment is independent used-car dealerships.

## Topics covered

1. **System messages:** role, facts, rules, and response format.
2. **Few-shot prompting:** examples guide automotive request classification. This is prompt context, not model training.
3. **JSON output:** extract a vehicle enquiry into consistent key-value fields and validate it with Python's `json.loads()`.
4. **Python dictionaries:** use `.get()` to provide a safe default for a missing key.
5. **Type hints and docstrings:** document expected function inputs, outputs, and purpose.
6. **Decorators:** add function-call logging without changing the wrapped function's core logic.
7. **LangChain `@tool`:** demonstrate converting a Python function into a LangChain tool. This is a tool-definition example, not yet a complete autonomous agent.
8. **Manual conversation memory:** retain at most eight question-and-answer turns.
9. **Exception handling:** use `try/except` to handle invalid input, JSON parsing issues, and API failures gracefully.

## Run in Google Colab

1. Open `AutoMate_AI_Day_02.ipynb` in Google Colab.
2. Add the `GROQ_API_KEY` secret in Colab Secrets and enable notebook access.
3. Run the cells from top to bottom.
4. Complete the Day 2 checklist at the end of the notebook.

## Language

The AutoMate AI system prompt instructs the model to respond only in English. The notebook and documentation are in English.

## Limitations

The chatbot does not access live vehicle listings, prices, specifications, recalls, or dealer inventory. Treat its answers as general guidance and verify current vehicle details with official sources.

## Stack

Python · LangChain · LangChain-Groq · Groq API · Google Colab


## OPC submission file

The required Python source file for this task is `task.py`. The Colab notebook is retained as an optional interactive version. Run this task in Google Colab after installing `langchain` and `langchain-groq`, and add `GROQ_API_KEY` in Colab Secrets. The script uses the Colab `userdata` API.
