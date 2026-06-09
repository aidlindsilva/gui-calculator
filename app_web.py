import streamlit as st

# Configure the web page layout
st.set_page_config(page_title="Streamlit Web Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Web-Based Calculator")
st.write("A clean, responsive web calculator built entirely in Python using Streamlit.")

# Initialize web session state to track the active calculation string
if "expression" not in st.session_state:
    st.session_state.expression = ""

# A helper function to safely process button clicks
def append_character(char):
    if char == "C":
        st.session_state.expression = ""
    elif char == "=":
        try:
            # Evaluate the mathematical string safely
            result = str(eval(st.session_state.expression))
            st.session_state.expression = result
        except ZeroDivisionError:
            st.error("Error: Cannot divide by zero")
            st.session_state.expression = ""
        except Exception:
            st.error("Error: Invalid Expression")
            st.session_state.expression = ""
    else:
        st.session_state.expression += str(char)

# 1. Display Screen (Read-Only text input acting as our screen)
st.text_input(
    label="Calculator Display", 
    value=st.session_state.expression, 
    disabled=True, 
    label_visibility="collapsed"
)

# 2. Grid Layout Structure using Streamlit Columns
# Defining the button configuration
buttons = [
    ['C', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

# Generate rows and columns dynamically on the webpage
for row in buttons:
    cols = st.columns(4) # Create 4 horizontal columns
    for index, button_label in enumerate(row):
        if button_label == '':
            continue
        # Render a button inside the specific column slot
        if cols[index].button(button_label, use_container_width=True):
            append_character(button_label)
            st.rerun() # Refresh the web app state instantly to display the change