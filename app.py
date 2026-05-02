# app.py

import streamlit as st
import matplotlib.pyplot as plt
from ranker import get_recommendations
import pandas as pd
from classifier import predict_with_confidence
from suggestions import suggest_rephrase
from visuals import get_image_path
from dynamic_explanations import get_dynamic_explanation
from ml_predictor import predict_model


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

st.subheader("How the System Works")
st.image("assets/flow.png")
# -------- INPUT SECTION -------- #

st.subheader("Enter Problem Details")

problem_text = st.text_area("Problem Statement")

dataset_size = st.selectbox("Dataset Size", ["small", "medium", "large"])
feature_count = st.selectbox("Feature Count", ["few", "many"])
data_type = st.selectbox("Data Type", ["numerical", "categorical", "mixed"])

st.markdown("---")

# -------- BUTTON -------- #

if st.button("Recommend Models"):

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

        st.subheader("Detected Problem Type")
        st.info(f"**{problem_type.upper()}**")

        # -------- SUGGESTION -------- #

        suggestion = suggest_rephrase(problem_text, problem_type, confidence_scores)

        if suggestion:
            st.warning(f"{suggestion}")

        st.markdown("---")

        # -------- CONFIDENCE -------- #

        st.subheader("Confidence Scores")

        conf_df = pd.DataFrame({
            "Problem Type": list(confidence_scores.keys()),
            "Confidence": list(confidence_scores.values())
        })

        st.bar_chart(conf_df.set_index("Problem Type"))

        st.markdown("---")

        # -------- BEST MODEL -------- #

        best_algo, best_score = recommendations[0]

        st.subheader("Best Recommendation")
        st.success(f"{best_algo} (Score: {best_score})")

        st.markdown("---")

        # -------- ALL RECOMMENDATIONS -------- #

        st.subheader("Top Recommended Algorithms")

        names = []
        scores = []

        for algo, score in recommendations:
            reasons = get_dynamic_explanation(
                algo,
                dataset_size,
                feature_count,
                data_type
            )

            st.markdown(f"### {algo}")
            st.markdown(f"**Score:** {score}")

            st.markdown("**Why this model?**")
            for r in reasons:
                st.write(f"• {r}")
            img_path = get_image_path(algo)
            
            if img_path:
                st.image(img_path, caption=algo)
                
            st.markdown("---")

            names.append(algo)
            scores.append(score)

        # -------- VISUALIZATION -------- #

       # -------- VISUALIZATION -------- #

        st.subheader("Recommendation Scores")

        df = pd.DataFrame({
            "Algorithm": names,
            "Score": scores
        })

        fig, ax = plt.subplots()
        ax.bar(df["Algorithm"], df["Score"])

        ax.set_xlabel("Algorithms")
        ax.set_ylabel("Score")
        ax.set_title("Model Suitability Ranking")

        plt.xticks(rotation=30)

        st.pyplot(fig)