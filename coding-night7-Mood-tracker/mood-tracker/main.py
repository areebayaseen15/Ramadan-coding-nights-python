import streamlit as st
import pandas as pd
import datetime
import csv
import os

# File to store mood logs
MOOD_FILE = "mood_log.csv"

# Load mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE, on_bad_lines='skip')

# Save mood entry
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)

    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        # Add header if new file
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])

        writer.writerow([date, mood])

# Streamlit UI Styling
st.set_page_config(
    page_title="Mood Tracker",
    page_icon="😊",
    layout="centered"
)

# Custom CSS Styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ff6b6b;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #ff4757;
        }
        .stTitle {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #333;
        }
        .stFooter {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown('<h1 class="stTitle">🌈 Mood Tracker</h1>', unsafe_allow_html=True)

# Get today's date
today = datetime.date.today()

st.subheader("How are you feeling today?")

# Mood Selection with Icons
mood_options = {
    "😊 Happy": "Happy",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
    "😐 Neutral": "Neutral"
}

mood = st.selectbox("Select your mood", list(mood_options.keys()))

if st.button("Log Mood"):
    save_mood_data(today, mood_options[mood])
    st.success("✅ Mood logged successfully!")

# Load & Display Data
data = load_mood_data()

if not data.empty:
    st.subheader("📊 Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

# Footer
st.markdown(
    '<p class="stFooter">✨ Built by <b>Areeba Yaseen</b> | Powered by Streamlit</p>',
    unsafe_allow_html=True
)
