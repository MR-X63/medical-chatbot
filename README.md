# Medical Chatbot

An AI-powered medical chatbot built with Python that checks symptoms, predicts possible diseases, and suggests nearby hospitals.

Built by Sayyed Shan | AIML Student

## Features

- Symptom Checker - Describe your symptoms in plain English
- Disease Prediction - AI suggests possible conditions with severity rating
- Hospital Suggestions - Finds nearby hospitals based on required specialty
- Multi-turn Chat - Remembers conversation context
- Web UI - Clean chat interface built with Streamlit

## Tech Stack

- Python 3
- Groq API (LLaMA 3.3 70B model)
- Streamlit (web UI)
- CSV (hospital database)

## How to Run

1. Clone the repository
git clone https://github.com/MR-X63/medical-chatbot.git
cd medical-chatbot

2. Install dependencies
pip install streamlit groq

3. Get a free Groq API key
Go to console.groq.com, sign up and create an API key

4. Run the web app
streamlit run app.py

5. Run terminal version
python main.py

## Project Structure

app.py - Streamlit web UI
main.py - Terminal version
chatbot.py - Groq API logic
hospitals.py - Hospital filtering logic
hospitals.csv - Hospital database
requirement.txt - Dependencies

## How It Works

1. User describes symptoms in chat
2. AI analyzes symptoms and gives possible diagnosis
3. AI rates severity as Mild, Moderate, or Serious
4. AI suggests which medical specialty to consult
5. App filters hospitals.csv and shows nearby hospitals

## Disclaimer

This chatbot is for educational purposes only. It is not a substitute for professional medical advice. Always consult a real doctor.

## Author

Sayyed Shan - AIML Student
GitHub: github.com/MR-X63
Email: sayyedshan1433@gmail.com
