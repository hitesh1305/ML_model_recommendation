# 🧠 ML Model Recommendation System
Hybrid AI Decision Support System using NLP, Rule-Based Logic & Machine Learning

---

## 🚀 Overview

Selecting the right machine learning algorithm is a challenging task, especially for beginners. This project builds a hybrid system that analyzes a natural language problem statement and dataset characteristics to recommend the most suitable ML algorithms.

The system provides:
- Top 3 algorithm recommendations
- Confidence scores
- Clear explanations

This reduces trial-and-error and improves decision-making in ML workflows.

---

## 🎯 Key Features

- NLP-based problem understanding  
- Hybrid system (Rule-based + ML-based)  
- Top 3 algorithm recommendations  
- Dynamic explanations  
- Confidence-based ambiguity handling  
- Streamlit-based interactive UI  
- Real-time prediction  

---

## 🏗️ System Architecture

User Input (Text + Parameters)  
→ TF-IDF Vectorization  
→ Logistic Regression Classifier  
→ Problem Type Detection  
→ Rule-Based Engine + ML-Based Engine  
→ Score Combination  
→ Top 3 Recommendations  
→ Explanation + Confidence  
→ UI Output  

---

## ⚙️ Tech Stack

- Python  
- scikit-learn  
- pandas  
- NumPy  
- NLTK  
- Streamlit  
- matplotlib  

---

## 🧩 Project Structure

ml_model_recommendation/

- app.py → Main application  
- classifier.py → NLP classifier  
- rules.py → Rule-based engine  
- ranker.py → Ranking logic  
- dynamic_explanations.py → Explanation generator  
- suggestions.py → Ambiguity handling  
- ml_predictor.py → ML-based ranking  
- train_model.py → Model training  
- dataset.csv → Training dataset  

Saved models:
- model.pkl  
- vectorizer.pkl  
- ml_model.pkl  
- encoders.pkl  

---

## 🔄 Implementation Workflow

1. User enters problem statement and selects dataset details  

2. Text is converted into numerical form using TF-IDF  

3. Logistic Regression predicts problem type  
   (classification / regression / clustering)  

4. Input features are prepared for ranking  

5. Rule-based engine assigns scores using predefined logic  

6. Random Forest model predicts best algorithm  

7. Scores from both systems are combined  

8. Algorithms are ranked and top 3 are selected  

9. Dynamic explanations are generated  

10. Final results are displayed with confidence  

---

## 🧠 Machine Learning Techniques Used

TF-IDF  
- Converts text into numerical vectors  
- Highlights important words  

Logistic Regression  
- Classifies problem type  
- Outputs probabilities  

Random Forest  
- Predicts best algorithm  
- Uses multiple decision trees  

---

## 📊 Performance

- ~91% classification accuracy  
- Real-time response  
- Tested on multiple scenarios  
- Handles ambiguous inputs  

---

## 💡 Why This Project is Useful

- Reduces manual model selection effort  
- Helps beginners understand algorithm choice  
- Provides explainable recommendations  
- Saves time in ML workflow  
- Acts as a decision-support system  

---

## 🌍 Contribution to ML Community

- Combines rule-based and ML-based approaches  
- Demonstrates NLP for ML problem understanding  
- Provides explainable recommendations  
- Introduces confidence-based feedback  
- Offers a simple and extensible framework  

---

## ⚠️ Limitations

- Small dataset for ML ranking  
- Rule-based logic is predefined  
- No dataset content analysis  
- TF-IDF lacks deep semantic understanding  

---

## 🚀 Future Improvements

- Replace TF-IDF with embeddings (BERT)  
- Expand dataset  
- Add AutoML integration  
- Perform dataset analysis  
- Improve UI  

---

## 📦 Installation

git clone https://github.com/hitesh1305/ML_model_recommendation.git

cd ml_model_recommendation  
pip install -r requirements.txt  
streamlit run app.py  

---

## 👨‍💻 Authors

Hitesh – NLP, rule-based system, architecture, ML model, dataset, integration  

---

## ⭐ Conclusion

This project demonstrates how NLP, rule-based logic, and machine learning can be combined to build an intelligent and explainable system for ML model selection.
