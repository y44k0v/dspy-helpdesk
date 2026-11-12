import dspy
from config import setup_lm
from kb import search_kb
from pipeline import Research

setup_lm()
agent = dspy.ReAct(Research, tools=[search_kb], max_iters=3)
out = agent(ticket="How can I export my notes as Markdown?")
print(out.facts)
dspy.inspect_history(n=3)  # watch the thought / tool call / observation loop