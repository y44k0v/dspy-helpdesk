import dspy
from config import setup_lm
from pipeline import Triage

setup_lm()
triage = dspy.ChainOfThought(Triage)
out = triage(ticket="The desktop app stopped syncing and I have a presentation in an hour!")

print(out.category)   # e.g. technical
print(out.urgency)    # e.g. high
print(out.reasoning)  # the model's step-by-step reasoning