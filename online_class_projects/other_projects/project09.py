## Project 9: Build a Python Website in 15 Minutes With Streamlit

import streamlit as st

# Set page config (this must be the first Streamlit command)
st.set_page_config(page_title="My Website", page_icon="🌐", layout="wide")

def main():
    st.title("Welcome to My Website!")
    st.write("This is a simple website built with Streamlit in 15 minutes.")
    st.write("Use the sidebar to navigate between pages.")

    # Add some interactivity
    st.subheader("Quick Poll")
    like = st.radio("Do you like this website?", ("Yes", "No", "Maybe"))
    if st.button("Submit"):
        st.write(f"You selected: {like}")

if __name__ == "__main__":
    main()