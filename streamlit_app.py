import streamlit as st
from PIL import Image
import time

im = Image.open(rf"logo-round.png")
st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)

st.markdown(
    "<h1 style='text-align: center; color: black;'>Find Yourself Quiz</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<style>
div.stButton > button:first-child {
    size: 25px;           
    font-style: bold;
    padding: 12px 45px;
    min-width: 120px;       
    background-color:white;     
    color:black;               
    border: 2px solid black;  
    border-radius:10px;       
    cursor:pointer;
}
[data-testid="stSidebar"] h2 {
    font-size: 35px;
    font-weight: bold; 
}
[data-testid="stSidebar"] {
    background-color: #bdbababd;
}
div[data-testid="stMarkdownContainer"] > p strong {
    font-size: 25px;   
    display: inline-block; 
}
div[role="radiogroup"] > label {
    position: relative;
    padding-left: 30px; 
    margin-bottom: 4px;  
    font-size: 19px;
}    
div[role="radiogroup"] > label input[type="radio"] {
    position: absolute;
    left: 50%;        
    top: 50%;         
    transform: translate(-50%, -50%);
}
</style>
""", unsafe_allow_html=True)

quiz = [
    {
        "question": " What is your Gender?",
        "options": ["Male", "Female"]
    },
    {
        "question": " What is more related to you?",
        "options": [
        "work with nature",
        "work with people",
        "work with technics",
        "work with art",
        "work with symbols"
        ]
    },
    {
        "question": " Do you feel comfortable working in team?",
        "options": [
            "Yes, I love communication",
            "Mostly, but sometimes alone",
            "Sometimes, It depends",
            "Not Really, but would like to get some help",
            "No, I’d rather do it alone"
        ]
    },
    {
        "question": " Do you enjoy solving mathematical problems with computer?",
        "options": [
            "Yes, I do",
            "Mostly, but not good with computers",
            "Sometimes, It depends",
            "Not Really, but like technologies",
            "No, it’s not for me"
        ]
    },
    {
        "question": " Are you comfortable adapting quickly when things don't go as planned?",
        "options": [
            "Yes, I adapt fast and calm",
            "Mostly, but stress affects me",
            "Sometimes, It depends",
            "Not Really, but I good manage stress",
            "No, I prefer stable and predictable situation"
        ]
    },
    {
        "question": " Are you interested in learning how the human body or nature works?",
        "options": [
            "Yes, It's really interesting",
            "Mostly, but prefer help people",
            "Sometimes, It depends",
            "Not Really, but I'm a bit afraid of medical tools",
            "No, It's not mine"
        ]
    },
    {
        "question": " Do you usually understand what others feel and how to respond emotionally?",
        "options": [
            "Yes, I'm very sensitive",
            "Mostly, but hard to understand other",
            "Sometimes, It depends",
            "Not Really, but I understand people well",
            "No, I'm kinda robot"
        ]
    },
    {
        "question": " Do you enjoy analyzing markets, managing money, or running projects?",
        "options": [
            "Yes, It's really interests me",
            "Mostly, but I'm not good in math",
            "Sometimes, It depends",
            "Not Really, but I'm a good mathematician",
            "No, It's all hard for me"
        ]
    },
    {
        "question": " Do you often come up with new ideas and enjoy experimenting with them?",
        "options": [
            "Yes, I'm very creative",
            "Mostly, but not with new things",
            "Sometimes, It depends",
            "Not Really, but new stuff is mine passion",
            "No, I'm not that open-minded"
        ]
    },
    {
        "question": " Do you enjoy writing, learning languages, or exploring culture and history?",
        "options": [
            "Yes, It's very interesting",
            "Mostly, but I prefer learning languages only",
            "Sometimes, It depends",
            "Not Really, but I like exploring culture",
            "No, I don't enjoy writing or the past"
        ]
    },
    {
        "question": " Do you enjoy leading people and organizing processes or tasks?",
        "options": [
            "Yes, I love lead and being responsible",
            "Mostly, but I'm bad at managing tasks",
            "Sometimes, It depends",
            "Not Really, but I can manage tasks well",
            "No, I’d rather be a part of the machine"
        ]
    },
    {
        "question": " Do you like working with visuals, sounds, or building artistic things?",
        "options": [
            "Yes, I’m pretty creative in these areas",
            "Mostly, but hard in realization",
            "Sometimes, It depends",
            "Not Really, but I can bring others' ideas to life",
            "No, that’s absolutely not me"
        ]
    }
]

total_questions = len(quiz)

if "answers" not in st.session_state:
    st.session_state.answers = {q["question"]: None for q in quiz}

for i, q in enumerate(quiz, start=1):
    st.markdown(f"**{i}) {q['question']}**")
    current_answer = st.session_state.answers[q["question"]]

    choice = st.radio(
        "",
        q["options"],
        index=None if current_answer is None else q["options"].index(current_answer),
        key=f"q{i}" 
    )
    st.session_state.answers[q["question"]] = choice

st.sidebar.header("Progress")
progress_bar = st.sidebar.progress(0)
progress_text = st.sidebar.empty()

st.sidebar.markdown("**Questions:**")
for i, (question, ans) in enumerate(st.session_state.answers.items(), start=1):
    if ans is None:
        st.sidebar.markdown(f"**{i}) ❌ Not yet**")
    else:
        st.sidebar.markdown(f"**{i}) ✅ Answered**")

answered_count = sum(1 for v in st.session_state.answers.values() if v is not None)
progress = int((answered_count / total_questions) * 100)
progress_bar.progress(progress)
progress_text.write(f"Done: {answered_count}/{total_questions} ({progress}%)")

col1, col2, col3 = st.columns(3)
with col1:
    pass
with col2:
    center_button = st.button('**Submit**')
with col3:
    pass

placeholder = st.empty()
if center_button:
    if any(v is None for v in st.session_state.answers.values()):
        placeholder.warning("Please, answer all the questions!", icon="❌")
    else:
        st.session_state.submitted_answers = st.session_state.answers.copy()
        placeholder.success("Thank you for your answers!", icon="✅")

