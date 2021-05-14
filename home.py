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
from createtable import create_table

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

app_header()
main()
