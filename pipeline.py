from typing import Literal

import dspy

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