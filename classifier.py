# classifier.py

import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_with_confidence(text):
    text = text.lower()
    vec = vectorizer.transform([text])

    probs = model.predict_proba(vec)[0]
    classes = model.classes_

    result = dict(zip(classes, probs))

    prediction = model.predict(vec)[0]

    return prediction, result