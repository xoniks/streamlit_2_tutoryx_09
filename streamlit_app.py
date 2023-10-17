import streamlit as st


def calculate_wage(hours:float, rate:float)->float:
    return hours*rate

name = st.text_input('Please enter your name: ')
hours = st.number_input('Insert a number for hours ')
rate = st.number_input('Insert a number for rate ')
pay = calculate_wage(hours,rate)


if st.button('Calculate wage!'):
    st.write(f'{name} your wage is: ',pay)
    
    