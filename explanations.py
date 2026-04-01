# explanations.py

def get_explanation(algo):

    explanations = {

        "Linear Regression":
        "Works well with numerical data and few features. It is simple, fast, and interpretable.",

        "Decision Tree Regressor":
        "Handles nonlinear relationships and is easy to understand and visualize.",

        "Random Forest Regressor":
        "An ensemble model that improves accuracy and handles complex patterns effectively.",

        "Ridge/Lasso":
        "Useful when there are many features. Helps reduce overfitting using regularization.",

        "Logistic Regression":
        "Simple and effective for classification problems with linear boundaries.",

        "SVM":
        "Effective in high-dimensional spaces and works well with many features.",

        "Decision Tree":
        "Easy to interpret and works well with mixed data types.",

        "Random Forest":
        "Robust and handles large datasets with complex relationships.",

        "KNN":
        "Simple algorithm based on similarity between data points.",

        "K-Means":
        "Efficient clustering method for large datasets with clear groupings.",

        "DBSCAN":
        "Can find clusters of arbitrary shape and handle noise.",

        "Hierarchical Clustering":
        "Builds a tree of clusters and works well for small datasets."
    }

    return explanations.get(algo, "No explanation available.")