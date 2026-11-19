from fastapi import FastAPI
from pydantic import BaseModel

from config import setup_lm
from pipeline import build_pipeline

setup_lm()                # configure DSPy once, at startup
bot = build_pipeline()    # loads triage_optimized.json if present

app = FastAPI(title="Cumulo Helpdesk (DSPy)")


class TicketIn(BaseModel):
    ticket: str


class TicketOut(BaseModel):
    category: str
    urgency: str
    facts: str
    reply: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/triage", response_model=TicketOut)
def triage(body: TicketIn):
    out = bot(ticket=body.ticket)
    return TicketOut(category=out.category, urgency=out.urgency, facts=out.facts, reply=out.reply)