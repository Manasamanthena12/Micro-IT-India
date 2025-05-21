# Micro-IT-India
🎬 Movie Review Sentiment Analysis
Welcome to the Movie Review Sentiment Analysis app! This web app uses AI to analyze movie reviews and predict their sentiment—whether they’re Positive 😊, Negative 😔, or Neutral 😐—with an impressive 88.71% accuracy. Built as a personal project to explore natural language processing, this app offers a fun and insightful way to understand the emotions behind movie reviews. Launched on May 21, 2025, at 09:04 PM IST, it’s now live for everyone to try!
What Does This App Do? 🌟
The Movie Review Sentiment Analysis app makes it easy to gauge the sentiment of any movie review. Just type in a review, and the app will classify it as Positive, Negative, or Neutral, complete with a confidence score. It’s a quick way to see if a review leans toward praise, criticism, or neutrality—all with a cinematic flair! The app has a single, streamlined page:

A Main Page where you enter your review and get instant sentiment predictions, displayed in colorful boxes with emojis to keep things lively.

The app is hosted online, so you can access it anytime, anywhere with an internet connection.
Cool Things About the App ✨

Predicts three sentiments: Positive 😊, Negative 😔, and Neutral 😐, using a Logistic Regression model trained on the IMDb dataset.
Shows confidence scores for each prediction, so you know how sure the model is.
Features a light, movie-themed background with popcorn, clapperboards, cameras, and mics, paired with black text and orange accents for a vibrant look.
User-friendly design with a browser tab titled “Sentiment Analysis” and a 🎬 icon, plus a visible cursor in the input area.
Available online for everyone to try—no installation needed!

Tools We Used 🛠️
Here’s the tech stack behind the app:

Python: The core language for building the app.
Streamlit: Used to create the interactive web interface.
Pandas: For handling data during model training (in main.py).
Scikit-learn: Powers the Logistic Regression model for sentiment prediction.
NLTK: For text preprocessing, like removing stopwords.
Pickle: To save and load the trained model and vectorizer (built into Python, no extra install needed).

What’s in the Project Folder 📂

app.py: The main file that runs the Streamlit app.
model.pkl: The trained Logistic Regression model for sentiment prediction.
vectorizer.pkl: The TF-IDF vectorizer for transforming reviews into numerical features.
requirements.txt: A list of dependencies needed to run the app (e.g., Streamlit, Scikit-learn, NLTK).

Try the App Online 🌐
You can use the app right now on Streamlit Cloud:Access the app here: Movie Review Sentiment Analysis
Set Up the App on Your Computer 💻
Want to run the app locally? Follow these steps:
Things You Need

Python 3.8 or higher.
Git to download the project (optional).

Steps to Run

Download the ProjectOpen a terminal and type:  git clone https://github.com/your-username/sentiment-analysis-3.git
cd sentiment-analysis-3


Install DependenciesSet up a virtual environment (recommended) and install the required libraries:  pip install -r requirements.txt


Run the AppLaunch the app with Streamlit:  streamlit run app.py

This will open the app in your browser at http://localhost:8501.

About
Analyze the sentiment of movie reviews with AI! This project showcases natural language processing in action.
Resources

README
Activity

Stats

Stars: 0 stars  
Watchers: 1 watching  
Forks: 0 forks

Releases
No releases publishedCreate a new release
Packages
No packages publishedPublish your first package
Languages

Python: 100.0%

Suggested Workflows
Based on your tech stack:  

Python Package: Create and test a Python package on multiple Python versions.  
Publish Python Package: Publish a Python Package to PyPI on release.More workflows

Footer
Built with ❤️ by your-username. Try the app and share your feedback!
