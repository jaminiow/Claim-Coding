# app3.py

######################################################################
# Import Libraries
#import streamlit as st
#import streamlit as st
#import numpy as np
#import pandas as pd  #Used for Dataframe Creations
import pyodbc as py  #Used for Database Connections
#import openpyxl  # Used for Excel
#import datetime
#import streamlit as st
#import webbrowser
#import time
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
#Definition for APP3
def app():
    now = datetime.datetime.now()
    #st.write("""Current date and time :""", now)
    st.title('Welcome to ECN Tracking')
    #st.write('Welcome to ECN Tracking')
    #st.button("Refresh Data") #This button refreshes the Data

    #col1 = st.beta_columns(1) #Establish the number of columns

    

#######################################################################



#Read in Data from CA_PARTNUMBER Table from Hana

    def loadpartnumber(): # Hana: Run Query on CA_WORKFLOW_1
        st.write('loadpartnumber')
        HANA_PARTNUMBER_df = pd.read_sql('''

            Select 
            ECN AS PDMLINK_ECN,        
            ECNSTATE AS PDMLINK_ECNSTATE,  
            REVISION AS PDMLINK_REV,
            PART_STATE AS PDMLINK_PARTSTATE,
            DESIGNCONTROL AS PDMLINK_DesignControl,
            PART_NUMBER as PNC
    

            From _SYS_BIC."deere.pdm.analytics.model/CA_PARTNUMBER"

            WHERE
            DESIGNCONTROL LIKE '%D0%'
            AND
            LATEST_REV_IND = 'X'

         


            '''
            , conn)
        return HANA_PARTNUMBER_df

    def loadpartnumber2(): # Hana: Run Query on CA_WORKFLOW_1
        st.write('loadpartnumber')
        HANA_PARTNUMBER2_df = pd.read_sql('''

            Select 
            ECN AS PDMLINK_ECN,     
            COUNT(PART_NUMBER) as PNC
        
            From _SYS_BIC."deere.pdm.analytics.model/CA_PARTNUMBER"

            WHERE
            DESIGNCONTROL LIKE '%D0%'
            AND
            LATEST_REV_IND = 'X'

            GROUP BY  ECN


         


            '''
            , conn)
        return HANA_PARTNUMBER2_df

#######################################################################

    def loadworkflow1(): # Hana: Run Query on CA_WORKFLOW_1
        st.write('LOADWORKFLOW')
        HANA_WORKFLOW1_df = pd.read_sql('''
        
            Select 
            MATNR AS Material,
            DOKTL AS NWBC_Rev,
            PLPDP_TASK_ECM AS NWBC_ECM,
            PLPDP_PHASE_NAME_GROUP AS NWBC_PhaseName,
            PLPDP_PROJECT_SYSTEM_STATUS AS NWBC_ProjectSystemStatus,
            PLPDP_PHASE_SYSTEM_STATUS AS NWBC_PhaseSystemStatus,
            PLPDP_NUMBER AS NWBC_ProjectNumber


            From _SYS_BIC."deere.pdm.analytics.model/CA_WORKFLOW_1"

            WHERE 
            PLPDP_PROJECT_SYSTEM_STATUS = 'Released'
            AND
            PLPDP_PHASE_SYSTEM_STATUS = 'Released'
            AND
            PLPDP_NUMBER LIKE 'D000%'

            '''
            , conn)
        return HANA_WORKFLOW1_df
    
 
    res = loadworkflow1()
    res2 = loadpartnumber()
    res3 = loadpartnumber2()
    user_input = (st.sidebar.text_input("Enter ECN and Press Enter",))
    
  

        
    #if st.button('Show dataframe'):
        #res = loadworkflow1()
        #ecnlist = res['NWBC_ECM'].tolist()
        #species = st.selectbox('Show iris per variety?', ecnlist)
        #st.write(species)
        #st.write(res)
        #filteredres = filters(res)


    if st.button('Show Summary'):


        
        #st.balloons()
        with st.spinner('Wait for it...'):
            new_df = res[res['NWBC_ECM'] == user_input]
            st.write('NWBC Summary for :', user_input)
            st.write(new_df)

            new_df1 = res2[res2['PDMLINK_ECN'] == user_input]
            st.write('PDMLINK Summary for :', user_input)
            st.write(new_df1)

            new_df2 = res3[res3['PDMLINK_ECN'] == user_input]
            st.write('PDMLINK Summary for :', user_input)
            st.write(new_df2)


            
        st.balloons()
        st.success('Done!')
        


    
   

             
        
        
