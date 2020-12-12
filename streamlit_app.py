#app.py
import streamlit as st
import app1
#import pyodbc as py  #Used for Database Connections
st.set_page_config(layout="wide")

PAGES = {
    "Aftertreatment_Claim_Coding ": app1,
} 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


# HANA Conenctions
#conn = py.connect(Trusted_Connection='yes', DRIVER='SQL Server',SERVERNODE='phnhdb.dx.deere.com:30015',User='rg41159',Password='IHOPEIGETMYPHDIN13YEARS')

#cnxn = py.connect('DRIVER="CData ODBC Driver for SAP HANA";User=system;Password="IHOPEIGETMYPHDIN13YEARS";SERVERNODE="phnhdb.dx.deere.com:30015"')
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
server = 30015
server = 'phnhdb.dx.deere.com' 
database = 'phnhdb' 
username = 'rg41159' 
password = 'IHOPEIGETMYPHDIN13YEARS' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
