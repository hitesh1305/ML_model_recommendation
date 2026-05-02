import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv("dataset.csv")

# Encode features
encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Split
X = df.drop("best_model", axis=1)
y = df["best_model"]

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save
pickle.dump(model, open("ml_model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))

print("Model trained and saved.")