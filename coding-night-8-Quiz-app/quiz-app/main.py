import streamlit as st
import random
import time

# Custom Page Configurations
st.set_page_config(page_title="Interactive Quiz", page_icon="🎯", layout="centered")

quiz_questions = [
    {
        "question": "What will be the output of the following code? x = [1, 2, 3]; y = x; y.append(4); print(x)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "None", "Error"],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "question": "How do you create a set in Python?",
        "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "'1, 2, 3'"],
        "answer": "{1, 2, 3}"
    },
    {
        "question": "What will bool([]) return?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False"
    }
]

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }
    .main {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff9966, #ff5e62);
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
        border: none;
        transition: 0.3s ease-in-out;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #ff5e62, #ff9966);
        transform: scale(1.05);
    }
    .stRadio label {
        font-size: 16px;
    }
    h1 {
        font-size: 40px;
        font-weight: bold;
        color: #ff5733;
        text-shadow: 2px 2px 10px rgba(255, 87, 51, 0.3);
        animation: fadeIn 1s ease-in-out;
    }
    .score-box {
        font-size: 18px;
        color: #444;
        background: #f0f0f0;
        padding: 10px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 10px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 20px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True
)

# Session State: Store the current question, score, and quiz status
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_questions)
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_ended" not in st.session_state:
    st.session_state.quiz_ended = False  # Track quiz status

question = st.session_state.current_question

# Title
st.title("🎯 Interactive Quiz Game")

# Score display
st.markdown(f"<div class='score-box'>Score: {st.session_state.score}</div>", unsafe_allow_html=True)

if not st.session_state.quiz_ended:
    # Display question
    st.subheader(question["question"])

    # Multiple options
    selected_option = st.radio("Choose your answer", question["options"], key="answer")

    # Submit Answer
    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1  # Increase score on correct answer
            st.balloons()
        else:
            st.error(f"❌ Incorrect! The correct answer is: {question['answer']}")

        time.sleep(1.5)

        # Selecting a new random question
        st.session_state.current_question = random.choice(quiz_questions)

        st.rerun()

    # Stop Quiz Button
    if st.button("Stop Quiz"):
        st.session_state.quiz_ended = True
        st.rerun()

else:
    st.header(f"🎉 Your final score is: {st.session_state.score}")
    st.markdown("Thank you for playing! 🎯")

# Footer
st.markdown("""
    <div class='footer'>
        🚀 Developed by <b>Areeba Yaseen</b> | Powered by 
        <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" 
             alt="Streamlit" width="100">
    </div>
""", unsafe_allow_html=True)
