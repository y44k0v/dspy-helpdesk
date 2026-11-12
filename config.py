import os

import dspy
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables
# gemini-3.8-flash gives a 503 error high demand, try later
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def setup_lm() -> dspy.LM:
    """Create the Gemini LM and make it the default for all DSPy modules."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")

    lm = dspy.LM(
        f"gemini/{MODEL}",
        api_key=api_key,
        max_tokens=8192,   # Flash models may spend tokens "thinking", so leave room
        num_retries=8,     # automatically retry on 429 / transient errors
    )
    dspy.configure(lm=lm)  # global default
    return lm
