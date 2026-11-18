import dspy

from config import setup_lm
from data import devset
from metrics import pipeline_metric
from pipeline import build_pipeline

setup_lm()
bot = build_pipeline()
evaluate = dspy.Evaluate(devset=devset[:5], metric=pipeline_metric, num_threads=1, display_progress=True)
print(f"Full pipeline score: {evaluate(bot).score:.1f}%")