# app1.py
import streamlit as st
def app():
    st.title('Yoshita')
    st.markdown("<h1 style='text-align: left; color: red;'>Welcome to Streamlit</h1>", unsafe_allow_html=True)
    st.write('Welcome to app1')

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
