import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

# Set the page title and icon
st.set_page_config(page_title="Sentiment Analysis", page_icon="🎬")

# Download NLTK stopwords if not already done
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Load model and vectorizer
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    st.error("Model or vectorizer not found. Please run main.py first to train the model.")
    st.stop()

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Streamlit app
st.title("🎬 Movie Review Sentiment Analysis")
st.subheader("Discover the Emotion Behind Your Review!")
st.write("Enter a movie review to predict its sentiment (Positive, Negative, or Neutral).")

# User input
user_input = st.text_area("Enter your movie review:", placeholder="Type your review here (e.g., 'This movie was amazing!' or 'It was okay.')", height=150)

if 'prediction' not in st.session_state:
    st.session_state.prediction = None
    st.session_state.confidence = None

if st.button("Predict Sentiment"):
    if user_input:
        # Preprocess input
        cleaned_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        
        # Predict with probabilities
        prediction_proba = model.predict_proba(vectorized_input)[0]
        prediction = model.predict(vectorized_input)[0]
        
        # Determine sentiment based on probabilities
        prob_positive = prediction_proba[1]  # Probability of Positive (class 1)
        if prob_positive > 0.6:
            sentiment = "Positive 😊"
            color = "green"
        elif prob_positive < 0.4:
            sentiment = "Negative 😔"
            color = "red"
        else:
            sentiment = "Neutral 😐"
            color = "gray"
        
        # Store prediction and confidence in session state
        st.session_state.prediction = sentiment
        st.session_state.confidence = prob_positive if sentiment != "Neutral 😐" else abs(prob_positive - 0.5)
        
        # Display result in a styled box
        st.markdown(
            f"""
            <div style='background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;'>
                <h3>Sentiment: {sentiment}</h3>
                <p>Confidence: {st.session_state.confidence:.2%}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display model accuracy
        st.write(f"Model Accuracy: ~{0.8871:.2%} (based on test set)")
    else:
        st.warning("Please enter a review before predicting.")

# Add styling with a light movie-themed background and black text
st.markdown("""
<style>
    body {
        background-image: url('https://images.unsplash.com/photo-1598899134739-24c46f58b8c0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: black;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 20px;
    }
    .stTextArea textarea {
        font-size: 16px;
        padding: 10px;
        background-color: white;
        color: black;
        border: 2px solid #FF4500; /* Orange border for visibility */
        border-radius: 10px;
        caret-color: black; /* Ensure cursor is visible */
    }
    .stButton button {
        background-color: #FF4500; /* Orange button */
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        margin: 5px;
    }
    .stButton button:hover {
        background-color: #FF6347;
    }
    h1, h3 {
        color: #FF4500; /* Orange headers */
        text-align: center;
    }
    p, div {
        color: black;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)