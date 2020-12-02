#app.py
import streamlit as st
st.set_page_config(layout="wide")

import app1
import app2
import app3
import app4
import streamlit as st
import numpy as np
import pandas as pd  #Used for Dataframe Creations
import pyodbc as py  #Used for Database Connections
import openpyxl  # Used for Excel
import datetime
import streamlit as st
import webbrowser
import time

PAGES = {
    "Aftertreatment_Claim_Coding ": app1,
    "CI_Claim_Coding": app2,
    "ECN_Tracking": app3,
    "D60": app4,
    
} 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

