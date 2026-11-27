# AutoMate AI — Product Vision

**Working product name:** AutoMate AI  
**Positioning:** The AI sales and operations co-pilot for independent used-car dealerships  
**Tagline:** More organised leads. Better-informed customers. Smoother dealership operations.

## 1. The problem

Small and independent used-car dealerships often coordinate customer enquiries, vehicle stock details, test-drive requests, follow-ups, and daily reporting through a mixture of phone calls, messaging apps, notebooks, and spreadsheets.

When these workflows are disconnected, a dealership can struggle to:
- Keep customer enquiries organised.
- Match customer requirements with vehicles actually in stock.
- Follow up with interested buyers on time.
- Keep vehicle details consistent across customer conversations.
- Understand the status of leads and pending actions.

These are product hypotheses to validate with real dealerships, not assumptions that every dealer has the same workflow.

## 2. Target customer

The initial target segment is independent used-car dealerships and small pre-owned vehicle businesses in India.

Primary users:
- Dealership owner or manager.
- Sales executive.
- Inventory coordinator.
- Customer enquiry or follow-up staff.

The first pilot should focus on one dealership and a small, clearly defined workflow.

## 3. Product promise

AutoMate AI will sit alongside the dealership's existing process and help staff handle repetitive information work. It should not force a dealership to replace every existing system before receiving value.

The product should:
1. Capture and structure a customer enquiry.
2. Ask for missing buying requirements.
3. Match the enquiry against connected, current dealership inventory.
4. Prepare a clear response for the sales executive.
5. Record lead status and next follow-up.
6. Summarise pending enquiries and daily activity.

## 4. Initial MVP boundary

The first MVP should solve one end-to-end workflow:

**Customer enquiry → qualification → inventory match → staff-approved reply → lead record → follow-up reminder.**

MVP capabilities:
- English-first conversational enquiry intake.
- Structured lead extraction (budget, preferred body type, transmission, fuel, location, timeline, contact consent).
- Inventory search from a dealer-approved Google Sheet or CSV.
- Match results with source rows and last-updated time.
- Drafted replies that a human approves before sending.
- Lead logging and follow-up status.
- A simple daily pending-leads summary.

The first MVP should not:
- Purchase, reserve, or sell a vehicle autonomously.
- Promise that a vehicle is available without checking current inventory.
- Settle prices or negotiate on behalf of a dealer.
- Send unsolicited messages.
- Store identity documents or sensitive customer data without a justified, secure process.
- Claim to verify ownership, accident history, finance, or legal status without authoritative records.

## 5. Product principles

- **Truth over fluency:** never invent stock, price, mileage, ownership, accident history, or vehicle condition.
- **Human approval:** customer-facing messages and consequential changes require staff approval in the MVP.
- **Traceability:** show which inventory record or lead record supports an answer.
- **Least privilege:** connect only the spreadsheet, messaging channel, and permissions required.
- **Privacy by design:** collect only necessary data, explain its use, and define retention.
- **Cost-aware AI:** use deterministic Python for calculations, filtering, validation, and scheduled tasks; use an LLM for language understanding and drafting.
- **Useful before broad:** make one dealership workflow reliable before adding many agents.

## 6. Success measures for a pilot

Measure before and after the pilot:
- Time taken to enter and qualify an enquiry.
- Percentage of enquiries with complete required fields.
- Time to identify matching vehicles in stock.
- Follow-up completion rate.
- Number of stale or incorrect inventory answers.
- Staff time spent on routine enquiry administration.
- Staff acceptance rate of AI-drafted replies.

Do not claim business impact until it is measured with pilot data.

## 7. Long-term direction

After validating the MVP, AutoMate AI may expand into multi-branch inventory, dealer analytics, service reminders, document checklists, test-drive coordination, and additional dealership workflows. Each expansion must be supported by customer demand, trustworthy data sources, and appropriate controls.
