
# app2.py
import streamlit as st
def app():
    st.title('APP2')
    st.write('Welcome to app2')
    col1,col2 = st.beta_columns([4,1])
    col1.success("First Column")
    col1.button("Hello")
    col2.success("Second COlumn")
    col2.button("Hello From Col2")
