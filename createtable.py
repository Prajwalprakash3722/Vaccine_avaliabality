####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 13/03/2021
# Goal: To automate the vaccine availability slot
# licensed under MIT
# If you want to build the same app for feel free to fork it from my repo and make the necessary changes, But attriubution
# to the handle @Prajwalprakash3722 in GitHub is mandatory.
###################################################################################################################################################################
import streamlit as st
from main import *
from request import *
import pandas as pd
from pandas.core.frame import DataFrame
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
 

def create_table(args):
    
    if st.button("Show availability"):
        try:
            st.header("Keep this in mind this is a dummy data to show you the working.")
            data = sample_data(args)
            st.title("vaccination Availability")
            df = pd.DataFrame(data)
            st.dataframe(df)
        except:
             st.header("Enter Proper Value ?")