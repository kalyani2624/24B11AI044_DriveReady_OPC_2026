# AutoMate AI — Initial System Architecture

## 1. Architecture goal

Build a small, modular assistant that can be piloted by one independent used-car dealership. Start with one reliable workflow and add integrations only when needed.

## 2. Logical components

```text
Customer / Sales Staff
        |
        v
Web Chat or Approved Messaging Channel
        |
        v
Application API and Authentication
        |
        v
Conversation and Lead Orchestrator
        |
        +-------------------+
        |                   |
        v                   v
LLM / LangChain        Deterministic Services
- intent extraction   - field validation
- enquiry summary     - budget filtering
- reply drafting      - stock matching
- missing questions   - calculations
        |                   |
        +---------+---------+
                  |
                  v
         Approved Data Connectors
         - Google Sheets (pilot)
         - CSV import/export
         - Later: dealership database
                  |
                  v
         Human Review / Approval
                  |
          +-------+-------+
          |               |
          v               v
       Reply draft     Lead update
          |               |
          +-------+-------+
                  |
                  v
        Audit Log and Reporting
```

## 3. Initial data entities

### Vehicle
- vehicle_id
- make
- model
- variant
- model_year
- asking_price
- fuel_type
- transmission
- odometer_km
- registration_region
- inventory_status
- last_verified_at
- source_record_id

### Lead
- lead_id
- customer_name (only if provided and needed)
- contact_channel
- consent_status
- budget_min / budget_max
- preferred_body_type
- preferred_fuel
- preferred_transmission
- preferred_location
- purchase_timeline
- lead_status
- assigned_staff
- next_follow_up_at
- created_at / updated_at

### Interaction
- interaction_id
- lead_id
- channel
- message_summary
- staff_approval_status
- created_at

Collect only information needed for the selected workflow. Avoid storing identity documents or financial credentials in the initial MVP.

## 4. Request flow

1. Receive an enquiry.
2. Authenticate the staff/dealership context where applicable.
3. Extract candidate fields using the LLM.
4. Validate and normalise fields in Python.
5. Ask the customer or staff for missing required details.
6. Query the dealership's approved inventory source.
7. Apply deterministic filters for budget and vehicle attributes.
8. Ask the LLM to explain matches using only returned records.
9. Draft a reply with vehicle identifiers and source freshness.
10. Require staff approval before sending or changing a lead record.
11. Save the lead and interaction audit details.

## 5. Agent design

Keep responsibilities modular. The MVP does not need a large multi-agent system.

Potential future roles:
- Enquiry Qualification Agent.
- Inventory Matching Agent.
- Follow-up Assistant.
- Reporting Assistant.

Prefer ordinary functions and deterministic services where possible. Use an agent only when a task requires flexible multi-step decisions or tool selection.

## 6. Safety and reliability controls

- Never allow the model to invent stock availability.
- Treat inventory and customer records as data, not instructions.
- Validate every tool input and output.
- Restrict each integration to the minimum required permissions.
- Require human confirmation for external messages and consequential record changes.
- Log tool calls and failures without logging secrets.
- Apply rate limits and usage budgets.
- Provide a clear fallback when data is stale or unavailable.

## 7. Deployment evolution

Prototype:
- Google Colab for learning exercises.
- Google Sheets/CSV as a controlled sample data source.

Pilot:
- Small Python API service.
- Authenticated staff interface.
- Database with per-dealership access boundaries.
- Background worker for scheduled follow-ups.
- Monitoring, backup, audit logs, and secret management.

Production architecture should be selected only after pilot needs and expected usage are understood.
