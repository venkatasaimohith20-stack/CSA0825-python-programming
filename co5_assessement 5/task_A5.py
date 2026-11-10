POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}
def score_sentiment(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    for i, word in enumerate(words):
        val = 0
        if word in POSITIVE:
            val = 1
        elif word in NEGATIVE:
            val = -1           
        if val != 0 and i > 0 and words[i - 1] in NEGATORS:
            val = -val  # Flip sign if preceded by a negator
        total += val
    return total
def rule_based_chatbot_query(question):
    """Simulates answering citizen queries by matching station keywords."""
    question_lower = question.lower()
    if "adyar" in question_lower:
        return "Querying database for Adyar: Current PM2.5 is 48.0 (Status: Moderate)."
    elif "guindy" in question_lower:
        return "Querying database for Guindy: Current PM2.5 is 95.0 (Status: Poor)."
    return "Sorry, I didn't recognize that station name. Try asking about Adyar or Guindy."
print("Sentiment Score:", score_sentiment("The roads are not clean."))  # Output: -1 (Negative)
print("Chatbot Response:", rule_based_chatbot_query("What is the PM2.5 in Adyar today?"))