# app4.py

######################################################################
# Import Libraries
import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd  #Used for Dataframe Creations
import pyodbc as py  #Used for Database Connections
import openpyxl  # Used for Excel
import datetime
import streamlit as st
import webbrowser
import time
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
#st.set_page_config(layout="wide")
#######################################################################


#######################################################################
# HANA Conenctions
conn = py.connect(Trusted_Connection='yes', DRIVER='{HDBODBC}',SERVERNODE='phnhdb.dx.deere.com:30015')

#SQL Connections
conn1 = py.connect('Driver={SQL Server};'
                      'Server=FSDERGSQL1.SDE.DEERE.COM;'
                      'Database=JDPS_941_SALES_DB;'
                      'Trusted_Connection=yes;')

#SQL Connections
conn2 = py.connect('Driver={SQL Server};'
                      'Server=wdx2ua3031cmp\sqlexpress;'
                      'Database=JDPS_990_AFTERTREATMENT;'
                      'Trusted_Connection=yes;')
#######################################################################

#######################################################################
#Definition for APP4
def app():
    now = datetime.datetime.now()
    #st.write("""Current date and time :""", now)
    st.title('Welcome to D60')
    #st.write('Welcome to ECN Tracking')
    #st.button("Refresh Data") #This button refreshes the Data

    #col1 = st.beta_columns(1) #Establish the number of columns
    

#######################################################################


    df = pd.read_excel(r"C:\Users\rg41159\Tableau\JIMTEST.xlsx")
    st.write("Link to Power Points [link](http://share-internal.deere.com/teams/engineeringservices/First%20Pass%20Yield/Forms/AllItems.aspx?RootFolder=%2Fteams%2Fengineeringservices%2FFirst%20Pass%20Yield%2FCommon%20Errors%20Presentation%2FCAD%20Doc%20Error%20Power%20Points&FolderCTID=0x01200021788B50296C3B408F5A92EA35CDEA62&View=%7B5B76CD76%2D9A93%2D4080%2DA4C5%2D9FF7DFF1363D%7D)")

    ECNS = df['Engineer'].unique() #Unique list of ECNs
    ECNS_SELECTED = st.sidebar.multiselect('Select Engineer', ECNS) #Store ECN Choice made by user
    state_data = df[df['Engineer'].isin(ECNS_SELECTED)]
    st.write(state_data)
    
    ECNS2 = df['Supervisor/Group'].unique() #Unique list of ECNs
    ECNS_SELECTED2 = st.sidebar.multiselect('Select Manager', ECNS2) #Store ECN Choice made by user
    state_data2 = df[df['Supervisor/Group'].isin(ECNS_SELECTED2)]
    st.write(state_data2)
    
