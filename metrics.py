import dspy

from kb import kb_as_text


def triage_metric(example, pred, trace=None):
    """Fraction of (category, urgency) that match the label."""
    score = (int(example.category == pred.category) + int(example.urgency == pred.urgency)) / 2
    # During optimization (trace is not None) optimizers want a strict pass/fail.
    return score == 1.0 if trace is not None else score


class Judge(dspy.Signature):
    """Decide whether the support reply is helpful for the ticket and
    stays faithful to the knowledge base (no invented policies)."""

    ticket: str = dspy.InputField()
    reply: str = dspy.InputField()
    knowledge_base: str = dspy.InputField()
    is_good: bool = dspy.OutputField()


def pipeline_metric(example, pred, trace=None):
    """LLM-as-judge: triage correctness plus reply quality."""
    cat_ok = int(example.category == pred.category)
    urg_ok = int(example.urgency == pred.urgency)
    verdict = dspy.Predict(Judge)(
        ticket=example.ticket, reply=pred.reply, knowledge_base=kb_as_text()
    )
    score = (cat_ok + urg_ok + int(verdict.is_good)) / 3
    return score == 1.0 if trace is not None else score