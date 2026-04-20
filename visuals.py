def get_image_path(algo):

    mapping = {
        "Linear Regression": "assets/linear_regression.png",
        "Decision Tree Regressor": "assets/decision_tree_regressor.png",
        "Decision Tree": "assets/decision_tree.png",
        "Random Forest": "assets/random_forest.png",
        "Hierarchical Clustering":"assets/hierarchical_clustering.png",
        "KNN":"assets/knn.png",
        "Random Forest Regressor": "assets/random_forest.png",
        "Logistic Regression": "assets/logistic_regression.png",
        "SVM": "assets/svm.png",
        "K-Means": "assets/kmeans.png",
        "DBSCAN": "assets/dbscan.png",
        
    }

    return mapping.get(algo, None)