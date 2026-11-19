# DSPy Simple help desk
## Gemini API free tier

A pipeline that takes a raw customer ticket and returns:

 1. a category (billing, technical, account, feature_request, other),
 2. an urgency (low, medium, high),
 3. a drafted reply, grounded in a small knowledge base and checked against style rules.

```
        ticket ──► Triage (ChainOfThought) ──► category + urgency ─┐
           │                                                       ├─► Draft
         reply (ChainOfThought + Refine) ──► reply
           └────► Research (ReAct + search tool) ──► facts ────────┘

```

### Usage 
#### Terminal
```BASH
$ uv run python main "My invoice has the wrong company name, I need it fixed for taxes."

Category : billing
Urgency  : high
Facts    : To correct the company name on your invoice, reply to the invoice email. Support will reissue it within 2 business days.

Reply:
Hello!

To correct the company name on your invoice, please reply directly to the invoice email. Our support team will then reissue it within 2 business days.

Cumulo Support
```
