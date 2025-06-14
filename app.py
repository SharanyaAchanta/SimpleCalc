import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 == 0:
            st.error("Cannot divide by zero.")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")
