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
import streamlit.components.v1 as components

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

app_header()
main()
st.markdown(
    "Any Issues, Just tweet it and mention me, I'll try my best to address them")
components.html("""<a href="https://twitter.com/intent/tweet?screen_name=prakash_prajwal&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-lang="en" data-show-count="false">Tweet to @prakash_prajwal</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>""")
