import streamlit as st
import random
import time
import requests
import pathlib

st.title("💰 Money Making Machine" )


#function to load css

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

#load the external css
css_path = pathlib.Path("style.css")
load_css(css_path)

#money making function
def generate_money():
    return random.randint(1, 1000)

st.subheader("💵 Instant Cash Generator")
if st.button("Generate Money" , key="green"):
    st.write("⏳ Counting Your Money...")    
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made **${amount}!** 🎉")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?api_key=1234567")
        if response.status_code == 200:
            hustle = response.json()
            return hustle["side_husttle"]
        else:
            return "Freelancing"
    except:
        return "❌ Something went wrong"

st.subheader("🚀 Side Hustle Ideas")
if st.button("Generate Hustle" , key="pink"):
    idea = fetch_side_hustle()
    st.info(idea)

def money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=1234567")
        if response.status_code == 200:
            money_quotes = response.json()
            return money_quotes["money_quotes"]
        else:
            return "💡 The more you learn, the more you earn."
    except:
        return "❌ Something went wrong"

st.subheader("💡 Money Making Motivation Quotes")
if st.button("Get Money Quotes" , key = "blue"):
    quotes = money_quotes()
    st.info(quotes)
