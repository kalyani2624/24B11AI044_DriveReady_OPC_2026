# AutoMate AI — Business Model

## 1. Customer segment

Initial segment: independent used-car dealerships and small pre-owned vehicle businesses in India.

Likely buyer: dealership owner or manager.  
Daily users: sales executives and inventory coordinators.

## 2. Customer value

AutoMate AI aims to reduce manual effort in:
- Capturing and qualifying customer enquiries.
- Searching dealer stock for suitable vehicles.
- Preparing consistent customer replies.
- Recording leads and follow-up dates.
- Reviewing pending enquiries.

The value proposition must be tested with dealership interviews and a working pilot.

## 3. Revenue model hypotheses

Potential revenue streams:
1. Monthly per-dealership subscription.
2. One-time onboarding and inventory-sheet setup.
3. Higher-tier plans for multiple staff members, branches, or reporting.
4. Paid custom integrations after the core product is reliable.

No fixed pricing is committed at this stage. Pricing should be based on interviews, willingness-to-pay tests, support costs, provider/API expenses, and the value demonstrated in pilots.

## 4. Go-to-market approach

1. Interview 5–10 independent used-car dealers.
2. Observe how enquiries and inventory are currently handled.
3. Select one recurring, costly workflow.
4. Build a small prototype around that workflow.
5. Pilot with one dealership using sample or explicitly authorised data.
6. Measure time saved, lead completeness, follow-up completion, and data errors.
7. Iterate before charging or expanding.

## 5. Cost considerations

Operating costs may include:
- LLM API usage.
- Hosting and database services.
- Messaging-provider charges.
- Data backup and monitoring.
- Customer onboarding and support.
- Security and compliance work.

Use ordinary code for exact calculations, scheduled jobs, filtering, and validation. Reserve LLM calls for tasks that need language understanding or generation.

## 6. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Incorrect inventory answer | Read live approved records, show update time, fail closed when unclear |
| Wrong vehicle details | Do not infer specs; require source-backed records |
| Unwanted customer messages | Human approval and consent-aware messaging |
| API cost growth | Token limits, model routing, caching where safe, usage monitoring |
| Staff resistance | Fit the existing workflow and keep the interface simple |
| Sensitive data exposure | Minimise collection, restrict access, retention and deletion process |

## 7. OPC readiness

The product concept may be suitable for exploration as a one-person business, but company formation, name availability, trademark clearance, tax, contracts, privacy, and applicable legal obligations need separate professional verification before commercial launch.
