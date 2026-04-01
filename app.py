# app.py

import streamlit as st
from ranker import get_recommendations
from explanations import get_explanation
import pandas as pd
from classifier import predict_with_confidence
from suggestions import suggest_rephrase

# -------- PAGE CONFIG -------- #

st.set_page_config(
    page_title="ML Model Recommender",
    layout="centered",
    page_icon="🤖"
)

# -------- HEADER -------- #

st.title("🤖 ML Model Recommendation System")
st.caption("An intelligent system that analyzes your problem and suggests the best machine learning models.")

st.markdown("💡 Example: *Predict house prices based on area and location*")

st.markdown("---")

# -------- INPUT SECTION -------- #

st.subheader("📝 Enter Problem Details")

problem_text = st.text_area("Problem Statement")

dataset_size = st.selectbox("Dataset Size", ["small", "medium", "large"])
feature_count = st.selectbox("Feature Count", ["few", "many"])
data_type = st.selectbox("Data Type", ["numerical", "categorical", "mixed"])

st.markdown("---")

# -------- BUTTON -------- #

if st.button("🚀 Recommend Models"):

    if problem_text.strip() == "":
        st.warning("Please enter a problem statement.")
    else:

        # -------- PROCESSING -------- #
        with st.spinner("Analyzing problem and evaluating models..."):
            problem_type, confidence_scores = predict_with_confidence(problem_text)

            recommendations = get_recommendations(
                problem_type,
                dataset_size,
                feature_count,
                data_type
            )

        # -------- OUTPUT -------- #

        st.subheader("🔍 Detected Problem Type")
        st.info(f"**{problem_type.upper()}**")

        # -------- SUGGESTION -------- #

        suggestion = suggest_rephrase(problem_text, problem_type, confidence_scores)

        if suggestion:
            st.warning(f"⚠️ {suggestion}")

        st.markdown("---")

        # -------- CONFIDENCE -------- #

        st.subheader("🔎 Confidence Scores")

        conf_df = pd.DataFrame({
            "Problem Type": list(confidence_scores.keys()),
            "Confidence": list(confidence_scores.values())
        })

        st.bar_chart(conf_df.set_index("Problem Type"))

        st.markdown("---")

        # -------- BEST MODEL -------- #

        best_algo, best_score = recommendations[0]

        st.subheader("🥇 Best Recommendation")
        st.success(f"{best_algo} (Score: {best_score})")

        st.markdown("---")

        # -------- ALL RECOMMENDATIONS -------- #

        st.subheader("🏆 Top Recommended Algorithms")

        names = []
        scores = []

        for algo, score in recommendations:
            st.markdown(f"""
            ### 🧠 {algo}
            **Score:** {score}  
            {get_explanation(algo)}
            """)
            st.markdown("---")

            names.append(algo)
            scores.append(score)

        # -------- VISUALIZATION -------- #

        st.subheader("📊 Recommendation Scores")
        st.caption("Higher score indicates better suitability for the given problem.")

        df = pd.DataFrame({
            "Algorithm": names,
            "Score": scores
        })

        st.bar_chart(df.set_index("Algorithm"))