#######################################################################

    
                          

    
    

    


    #my_expander = st.beta_expander("JIM TEST")
    #with my_expander:
        #'Hello there!'
        #clicked = st.button('Click me!')
        #select_status = st.radio("Covid-19 patient's status", ('Confirmed',
        #'Active', 'Recovered', 'Deceased'))
        #select_statusS = st.radio("Covid-19 patient's status", ('Confirmed'))

#######################################################################
# Setup Sidebar for filtering
    #st.sidebar.title("ECN Data")
    
    #ECNS = HANA_PARTNUMBER_df['PDMLINK_ECN'].unique() #Unique list of ECNs
    #ECNS_SELECTED = st.sidebar.multiselect('Select ECNS', ECNS) #Store ECN Choice made by user

    #PARTS = HANA_PARTNUMBER_df['PART_NUMBER'].unique() #Unique list of PARTS
    #PARTS_SELECTED = st.sidebar.multiselect('Select PARTS', PARTS) #Store PARTS Choice made by user

# Mask to filter dataframe
    #mask_ECNS = HANA_PARTNUMBER_df['PDMLINK_ECN'].isin(ECNS_SELECTED)
    #HANA_PARTNUMBER_df = HANA_PARTNUMBER_df[mask_ECNS]

    #mask_PARTS = HANA_PARTNUMBER_df['PART_NUMBER'].isin(PARTS_SELECTED)
    #HANA_PARTNUMBER_df = HANA_PARTNUMBER_df[mask_PARTS]
    #df_filtered = (df[msk1 & msk2 & msk3 & msk4])["CPM"]

    #st.sidebar.checkbox("Show Analysis by State", True, key=1)
    #select = st.sidebar.selectbox('Select a State',HANA_WORKFLOW1_df['NWBC_ECM'])

    #title = st.text_input('Movie title', 'Life of Brian')
    #st.write('The current movie title is', title)

    #number = st.number_input('Insert a number')
    #st.write('The current number is ', number)

#get the state selected in the selectbox


    #ECNS = HANA_WORKFLOW1_df['NWBC_ECM'].unique() #Unique list of ECNs
    #ECNS_SELECTED = st.sidebar.multiselect('Select ECNS', ECNS) #Store ECN Choice made by user
    #state_data = HANA_WORKFLOW1_df[HANA_WORKFLOW1_df['NWBC_ECM'].isin(ECNS_SELECTED)
    
    #select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed',
    #'Active', 'Recovered', 'Deceased'))
    #mask_ECNS = HANA_PARTNUMBER_df['PDMLINK_ECN'].isin(ECNS_SELECTED)
    #HANA_PARTNUMBER_df = HANA_PARTNUMBER_df[mask_ECNS]
#######################################################################

#######################################################################
# Setup Sidebar for filtering
    #st.sidebar.title("ECN Data")
    #ECNS = HANA_WORKFLOW1_df['NWBC_ECM'].unique() #Unique list of ECNs
    #ECNS_SELECTED = st.sidebar.multiselect('Select ECNS', ECNS) #Store ECN Choice made by user
    #mask_ECNS = HANA_WORKFLOW1_df['NWBC_ECM'].isin(ECNS_SELECTED)
    #HANA_WORKFLOW1_df = HANA_WORKFLOW1_df[mask_ECNS]
    #st.sidebar.checkbox("Show Analysis by State", True, key=1)
    #select = st.sidebar.selectbox('Select a ECN',HANA_WORKFLOW1_df['NWBC_ECM'])

#get the state selected in the selectbox
    #state_data = HANA_WORKFLOW1_df[HANA_WORKFLOW1_df['NWBC_ECM'] == select]



    
    #HANA_WORKFLOW1_df = HANA_WORKFLOW1_df['NWBC_ECM'].isin(select)


# Create a list of possible values and multiselect menu with them in it.
    #ECNS = HANA_WORKFLOW1_df['NWBC_ECM'].unique()
    #ECNS_SELECTED = st.sidebar.multiselect('Select ECNS', ECNS)

# Mask to filter dataframe
    #mask_ECNS = HANA_WORKFLOW1_df['NWBC_ECM'].isin(ECNS_SELECTED)

    #HANA_WORKFLOW1_df = HANA_WORKFLOW1_df[mask_ECNS]
#######################################################################
