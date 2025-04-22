import streamlit as st
import random

if 'is_number_include' not in st.session_state:
    st.session_state['is_number_include'] = False
if 'is_special_include' not in st.session_state:
    st.session_state['is_special_include'] = False
if 'is_uppercase_include' not in st.session_state:
    st.session_state['is_uppercase_include'] = False
if 'value_till' not in st.session_state:
    st.session_state['value_till'] = 8

with st.container():
    def set_password():
        password:str = ""
        included_chars = "abcdefghijklmnopqrstuvwxyz"
        upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_chars = "!@#$%^&*(_+=-)"
        number_chars = "0123456789"
        if st.session_state['is_uppercase_include']:
            included_chars+=upper_chars
            password+= random.choice(upper_chars)  
        if st.session_state['is_special_include']:
            included_chars+=special_chars
            password+= random.choice(special_chars)  
        if st.session_state['is_number_include']:
            included_chars+=number_chars
            password+= random.choice(number_chars)
        while len(password) < st.session_state['value_till']:
            password += random.choice(included_chars)
        st.code(body=password,language = 'plaintext')


    st.slider(min_value=8,max_value=16,key='value_till',on_change=set_password,label="slider")
    st.checkbox("Numbers",key='is_number_include',on_change=set_password)
    st.checkbox("Uppercase",key='is_uppercase_include',on_change=set_password)
    st.checkbox("Special Characters",key='is_special_include',on_change=set_password)
