#app.py
import streamlit as st
import app1
import pyodbc as py  #Used for Database Connections
import pandas as pd
st.set_page_config(layout="wide")

PAGES = {
    "Aftertreatment_Claim_Coding ": app1,
} 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#SQL Connections
conn1 = py.connect('Driver={SQL Server};'
                      'Server=FSDERGSQL1.SDE.DEERE.COM;'
                      'Database=JDPS_941_SALES_DB;'
                      'Trusted_Connection=yes;')


