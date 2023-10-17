import streamlit as st


def calculate_wage(hours:float, rate:float)->float:
    return hours*rate

name = st.text_input('Please enter your name: ')
hours = st.number_input('Insert a number for hours ', step=0.5)
rate = st.number_input('Insert a number for rate ', step=1)
pay = calculate_wage(hours,rate)


if st.button('Calculate wage!'):
    st.write(f'{name} your wage is: ',pay)
    
    