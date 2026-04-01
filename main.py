# main.py
from explanations import get_explanation
from classifier import predict_problem
from ranker import get_recommendations

# -------- USER INPUT -------- #

text = input("Enter problem statement: ")
dataset_size = input("Dataset size (small/medium/large): ")
feature_count = input("Feature count (few/many): ")
data_type = input("Data type (numerical/categorical/mixed): ")

# -------- PROCESS -------- #

problem_type = predict_problem(text)

recommendations = get_recommendations(
    problem_type,
    dataset_size,
    feature_count,
    data_type
)

# -------- OUTPUT -------- #

print("\nDetected Problem Type:", problem_type)
print("\nTop Recommended Algorithms:\n")

for algo, score in recommendations:
    print(f"{algo} (Score: {score})")
    print("Reason:", get_explanation(algo))
    print("-" * 40)