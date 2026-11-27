# AutoMate AI — Development Roadmap

This roadmap is a proposed product plan. It is separate from the mentor's daily curriculum and may be adjusted as the classes progress.

## Phase 0 — Learning foundation (Days 1–3)

- [x] Day 1: basic LLM chatbot with LangChain and Groq.
- [x] Day 2: prompting, JSON, manual memory, Python functions, decorators, and exception handling.
- [x] Day 3: first basic LangChain agent and ten-case evaluation file.
- [ ] Execute all notebooks and source files in Colab with working API credentials.
- [ ] Review and record actual Day 3 test outcomes.

## Phase 1 — Discovery and workflow definition

- Interview 5–10 independent used-car dealers.
- Map their enquiry, inventory, and follow-up workflows.
- Identify the most painful repeated task.
- Define required data fields and approval boundaries.
- Obtain permission before using any real dealership data.

Deliverable: validated workflow and sample data schema.

## Phase 2 — Inventory and lead foundation

- Create a controlled vehicle inventory template.
- Import CSV data and connect a Google Sheet.
- Validate records and stale timestamps.
- Create a lead schema and basic lead logging.
- Implement deterministic vehicle filtering.

Deliverable: reliable inventory lookup and lead storage without autonomous customer messaging.

## Phase 3 — Enquiry qualification assistant

- Extract budget, body style, fuel, transmission, location, and purchase timeline.
- Ask for missing information.
- Summarise enquiries for sales staff.
- Match enquiries against actual inventory.
- Show source records and data freshness.
- Require staff approval of replies.

Deliverable: end-to-end enquiry qualification workflow.

## Phase 4 — Messaging and follow-up

- Start with one approved channel (Telegram for a low-cost prototype).
- Add consent-aware customer communication.
- Draft follow-up messages.
- Track next follow-up dates and outcomes.
- Add retries, rate limits, and audit logs.

WhatsApp integration should be added only after reviewing provider access, templates, consent, and cost.

Deliverable: controlled follow-up workflow.

## Phase 5 — Knowledge and retrieval

- Add dealership policies, FAQs, and vehicle documentation.
- Use RAG only where source documents add value.
- Return references to retrieved records/documents.
- Test retrieval accuracy and unsupported-answer behaviour.

Deliverable: dealership knowledge assistant.

## Phase 6 — Pilot dashboard and reporting

- Lead pipeline view.
- Inventory status view.
- Pending follow-ups.
- Daily and weekly summaries.
- Staff roles and permissions.
- Usage and cost monitoring.

Deliverable: pilot-ready dashboard.

## Phase 7 — Multi-agent expansion

Only after the single-agent workflow is stable:
- Separate enquiry, inventory, follow-up, and reporting responsibilities.
- Define explicit input/output contracts.
- Add handoff limits, timeouts, and failure handling.
- Compare multi-agent value against a simpler single-agent workflow.

Deliverable: modular multi-agent system where complexity is justified.

## Release gates

Do not progress to a real customer pilot until:
- Inventory answers are grounded in current source records.
- No unsupported stock or price promises are made.
- Staff approval is enforced for external messages.
- Access controls and secret management are in place.
- Test cases cover normal, missing, stale, and conflicting data.
- A manual fallback exists when an integration fails.
