#app.py
import streamlit as st
st.set_page_config(layout="wide")

import app1
#import app2
#import app3
#import app4
import numpy as np
import pandas as pd  #Used for Dataframe Creations
import pyodbc as py  #Used for Database Connections
#import openpyxl  # Used for Excel
#import sqlalchemy
import datetime
import webbrowser
import time

PAGES = {
    "Aftertreatment_Claim_Coding ": app1,

    
} 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
