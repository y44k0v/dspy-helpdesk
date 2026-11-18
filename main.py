import sys

import dspy

from config import setup_lm
from pipeline import build_pipeline

setup_lm()
bot = build_pipeline()


def handle(ticket: str):
    out = bot(ticket=ticket)
    print(f"\nCategory : {out.category}")
    print(f"Urgency  : {out.urgency}")
    print(f"Facts    : {out.facts}")
    print(f"\nReply:\n{out.reply}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        handle(" ".join(sys.argv[1:]))
    else:
        print("Type a ticket (empty line to quit). Add '!debug' to see the last prompts.")
        while True:
            text = input("> ").strip()
            if not text:
                break
            debug = text.endswith("!debug")
            handle(text.removesuffix("!debug").strip())
            if debug:
                dspy.inspect_history(n=3)