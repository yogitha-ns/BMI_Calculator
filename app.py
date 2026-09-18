import streamlit as st


st.title('BMI Calculator')

# input the number
weight = st.number_input('Enter your weight in kilograms:',min_value=0.0,format='%.2f')

# height format selection
height_unit = st.radio('Select height unit:',['Centimeters','Meters','Feet'])

height = st.number_input(f"Enter your height in ({height_unit.lower()})",min_value=0.0,format='%.2f')

# calculate the BMI if the button is pressed
if st.button('Calculate BMI'):
    try:
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        # to prevent the error
        if height_m < 0:
            st.error('Please enter a valid height.')
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("You are Healthy")
        elif 25 <= bmi < 30:
            st.warning("You are Overweight")
        else:
            st.error("You are Extremely Overweight")

    except:
        st.error('Please enter a valid height.')
