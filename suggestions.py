def suggest_rephrase(text, prediction, confidence_scores):

    max_conf = max(confidence_scores.values())

    text = text.lower()

    if max_conf < 0.65:

        # Special intelligent correction
        if "price" in text or "amount" in text or "value" in text:
            return "Did you mean 'predict' instead of 'detect'? This looks like a regression problem."

        if prediction == "regression":
            return "Try using words like 'predict', 'estimate', or specify a numerical outcome."

        elif prediction == "classification":
            return "Try specifying categories like 'yes/no', 'spam/not spam', etc."

        elif prediction == "clustering":
            return "Try using words like 'group', 'segment', or 'cluster'."

    return None