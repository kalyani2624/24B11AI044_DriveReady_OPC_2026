# AutoMate AI 🚗

**The AI Sales & Operations Co-Pilot for Independent Used-Car Dealerships**

AutoMate AI is an early-stage product concept for helping small automotive dealerships organise customer enquiries, match buyer requirements to their own inventory, prepare staff-approved replies, and manage follow-ups.

This repository is also the Drive Ready OPC 2026 daily learning submission. Each day contains the required `task.py` and `README.md`; Colab notebooks are retained as optional interactive companions.

## The problem we want to solve

Independent used-car dealerships may manage enquiries, vehicle stock, and customer follow-ups across spreadsheets, calls, messaging apps, and manual notes. AutoMate AI aims to bring these repeated workflows into one assistant while keeping dealership staff in control.

This is a product hypothesis, not a claim that every dealership has the same problem. We will validate it through dealer interviews and a small pilot.

## Initial target customer

Independent used-car dealerships and small pre-owned vehicle businesses in India.

## Initial MVP

The first end-to-end workflow is:

**Customer enquiry → qualification → inventory match → staff-approved reply → lead record → follow-up reminder.**

Planned MVP capabilities:
- Extract buyer requirements such as budget, preferred vehicle type, fuel, transmission, location, and purchase timeline.
- Ask clarifying questions when important information is missing.
- Search a dealership's approved inventory sheet or database.
- Show vehicle matches with source record and last-updated time.
- Draft customer replies for staff approval.
- Log leads and next follow-up dates.
- Summarise pending enquiries for dealership staff.

## What AutoMate AI does not do yet

The current Day 1–3 notebooks are learning prototypes. They are not connected to a live dealership, stock feed, WhatsApp, Telegram, or Google Sheets tool. They cannot verify real availability, prices, ownership, accident history, vehicle condition, or legal status. They do not book, reserve, negotiate, or sell vehicles.

Never treat a model-generated answer as verified inventory data. A future connected version must rely on authorised, current records and show their freshness. Customer-facing messages and consequential changes should require staff approval in the initial MVP.

## Daily learning and implementation

### Day 1 — LLM chatbot foundation

Required source: `Day-01/task.py`  
Optional Colab notebook: `Day-01/AutoMate_AI_Day_01.ipynb`

Practice LangChain model calls, system instructions, secure API-key use, and conversational memory.

### Day 2 — Prompt engineering and Python foundations

Required source: `Day-02/task.py`  
Optional Colab notebook: `Day-02/AutoMate_AI_Day_02.ipynb`

Practice role/facts/rules/format, few-shot prompting, JSON, dictionaries, type hints, decorators, memory, and error handling.

### Day 3 — First basic LangChain agent

Required source: `Day-03/task.py`  
Test data: `Day-03/test.csv`  
Optional Colab notebook: `Day-03/AutoMate_AI_Day_03.ipynb`

Create the first basic agent, understand brain/instructions/tools/memory and the ReAct loop, and test ten dealership-assistant scenarios. This first agent has no external tools yet.

### Day 4 — Dealership agent with tools and Google Sheets

Required source: `Day-04/task.py`  
Test prompts: `Day-04/test.csv`  
Implementation guide: `Day-04/README.md`

- Connect a LangChain agent to a dealership-owned Google Sheets workbook.
- Search available vehicle inventory using `search_inventory`.
- Calculate estimated vehicle-loan EMI with deterministic Python using `calculate_vehicle_emi`.
- Validate customer enquiries with Pydantic and save consented leads using `save_qualified_lead`.
- Handle API rate limits and connection failures.

**Day 4 scope:** Google Sheets inventory lookup and lead logging are included. Customer messaging, vehicle booking, payment, live market data, and vehicle-condition verification are not connected.

## Product documentation

- [Product vision](docs/PRODUCT_VISION.md)
- [Business model](docs/BUSINESS_MODEL.md)
- [System architecture](docs/SYSTEM_ARCHITECTURE.md)
- [Development roadmap](docs/DEVELOPMENT_ROADMAP.md)

## Repository structure

```text
24B11AI084_DriveReady_OPC_2026/
├── Day-01/
│   ├── task.py
│   ├── README.md
│   └── AutoMate_AI_Day_01.ipynb
├── Day-02/
│   ├── task.py
│   ├── README.md
│   └── AutoMate_AI_Day_02.ipynb
├── Day-03/
│   ├── task.py
│   ├── README.md
│   ├── test.csv
│   └── AutoMate_AI_Day_03.ipynb
├── docs/
│   ├── PRODUCT_VISION.md
│   ├── BUSINESS_MODEL.md
│   ├── SYSTEM_ARCHITECTURE.md
│   └── DEVELOPMENT_ROADMAP.md
└── requirements.txt
```

## Run the learning tasks

Run the notebooks in Google Colab or use the `task.py` source files in a compatible environment. The current exercises use:
- Day 1 and Day 2: Groq API via LangChain-Groq; Colab Secret `GROQ_API_KEY`.
- Day 3: Google Gemini or OpenAI; Colab Secret `GOOGLE_API_KEY` or `OPENAI_API_KEY`.

Install the packages listed in `requirements.txt` and any day-specific dependencies. Model identifiers and provider availability can change; check your provider's current model catalogue before running.

## Product principles

1. **Truth over fluency:** never invent vehicle stock, prices, mileage, or condition.
2. **Human approval:** staff approve customer-facing messages and consequential changes.
3. **Traceability:** show the source record and freshness of inventory information.
4. **Least privilege:** connect only to the systems and data required.
5. **Privacy by design:** collect only necessary customer data and define access and retention.
6. **Cost-aware AI:** use ordinary code for calculations, filtering, validation, and scheduled work; use LLMs for language understanding and drafting.
7. **Validate before scaling:** interview dealers and measure a pilot before expanding features.

## Current status

**Stage:** Learning prototypes and product discovery.  
**Live dealership integrations:** None yet.  
**Commercial launch:** Not started.

## Security

Never commit API keys, `.env` files, access tokens, customer personal data, or dealership credentials. Use Colab Secrets or a proper secret manager.
