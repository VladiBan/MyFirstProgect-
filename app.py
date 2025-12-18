import streamlit as st 
st.title("My First progect or smth type shi")
name = st.text_input(" What is your name")
if name:
  st.write(f"Hello, {name}")
