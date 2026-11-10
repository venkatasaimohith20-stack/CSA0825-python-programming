POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}
def score(text):
    """+1 per positive word, -1 per negative word; a preceding negator flips it."""
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0   
    # TODO 1: For each word, find its value (+1, -1 or 0); if previous word is a negator, flip sign
    for i, word in enumerate(words):
        val = 0
        if word in POSITIVE:
            val = 1
        elif word in NEGATIVE:
            val = -1          
        if val != 0 and i > 0 and words[i - 1] in NEGATORS:
            val = -val  # Flip sign           
        total += val       
    return total
def label(text):
    s = score(text)
    return "positive" if s > 0 else "negative" if s < 0 else "neutral"
for c in [
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved."
]:
    print(f"{label(c):8} | {c}")