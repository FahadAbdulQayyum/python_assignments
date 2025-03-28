# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes
import streamlit as st

def main() -> None:
    st.title("BMI Calculator")
    weight = st.number_input("Enter your weight (in kgs)", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height (in meters)", min_value=0.0, step=0.01)
    
    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.write(f"Your BMI is {bmi:.2f}")
        else:
            st.error("Height must be greater than 0!")

if __name__ == '__main__':
    main()






# import streamlit as st

# def main() -> None:
#     st.title("BMI Calculator")
#     weight = st.number_input("Enter your weight (in kgs)")
#     height = st.number_input("Enter your height (in meters)")
#     bmi = weight / (height ** 2)
#     st.write(f"Your BMI is {bmi}")

# if __name__ == '__main__':

#     main()