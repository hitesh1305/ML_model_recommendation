# rules.py

# ---------------- REGRESSION ---------------- #

def regression_rules(dataset_size, feature_count, data_type):
    scores = {
        "Linear Regression": 1,
        "Decision Tree Regressor": 1,
        "Random Forest Regressor": 1,
        "Ridge/Lasso": 1
    }

    # Dataset size
    if dataset_size == "small":
        scores["Linear Regression"] += 2
        scores["Decision Tree Regressor"] += 1

    elif dataset_size == "medium":
        scores["Linear Regression"] += 1
        scores["Decision Tree Regressor"] += 1
        scores["Random Forest Regressor"] += 1

    elif dataset_size == "large":
        scores["Random Forest Regressor"] += 2
        scores["Decision Tree Regressor"] += 1

    # Feature count
    if feature_count == "few":
        scores["Linear Regression"] += 2
        scores["Decision Tree Regressor"] += 1

    elif feature_count == "many":
        scores["Ridge/Lasso"] += 2
        scores["Random Forest Regressor"] += 1

    # Data type
    if data_type == "numerical":
        scores["Linear Regression"] += 1

    elif data_type == "mixed":
        scores["Decision Tree Regressor"] += 1
        scores["Random Forest Regressor"] += 1

    return scores


# ---------------- CLASSIFICATION ---------------- #

def classification_rules(dataset_size, feature_count, data_type):
    scores = {
        "Logistic Regression": 1,
        "SVM": 1,
        "Decision Tree": 1,
        "Random Forest": 1,
        "KNN": 1
    }

    # Dataset size
    if dataset_size == "small":
        scores["Logistic Regression"] += 2
        scores["KNN"] += 1

    elif dataset_size == "medium":
        scores["Decision Tree"] += 1
        scores["Random Forest"] += 1

    elif dataset_size == "large":
        scores["Random Forest"] += 2
        scores["SVM"] += 1

    # Feature count
    if feature_count == "few":
        scores["Logistic Regression"] += 1
        scores["Decision Tree"] += 1

    elif feature_count == "many":
        scores["SVM"] += 2
        scores["Random Forest"] += 1

    # Data type
    if data_type == "numerical":
        scores["Logistic Regression"] += 1

    elif data_type == "categorical":
        scores["Decision Tree"] += 2

    elif data_type == "mixed":
        scores["Decision Tree"] += 2
        scores["Random Forest"] += 1

    return scores


# ---------------- CLUSTERING ---------------- #

def clustering_rules(dataset_size, feature_count, data_type):
    scores = {
        "K-Means": 1,
        "DBSCAN": 1,
        "Hierarchical Clustering": 1
    }

    # Dataset size
    if dataset_size == "small":
        scores["Hierarchical Clustering"] += 2

    elif dataset_size == "medium":
        scores["K-Means"] += 1
        scores["DBSCAN"] += 1

    elif dataset_size == "large":
        scores["K-Means"] += 2

    # Feature count
    if feature_count == "many":
        scores["K-Means"] += 1

    # Data type
    if data_type == "numerical":
        scores["K-Means"] += 1

    elif data_type == "mixed":
        scores["DBSCAN"] += 2

    return scores