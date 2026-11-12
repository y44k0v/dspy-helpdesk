from config import setup_lm
print("\nImports okay\n")
lm = setup_lm()
print("\nLM loaded\n")

# Calling the LM directly returns a list of completions.
print(lm("Say hello in one short sentence."))
