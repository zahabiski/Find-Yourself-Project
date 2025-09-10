# ---------------------- IMPORTS ----------------------

import streamlit as st
from PIL import Image
import time

# ---------------------- PAGE CONFIG ----------------------

im = Image.open("logo-round.png")

st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)

# ---------------------- PAGE HEADER ----------------------

st.markdown(
    "<h1 style='text-align: center; color: black;'>Find Yourself Quiz</h1>",
    unsafe_allow_html=True
)

