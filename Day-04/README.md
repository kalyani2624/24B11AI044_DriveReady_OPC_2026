# Day 4 — AutoMate AI: Agent Tools and Google Sheets

Day 4 adapts the 26 November class's bakery agent exercise to the AutoMate AI used-car dealership assistant.

## What this task builds

A LangChain agent with three tools connected to a private Google Sheets workbook:

1. `search_inventory` — searches dealership vehicle rows marked `AVAILABLE`.
2. `calculate_vehicle_emi` — calculates an estimated loan EMI using deterministic Python maths.
3. `save_qualified_lead` — validates and appends a customer enquiry to a separate Leads worksheet after explicit consent.

The agent uses `create_agent`, `ChatGroq`, the LangChain `@tool` decorator, and a Pydantic `LeadRecord` schema.

## Run in Google Colab

1. Open `task.py` in Google Colab (or upload it into a notebook).
2. Install packages:

```bash
pip install -U langchain langchain-groq gspread google-auth pydantic
```

3. Add a Colab Secret named `GROQ_API_KEY`, paste your own API key, and enable notebook access.
4. Run the script and approve Google Sheets access.
5. The script opens or creates **AutoMate AI - Dealership CRM** in your signed-in Google account.
6. Add authorised vehicle records to the `Inventory` worksheet using the exact headers below.
7. Test inventory searches, EMI calculations, and consent-based lead saving.

## Inventory worksheet columns

`vehicle_id, make, model, variant, year, asking_price_inr, fuel_type, transmission, odometer_km, location, status, last_verified_at`

Only rows with status `AVAILABLE` are returned. Use real, dealership-authorised records; the project does not generate sample stock.

## Leads worksheet columns

`lead_id, created_at_utc, customer_name, contact, budget_max_inr, preferred_vehicle, fuel_preference, transmission_preference, location, purchase_timeline, notes, consent_confirmed`

The lead tool refuses to save unless `consent_confirmed` is true. The assistant is instructed to request explicit permission first.

## Concepts from the class

- AI vs agent: a model generates; tools perform actions.
- Function calling: the model selects a tool and supplies arguments; the application executes it.
- `@tool`: exposes a documented Python function to the agent.
- Tool design: meaningful names, type hints, clear docstrings, one responsibility, and input validation.
- Agent construction: model + tools + system prompt using `create_agent`.
- Pydantic: validates structured lead information.
- Rate limits: handles HTTP 429 gracefully; each participant should use their own API key.

## Safety and limitations

- The workbook is private to the Google account that authorises it.
- No live dealership data is included. Add and maintain your own Inventory rows.
- No WhatsApp, email, customer messaging, reservation, or payment integration is connected.
- It cannot verify ownership, accident history, insurance, finance eligibility, legal status, or physical vehicle condition.
- EMI is an estimate, not a lender quotation.
- Never upload API keys, customer personal data, or dealership credentials to GitHub.

## OPC submission files

- `task.py` — required Python source.
- `README.md` — task and implementation documentation.
- `test.csv` — manual evaluation prompts.
