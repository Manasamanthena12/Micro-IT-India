# Micro-IT-India
Sentiment Analysis for Movie Reviews
# Movie Review Sentiment Analysis
A Streamlit app to predict the sentiment (Positive, Negative, or Neutral) of movie reviews using a Logistic Regression model.

## Features
- Trained on the IMDb dataset with 88.71% accuracy.
- Detects Positive 😊, Negative 😔, and Neutral 😐 sentiments with confidence scores.
- Light, movie-themed interface with elements like popcorn, clapperboard, and camera.
- Deployed on Streamlit Cloud: [https://sentiment-analysis-3.streamlit.app/](https://sentiment-analysis-3.streamlit.app/)

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run locally: `streamlit run app.py`.

## Files
- `main.py`: Data preprocessing, EDA, and model training.
- `app.py`: Streamlit app for predictions.
- `model.pkl` & `vectorizer.pkl`: Trained model and vectorizer.
