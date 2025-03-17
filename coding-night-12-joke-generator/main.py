import streamlit as st
import requests
import random

# Custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            background-color: #f4f4f4;
            font-family: 'Poppins', sans-serif;
        }
        
        .stButton>button {
            background-color: #ff5722;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 18px;
            transition: 0.3s ease;
        }
        

        .stSelectbox {
            font-size: 18px !important;
        }

        .joke-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            animation: fadeIn 1s;
            color : black
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
    </style>
""", unsafe_allow_html=True)



# Function to fetch a joke
def get_random_joke(joke_type):
    """Fetch a random joke based on the selected type."""
    if joke_type == "General Joke":
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")

            if response.status_code == 200:
                joke_data = response.json()
                return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
            else:
                return "Failed to fetch a joke, please try again later."
            
        except:
            return "Why did the programmer leave his job? \nBecause he didn't get the arrays!!"

    elif joke_type == "Programming Joke":
        try:
            response = requests.get("https://joke-api-gold.vercel.app/prgramming_joke")
            
            if response.status_code == 200:
                joke_data = response.json()
                return joke_data["jokes_list"]
            else:
                return "Failed to fetch a joke, please try again later."
        except:
            return "Why did the programmer leave his job? \nBecause he didn't get the arrays!!"
    elif joke_type == "Dark Humor Joke":
        try:
            response = requests.get("https://joke-api-gold.vercel.app/dark_humor_jokes")
            
            if response.status_code == 200:
                joke_data = response.json()
                return joke_data["jokes_list"]
            else:
                return "Failed to fetch a joke, please try again later."
        except:
            return "Why did the programmer leave his job? \nBecause he didn't get the arrays!!"
    
    elif joke_type == "Dad Joke":
        try:
            response = requests.get("https://joke-api-gold.vercel.app/dad_jokes")
            
            if response.status_code == 200:
                joke_data = response.json()
                return joke_data["jokes_list"]
            else:
                return "Failed to fetch a joke, please try again later."
        except:
            return "Why did the programmer leave his job? \nBecause he didn't get the arrays!!"
# Streamlit UI
st.markdown("<h1 style='text-align:center; color:#ff5722;'>😂 Random Joke Generator</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Select the joke type and click the button to get a laugh!</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])  # Center the elements

with col2:
    joke_type = st.selectbox("Choose joke type:", ["General Joke", "Programming Joke", "Dark Humor Joke", "Dad Joke"])

    if st.button("Tell me a joke!! 😂"):
        joke = get_random_joke(joke_type)
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align:center; margin-top: 30px;'>
        <p>Jokes from Official Joke API & Custom fastapi</p>
        <p>Built with ❤️ by <a href='https://github.com/areebayaseen15' target='_blank' style='color:#ff5722; text-decoration:none;'>Areeba Yaseen</a></p>
    </div>
""", unsafe_allow_html=True)
