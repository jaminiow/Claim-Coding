#app.py
import streamlit as st
import app1
import pyodbc as py  #Used for Database Connections
st.set_page_config(layout="wide")

PAGES = {
    "Aftertreatment_Claim_Coding ": app1,
} 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


#SQL Connections
conn2 = py.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=wdx2ua3031cmp\sqlexpress;'
                      'Database=JDPS_990_AFTERTREATMENT;'
                      'Trusted_Connection=yes;')
