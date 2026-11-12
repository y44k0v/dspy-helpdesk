from typing import Literal

import dspy

import os

from kb import search_kb

Category = Literal["billing", "technical", "account", "feature_request", "other"]
Urgency = Literal["low", "medium", "high"]


class Triage(dspy.Signature):
    """Classify a customer support ticket for Cumulo, a cloud note-taking app."""

    ticket: str = dspy.InputField()
    category: Category = dspy.OutputField()
    urgency: Urgency = dspy.OutputField()
    
class Research(dspy.Signature):
    """Use the knowledge base to find the facts needed to resolve the ticket."""

    ticket: str = dspy.InputField()
    facts: str = dspy.OutputField(desc="Relevant facts from the knowledge base, or 'none found'")
    

class DraftReply(dspy.Signature):
    """Write a short, friendly support reply using ONLY the provided facts.
    If the facts say 'none found', say that a human agent will follow up."""

    ticket: str = dspy.InputField()
    category: str = dspy.InputField()
    urgency: str = dspy.InputField()
    facts: str = dspy.InputField()
    reply: str = dspy.OutputField()

def reply_reward(args, pred) -> float:
    """1.0 when the reply follows both style rules, 0.5 for one, 0.0 for none."""
    reply = pred.reply.strip()
    short_enough = len(reply.split()) <= 120
    signed = reply.endswith("Cumulo Support")
    return (int(short_enough) + int(signed)) / 2

class Helpdesk(dspy.Module):
    def __init__(self):
        super().__init__()
        self.triage = dspy.ChainOfThought(Triage)
        self.research = dspy.ReAct(Research, tools=[search_kb], max_iters=3)
        #self.draft = dspy.ChainOfThought(DraftReply)
        self.draft = dspy.Refine(
            module=dspy.ChainOfThought(DraftReply),
            N=3,
            reward_fn=reply_reward,
            threshold=1.0,
        )

    def forward(self, ticket: str):
        t = self.triage(ticket=ticket)
        r = self.research(ticket=ticket)
        d = self.draft(
            ticket=ticket, category=t.category, urgency=t.urgency, facts=r.facts
        )
        return dspy.Prediction(
            category=t.category, urgency=t.urgency, facts=r.facts, reply=d.reply
        )
        
def build_pipeline(triage_path: str = "triage_optimized.json") -> Helpdesk:
    bot = Helpdesk()
    if os.path.exists(triage_path):
        bot.triage.load(triage_path)  # sub-modules can be loaded independently
    return bot