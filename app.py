import streamlit as st
from PIL import Image

# ---------------- NAVIGATION ----------------
pages = {
    "Main": [
        st.Page("quiz_app.py", title="Quiz"),
        st.Page("pages/profile.py", title="Profile"),
    ]
}

pg = st.navigation(pages, position="top")
pg.run()

# ---------------- PAGE CONFIG ----------------
im = Image.open("logo-round.png")
st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)
