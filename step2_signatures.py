import dspy

from config import setup_lm

setup_lm()

# 1. Inline signature: "input -> output"
summarize = dspy.Predict("text -> summary")
result = summarize(text="Our sync service was down for two hours because of an expired certificate.")
print(result.summary)

# 2. Multiple outputs, with type hints
classify = dspy.Predict("ticket: str -> category: str, urgency: str")
print(classify(ticket="I was charged twice this month!"))

# 3. See the exact prompt DSPy sent and what came back
dspy.inspect_history(n=1)