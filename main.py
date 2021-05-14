####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 13/03/2021
# Goal: To automate the vaccine availability slot
# licensed under MIT
# If you want to build the same app for feel free to fork it from my repo and make the necessary changes, But attriubution
# to the handle @Prajwalprakash3722 in GitHub is mandatory.
###################################################################################################################################################################
import streamlit as st
import regex as re
from request import *
from createtable import *


def app_header():
    st.warning("Try this with Indian_network service, COWIN-API's are geo-fenced")
    st.title("Covid-19 Vaccine appointment slot availability tracker. (Karnataka)")
    st.header(
        "You can select the following conditions and if any vaccine slots are avaliable will show!")
    st.subheader("Developed by Prajwal Prakash")


def main():
    left_column_1, right_column_1, right_column_2 = st.beta_columns(3)
    with left_column_1:
        user_pincode = st.text_input("Enter the Pincode(6 digits): ")
        if st.button("Verify Pincode"):
            st.markdown(get_pincode(user_pincode))
    create_table(user_pincode)
    with right_column_1:
        date_input = st.date_input("Enter the date:")
    with right_column_2:
        vaccine_name = st.selectbox('Select the vaccine: ', [
                                    'COVISHIELD', 'COWAXIN'])
        age = st.radio('Select Your age: ', ['18-44', '45+'])
    if age == '18-44':
        st.markdown(
            "The vaccination facility is suspended for the people of age 18-44 untill further notice by the Government of karnataka")
