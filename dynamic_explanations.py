# dynamic_explanations.py

def get_dynamic_explanation(algo, dataset_size, feature_count, data_type):

    reasons = []

    # -------- REGRESSION -------- #

    if algo == "Linear Regression":
        if feature_count == "few":
            reasons.append("Works well with a small number of features")
        if data_type == "numerical":
            reasons.append("Suitable for numerical data")
        if dataset_size in ["small", "medium"]:
            reasons.append("Performs efficiently on small to medium datasets")

    elif algo == "Decision Tree Regressor":
        reasons.append("Can capture nonlinear relationships")
        if data_type == "mixed":
            reasons.append("Handles mixed data types effectively")

    elif algo == "Random Forest Regressor":
        reasons.append("Handles complex and nonlinear patterns")
        if dataset_size == "large":
            reasons.append("Performs well on large datasets")
        if feature_count == "many":
            reasons.append("Works well with many features")

    elif algo == "Ridge/Lasso":
        if feature_count == "many":
            reasons.append("Helps prevent overfitting with many features")
        reasons.append("Applies regularization to improve generalization")

    # -------- CLASSIFICATION -------- #

    elif algo == "Logistic Regression":
        reasons.append("Simple and interpretable model")
        if data_type == "numerical":
            reasons.append("Works well with numerical input features")

    elif algo == "Decision Tree":
        reasons.append("Easy to interpret and visualize")
        if data_type == "mixed":
            reasons.append("Handles mixed data types well")

    elif algo == "Random Forest":
        reasons.append("Robust and reduces overfitting")
        if dataset_size == "large":
            reasons.append("Suitable for large datasets")

    elif algo == "SVM":
        if feature_count == "many":
            reasons.append("Effective in high-dimensional spaces")
        reasons.append("Finds optimal decision boundaries")

    elif algo == "KNN":
        reasons.append("Based on similarity between data points")
        if dataset_size == "small":
            reasons.append("Works better on smaller datasets")

    # -------- CLUSTERING -------- #

    elif algo == "K-Means":
        if dataset_size == "large":
            reasons.append("Efficient for large datasets")
        reasons.append("Works well when clusters are well-defined")

    elif algo == "DBSCAN":
        reasons.append("Detects clusters of arbitrary shape")
        if data_type == "mixed":
            reasons.append("Handles noise and outliers effectively")

    elif algo == "Hierarchical Clustering":
        if dataset_size == "small":
            reasons.append("Suitable for smaller datasets")
        reasons.append("Builds a hierarchy of clusters")

    # -------- DEFAULT -------- #

    if not reasons:
        reasons.append("Suitable based on given problem characteristics")

    return reasons