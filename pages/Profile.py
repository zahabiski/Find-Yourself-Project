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

st.expander("Hard Skills:", expanded=True)
st.expander("Soft Skills:", expanded=True)
st.expander("Overall Profile:", expanded=True)
