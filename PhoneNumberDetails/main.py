import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import streamlit as st
import random
import time

# Set Page Configuration
st.set_page_config(page_title="Phone Number Info", page_icon="📱", layout="centered")

# Custom CSS for Styling - Dark & Light Mode Compatible
st.markdown(
    """
    <style>
       @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    h1 {
        font-size: 40px;
        font-weight: bold;
        color: #ff5733;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
        text-shadow: 2px 2px 10px rgba(255, 87, 51, 0.3);
    }
    
    .info-box {
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 6px solid #ff9800;
        font-weight: bold;
        transition: transform 0.3s ease-in-out;
    }
    
    .info-box:hover {
        transform: scale(1.05);
    }
    
    @media (prefers-color-scheme: light) {
        .info-box {
            background-color: #fff3cd;
            color: #333;
        }
    }
    
    @media (prefers-color-scheme: dark) {
        .info-box {
            background-color: #333;
            color: #ffcc00;
            border-left: 6px solid #ffcc00;
        }
    }
  
    .custom-button {
        background: linear-gradient(to right, #ff5e62, #ff9966);
        color: white;
        padding: 12px 25px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        display: block;
    }
    .custom-button:hover {
        background: linear-gradient(to right, #ff9966, #ff5e62);
        transform: scale(1.07);
        box-shadow: 0 5px 20px rgba(255, 87, 51, 0.4);
    }

    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 20px;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with animation
st.markdown("<h1 class='title'>📱 Phone Number Details Lookup</h1>", unsafe_allow_html=True)

# Random fact generator
def get_random_fact():
    facts = [
        "📌 The first smartphone was invented in 1992 by IBM, called 'Simon'!",
        "📌 The world's first touchscreen phone was released in 1992, not the iPhone!",
        "📌 Over 5 billion people worldwide own a mobile phone!",
        "📌 The first-ever camera phone was released in 1999 in Japan!",
        "📌 Mobile phones have more computing power than the Apollo 11 spacecraft!",
    ]
    return random.choice(facts)

# AI-based phone number type prediction
def predict_number_type(phone):
    if phone.startswith("+1") or phone.startswith("+44") or phone.startswith("+61"):
        return "📞 Business Number (Mostly Used for Official Work)"
    elif phone.startswith("+92") or phone.startswith("+91"):
        return "📱 Personal Number (Mostly Used for Social & Daily Use)"
    elif "000" in phone:
        return "⚠️ High Risk! Possible Spam or Fake Number"
    else:
        return "🔍 Unknown Type (Could be Personal or Business)"

# User input field with animation
number = st.text_input("🔢 Enter your phone number with country code (e.g., +923001234567):")
find_details = st.markdown('<button class="custom-button">🔍 Find Details</button>', unsafe_allow_html=True)
if number or find_details:
    with st.spinner("🔍 Searching for details..."):
        time.sleep(2)  # Simulating delay
    
    try:
        phone = phonenumbers.parse(number)
        time_zones = timezone.time_zones_for_number(phone)
        sim_carrier = carrier.name_for_number(phone, "en")
        region = geocoder.description_for_number(phone, "en")
        is_valid = phonenumbers.is_valid_number(phone)
        is_possible = phonenumbers.is_possible_number(phone)
        num_type = phonenumbers.number_type(phone)
        phone_fact = get_random_fact()
        predicted_type = predict_number_type(number)

        num_type_text = {
            phonenumbers.PhoneNumberType.MOBILE: "📱 Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "☎️ Landline",
            phonenumbers.PhoneNumberType.TOLL_FREE: "📞 Toll-Free",
        }.get(num_type, "❓ Unknown")

        st.markdown("<h3 style='color:#007bff;'>📊 Phone Number Details:</h3>", unsafe_allow_html=True)
        
        st.markdown(f"<div class='info-box'>📌 <b>Parsed Number:</b> {phone}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>⏰ <b>Time Zone:</b> {time_zones}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>📡 <b>SIM Provider:</b> {sim_carrier if sim_carrier else 'Unknown'}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>🌍 <b>Registered Region:</b> {region}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>✅ <b>Valid Number:</b> {'Yes' if is_valid else 'No'}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>🔢 <b>Possible Number:</b> {'Yes' if is_possible else 'No'}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>📊 <b>Number Type:</b> {num_type_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>🤖 <b>AI Prediction:</b> {predicted_type}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>💡 <b>Did You Know?</b> {phone_fact}</div>", unsafe_allow_html=True)

    except phonenumbers.NumberParseException:
        st.error("❌ Invalid phone number format! Please enter a correct phone number.")

# Footer with animation
st.markdown("<div class='footer'>🚀 Developed by Areeba Yaseen | Powered by Streamlit</div>", unsafe_allow_html=True)
