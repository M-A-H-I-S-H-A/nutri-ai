import streamlit as st
st.markdown(
"<h1 style='text-align:center;'> Vitamin AI Health Assistant</h1>",
unsafe_allow_html=True
)
st.markdown("""
<style>

/* GLOBAL APP BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #EAF4FF, #F7FBFF);
    font-family: 'Segoe UI', sans-serif;
}

/* REMOVE STREAMLIT HEADER */
header[data-testid="stHeader"] {
    background: transparent;
}

/* MAIN CONTAINER */
.block-container {
    padding-top: 2rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#DCEBFF,#F2F7FF);
    border-right: 1px solid #C7DFFF;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: #1F4E79 !important;
}

/* INPUT FIELDS */
.stTextInput input {
    background: white !important;
    border-radius: 12px;
    border: 1px solid #C5DBFF !important;
    padding: 10px;
    color: #1F2D3D !important;
}

/* PASSWORD FIELD */
.stTextInput div div input {
    background: white !important;
}

/* PASSWORD ICON AREA */
.stTextInput div div div {
    background: white !important;
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(135deg,#4AA9E2,#2E6FD8);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 22px;
    font-size: 16px;
    font-weight: 500;
    transition: 0.3s;
}

/* BUTTON HOVER */
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg,#2E6FD8,#1F4E79);
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: white !important;
    border-radius: 14px;
    border: 1px solid #DCEBFF;
}

/* DROP AREA */
[data-testid="stFileUploaderDropzone"] {
    background: #F2F7FF !important;
    border-radius: 14px;
}

/* CHAT INPUT */
[data-testid="stChatInput"] {
    background: white !important;
    border-radius: 14px;
    border: 1px solid #DCEBFF;
}

/* CHAT MESSAGE BUBBLE */
[data-testid="stChatMessage"] {
    background: white !important;
    border-radius: 14px;
    border: 1px solid #E0ECFF;
    padding: 10px;
}

/* SELECT BOX */
.stSelectbox div {
    background: white !important;
    border-radius: 10px;
}

/* CHAT HISTORY BADGE */
code {
    background: #EAF4FF !important;
    color: #1F4E79 !important;
    border-radius: 6px;
    padding: 3px 7px;
}

/* TITLES */
h1, h2, h3 {
    color: #1F4E79;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #C5DBFF;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* TITLE COLOR */
h1 {
    color: #2E86C1 !important;
}

/* SUBTITLE (Vitamin AI Health Assistant) */
h2, h3 {
    color: #2E86C1 !important;
}

/* LABELS: Username, Password */
label {
    color: #2E86C1 !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* FILE UPLOADER BUTTON (Browse files) */
[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg,#4AA9E2,#2E6FD8) !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
}

/* HOVER EFFECT */
[data-testid="stFileUploader"] button:hover {
    background: #2E6FD8 !important;
}

/* CHAT INPUT (Describe your symptoms) */
[data-testid="stChatInput"] textarea {
    background: white !important;
    color: #1F4E79 !important;
    border: 1px solid #C5DBFF !important;
    border-radius: 12px !important;
}

/* REMOVE DARK BAR BELOW */
[data-testid="stChatInput"] {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* REMOVE DARK BACKGROUND UNDER CHAT INPUT */
[data-testid="stBottomBlockContainer"] {
    background: transparent !important;
}

/* CHAT INPUT BAR */
[data-testid="stChatInput"] {
    background: white !important;
    border-radius: 12px !important;
    border: 1px solid #C5DBFF !important;
    padding: 6px;
}

/* CHAT INPUT TEXT FIELD */
[data-testid="stChatInput"] textarea {
    background: white !important;
    color: #1F4E79 !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* REMOVE DARK CHAT INPUT CONTAINER */
div[data-testid="stBottom"] {
    background-color: transparent !important;
}

/* REMOVE INNER DARK BLOCK */
div[data-testid="stBottom"] > div {
    background: transparent !important;
}

/* CHAT INPUT FIELD */
[data-testid="stChatInput"] {
    background: white !important;
    border: 1px solid #C5DBFF !important;
    border-radius: 14px !important;
}

/* TEXT AREA */
[data-testid="stChatInput"] textarea {
    background: white !important;
    color: #1F4E79 !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* USER MESSAGE TEXT */
[data-testid="stChatMessage"] p {
    color: #1F4E79 !important;
    font-weight: 500;
}

/* AI MESSAGE TEXT */
[data-testid="stChatMessage"] div {
    color: #1F4E79 !important;
}

/* ICON BOXES (user / bot icons) */
[data-testid="stChatMessage"] {
    background: #F2F7FF !important;
    border: 1px solid #DCEBFF !important;
    border-radius: 12px !important;
}

/* IMAGE MESSAGE TEXT FIX */
[data-testid="stChatMessage"] span {
    color: #1F4E79 !important;
}

</style>
""", unsafe_allow_html=True)
from auth import signup, login
from questionnaire import questionnaire
from chatbot import chatbot
import database

st.title("Vitamin AI")

# Sidebar menu for login/signup
menu = st.sidebar.selectbox(
    "Menu",
    ["Login", "Signup"]
)

# ---------------- SIGNUP ----------------
if menu == "Signup":

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Create account"):
        signup(username, password)
        st.success("Account created")

# ---------------- LOGIN ----------------
elif menu == "Login":

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login(username, password)

        if user:
            st.session_state["user"] = username
            st.success("Login successful")

        else:
            st.error("Invalid login")


# ---------------- AFTER LOGIN ----------------
if "user" in st.session_state:

    st.sidebar.write("Logged in as:", st.session_state["user"])

    # Default page
    if "page" not in st.session_state:
        st.session_state["page"] = "Questionnaire"

    # Navigation
    page = st.sidebar.selectbox(
        "Navigate",
        ["Questionnaire", "Chatbot"],
        index=["Questionnaire", "Chatbot"].index(st.session_state["page"])
    )

    st.session_state["page"] = page

    # Load pages
    if page == "Questionnaire":
        questionnaire(st.session_state["user"])

    elif page == "Chatbot":
        chatbot(st.session_state["user"])