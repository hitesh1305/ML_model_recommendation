# suggestions.py

def suggest_rephrase(text, prediction, confidence_scores):

    max_conf = max(confidence_scores.values())

    # If confidence is low → suggest improvement
    if max_conf < 0.65:

        if prediction == "regression":
            return "Try using words like 'predict', 'estimate', or specify a numerical outcome."

        elif prediction == "classification":
            return "Try specifying categories like 'yes/no', 'spam/not spam', etc."

        elif prediction == "clustering":
            return "Try using words like 'group', 'segment', or 'cluster'."

    return None