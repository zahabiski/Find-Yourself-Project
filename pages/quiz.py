# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
import requests
import time
# ---------------------- PAGE CONFIG ----------------------
im = Image.open("logo-round.png")
st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)
# ---------------------- QUIZ DATA ----------------------
quiz = [
    {"question": " What is your Gender?", "options": ["Male", "Female"]},
    {"question": " What is more related to you?", "options": ["work with nature","work with people","work with technics","work with art","work with symbols"]},
    {"question": " Do you feel comfortable working in team?", "options": ["Yes, I love communication","Mostly, but sometimes alone","Sometimes, It depends","Not Really, but would like to get some help","No, I’d rather do it alone"]},
    {"question": " Do you enjoy solving mathematical and computer problems?", "options": ["Yes, I do","Mostly, but not good with computers","Sometimes, It depends","Not Really, but like technologies","No, it’s not for me"]},
    {"question": " Are you comfortable adapting quickly when things don't go as planned?", "options": ["Yes, I adapt fast and calm","Mostly, but stress affects me","Sometimes, It depends","Not Really, but I good manage stress","No, I prefer stable and predictable situation"]},
    {"question": " Are you interested in learning how the human body and nature works?", "options": ["Yes, It's really interesting","Mostly, but prefer help people","Sometimes, It depends","Not Really, but I'm a bit afraid of medical tools","No, It's not mine"]},
    {"question": " Do you usually understand what others feel and how to respond emotionally?", "options": ["Yes, I'm very sensitive","Mostly, but hard to understand other","Sometimes, It depends","Not Really, but I understand people well","No, I'm kinda robot"]},
    {"question": " Do you enjoy managing finances and running projects?", "options": ["Yes, It's really interests me","Mostly, but I'm not good in math","Sometimes, It depends","Not Really, but I'm a good mathematician","No, It's all hard for me"]},
    {"question": " Do you often come up with new ideas and enjoy experimenting with them?", "options": ["Yes, I'm very creative","Mostly, but not with new things","Sometimes, It depends","Not Really, but new stuff is mine passion","No, I'm not that open-minded"]},
    {"question": " Do you enjoy learning languages, exploring culture and history?", "options": ["Yes, It's very interesting","Mostly, but I prefer learning languages only","Sometimes, It depends","Not Really, but I like exploring culture","No, I don't enjoy writing or the past"]},
    {"question": " Do you enjoy leading people and organizing processes?", "options": ["Yes, I love lead and being responsible","Mostly, but I'm bad at managing tasks","Sometimes, It depends","Not Really, but I can manage tasks well","No, I’d rather be a part of the machine"]},
    {"question": " Do you like working with visuals, sounds and building artistic things?", "options": ["Yes, I’m pretty creative in these areas","Mostly, but hard in realization","Sometimes, It depends","Not Really, but I can bring others' ideas to life","No, that’s absolutely not me"]}
]
# ---------------------- QUIZ LOGIC ---------------------- 
total_questions = len(quiz) # Initialization of cycle 
if "answers" not in st.session_state: 
    st.session_state.answers = {q["question"]: None for q in quiz}
# ---------------------- PROGRESS BAR ----------------------
progress_container = st.container()
# ---------------------- PAGE HEADER ----------------------
st.markdown("<h1 style='text-align: center; color: black;'>Find Yourself Quiz</h1>", unsafe_allow_html=True)
# ---------------------- SHOW QUIZ ---------------------- 
for i, q in enumerate(quiz, start=1): 
    key = f"q{i}" 
    if key not in st.session_state: 
        st.session_state[key] = None 
    st.markdown(f"**{i}) {q['question']}**") 
    st.radio( "", q["options"], key=key )
    
for i, q in enumerate(quiz, start=1): 
    st.session_state.answers[q["question"]] = st.session_state.get(f"q{i}")
with progress_container:
    st.markdown('<div class="progress-bar-container">', unsafe_allow_html=True)
    answered = sum(1 for a in st.session_state.answers.values() if a is not None)
    progress = answered / len(quiz)
    st.markdown("<h3>Progress</h3>", unsafe_allow_html=True)
    st.progress(progress)
    st.write(f"Done: {answered}/{len(quiz)}")
    st.markdown('</div>', unsafe_allow_html=True)
# ---------------------- SUBMIT SECTION ----------------------
st.write("")
st.write("")
st.write("")
st.write("")
col1, col2, col3 = st.columns(3)
with col1: pass
with col2: center_button = st.button('**Submit**')    # Centers the submit button
with col3: pass
placeholder = st.empty()
if center_button:
    if any(v is None for v in st.session_state.answers.values()):
        placeholder.warning("Please, answer all the questions!", icon="❌")
    else:
        submitted_answers = st.session_state.answers.copy()    # copies the answers to work with (dict. format)
        pailor = {"promt":f"{submitted_answers}"}
        response = requests.post(
            "https://69ba1845b520.ngrok-free.app/check_data",
            json=pailor
        )
        print(modelresponce.json()["response"])
        placeholder.success("Thank you for your answers!", icon="✅")
        st.switch_page("pages/profile.py")
st.markdown("""
        <style>
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
            .stAlert {
                animation: fadeOut 6s ease;
            }
        </style>
    """, unsafe_allow_html=True)
time.sleep(6)
placeholder.empty()
# ---------------------- CUSTOM STYLES ----------------------
st.markdown("""
<style>
/* Button Submit */
div.stButton > button:first-child {
    size: 25px;           
    font-style: bold;
    padding: 12px 45px;
    min-width: 120px;       
    background-color: white;     
    color: black;               
    border: 2px solid black;  
    border-radius: 10px;       
    cursor: pointer;
}
/* BG */
[data-testid="stSidebar"] {
    background-color: #bdbababd;
}
/* Questions */
div[data-testid="stMarkdownContainer"] > p strong {
    font-size: 25px;   
    display: inline-block;
}
/* Padding */
div[role="radiogroup"] {
    margin-top: -25px;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
/*Progress Bar*/
.progress-bar-container {
  position: fixed; 
  top: 0;
  z-index: 1000;
}
</style>
""", unsafe_allow_html=True)
