import streamlit as st

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #2C5364, #203A43, #0F2027);
            color: white;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            background: #ff8c00;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #ffa500;
        }
        .result-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("🔢 Simple Calculator")
    st.write("Enter two numbers and choose an operation:")

    # Creating a styled card layout
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            num1 = st.number_input("Enter first number", value=0.0)

        with col2:
            num2 = st.number_input("Enter second number", value=0.0)

    operations = st.selectbox("Choose an operation", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

    if st.button("Calculate 🚀"):
        try:
            if operations == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operations == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operations == "Multiplication (*)":
                result = num1 * num2
                symbol = "×"
            else:
                if num2 == 0:
                    st.error("❌ Error: Division by Zero!")
                    return
                result = num1 / num2
                symbol = "÷"

            # Displaying the result in a stylish way
            st.markdown(f'<div class="result-card">{num1} {symbol} {num2} = {result}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Run the main function if the file is executed
if __name__ == "__main__":
    main()
