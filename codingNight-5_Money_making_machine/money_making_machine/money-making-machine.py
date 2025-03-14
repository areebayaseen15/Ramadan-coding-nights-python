import streamlit as st
import random
import time
import requests
import os

st.title("💰 Money Making Machine" )

# Function to load CSS with correct path
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css") 
    try:
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Warning: CSS file '{css_path}' not found.")

# Load the external CSS
load_css()

# Money making function
def generate_money():
    return random.randint(1, 1000)

st.subheader("💵 Instant Cash Generator")
if st.button("Generate Money", key="green"):
    st.write("⏳ Counting Your Money...")    
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made **${amount}!** 🎉")

def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-money-quotes-side-hustles-5r3zs8fxd.vercel.app/side_hustles")
        if response.status_code == 200:
            hustle = response.json()
            return hustle["side_husttle"]
        else:
            return "Freelancing"
    except:
        return "❌ Something went wrong"

st.subheader("🚀 Side Hustle Ideas")
if st.button("Generate Hustle", key="pink"):
    idea = fetch_side_hustle()
    st.info(idea)


#money quotes function
def money_quotes():
    try:
        response = requests.get("https://fastapi-money-quotes-side-hustles-5r3zs8fxd.vercel.app/money_quotes")
        if response.status_code == 200:
            money_quotes = response.json()
            return money_quotes["money_quotes"]
        else:
            return "💡 The more you learn, the more you earn."
    except:
        return "❌ Something went wrong"

st.subheader("💡 Money Making Motivation Quotes")
if st.button("Get Money Quotes", key="blue"):
    quotes = money_quotes()
    st.info(quotes)
