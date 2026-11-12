import dspy

from config import setup_lm
from data import devset
from metrics import triage_metric
from pipeline import Triage

setup_lm()

triage = dspy.ChainOfThought(Triage)

evaluate = dspy.Evaluate(
    devset=devset,
    metric=triage_metric,
    num_threads=1,          # keep low on the free tier to avoid rate limits
    display_progress=True,
    display_table=5,        # show 5 example rows
)

result = evaluate(triage)
print(f"Baseline score: {result.score:.1f}%")