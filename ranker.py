# ranker.py

from rules import regression_rules, classification_rules, clustering_rules

def get_recommendations(problem_type, dataset_size, feature_count, data_type):
    """
    Returns top 3 algorithms based on scoring rules
    """

    if problem_type == "regression":
        scores = regression_rules(dataset_size, feature_count, data_type)

    elif problem_type == "classification":
        scores = classification_rules(dataset_size, feature_count, data_type)

    elif problem_type == "clustering":
        scores = clustering_rules(dataset_size, feature_count, data_type)

    else:
        return []

    # Sort algorithms by score (descending)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:3]