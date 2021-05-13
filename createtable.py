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
 

def create_table():

    if st.button("Show avaliabality"):

        data = [{
            "center_id": 1234,
            "name": "District General Hostpital",
            "address": "45 M G Road",
            "state_name": "Maharashtra",
            "district_name": "Satara",
            "block_name": "Jaoli",
            "pincode": "413608",
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "fee": "250",
            "date": "31-05-2021",
            "available_capacity": 50,
            "available_capacity_dose1": 25,
            "available_capacity_dose2": 25,
            "min_age_limit": 18,
            "vaccine": "COVISHIELD",
        }
        ]

        st.title("vaccination Avaliabality")
        df = pd.DataFrame(data)
        st.dataframe(df)
