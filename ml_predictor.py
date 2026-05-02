import pickle

model = pickle.load(open("ml_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

def predict_model(problem_type, dataset_size, feature_count, data_type):

    input_data = {
        "problem_type": problem_type,
        "dataset_size": dataset_size,
        "feature_count": feature_count,
        "data_type": data_type
    }

    encoded = []
    for col in ["problem_type", "dataset_size", "feature_count", "data_type"]:
        encoded.append(encoders[col].transform([input_data[col]])[0])

    pred = model.predict([encoded])[0]
    probs = model.predict_proba([encoded])[0]

    return pred, probs