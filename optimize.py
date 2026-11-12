import dspy

from config import setup_lm
from data import devset, trainset
from metrics import triage_metric
from pipeline import Triage

setup_lm()

student = dspy.ChainOfThought(Triage)

optimizer = dspy.BootstrapFewShot(
    metric=triage_metric,
    max_bootstrapped_demos=4,  # demos the model generates itself and that pass the metric
    max_labeled_demos=4,       # demos taken directly from the labeled data
)
optimized = optimizer.compile(student, trainset=trainset)

evaluate = dspy.Evaluate(devset=devset, metric=triage_metric, num_threads=1, display_progress=True)
print(f"Optimized score: {evaluate(optimized).score:.1f}%")

optimized.save("triage_optimized.json")  # human-readable JSON with the learned demos
print("Saved triage_optimized.json")