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






"Hello"

#######################################################################
# HANA Conenctions
conn = py.connect(Trusted_Connection='yes', DRIVER='{IBM DB2 ODBC DRIVER}',SERVERNODE='phnhdb.dx.deere.com:30015')

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
