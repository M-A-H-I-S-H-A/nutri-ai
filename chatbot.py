import streamlit as st
import sqlite3
from PIL import Image
from ai_engine import analyze_health

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()


def chatbot(username):

    st.title("Vitamin AI Chatbot")

    # ======================
    # SIDEBAR MEDICAL PROFILE
    # ======================

    st.sidebar.header("Medical Profile")

    cursor.execute(
        "SELECT * FROM medical_history WHERE username=?",
        (username,)
    )

    profile = cursor.fetchone()

    if profile:
        st.sidebar.write("Name:", profile[1])
        st.sidebar.write("Age:", profile[2])
        st.sidebar.write("Sex:", profile[3])
        st.sidebar.write("Occupation:", profile[4])
    else:
        st.sidebar.write("No medical profile saved.")

    # ======================
    # SIDEBAR CHAT HISTORY
    # ======================

    st.sidebar.header("Chat History")

    cursor.execute(
        "SELECT message,response FROM chats WHERE username=?",
        (username,)
    )

    chats = cursor.fetchall()

    for chat in chats:
        st.sidebar.write("🧑", chat[0])
        st.sidebar.write("🤖", chat[1])
        st.sidebar.write("---")

    # ======================
    # MAIN CHAT AREA
    # ======================

    st.subheader("Ask about your symptoms or upload an image")

    uploaded_image = st.file_uploader(
        "Upload image (tongue, skin, nails, eyes)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image")

    user_input = st.chat_input("Describe your symptoms")

    # ======================
    # PROCESS CHAT
    # ======================

    if user_input or uploaded_image:

        message = user_input if user_input else "User uploaded an image"

        cursor.execute(
            "SELECT * FROM medical_history WHERE username=?",
            (username,)
        )

        profile = cursor.fetchone()

        # Image observation logic
        analysis_text = ""

        if uploaded_image:
            analysis_text = """
User uploaded a skin image showing white patches.
Possible indicators:
- Vitamin B12 deficiency
- Vitamin D deficiency
- Skin depigmentation
"""

        prompt = f"""
Medical profile:
{profile}

Symptoms:
{user_input}

Image observations:
{analysis_text}

Based on this information suggest possible vitamin deficiencies and advice.
"""

        response = analyze_health(profile, prompt)

        # Show messages in chat
        st.chat_message("user").write(message)

        if uploaded_image:
            st.image(img)

        st.chat_message("assistant").write(response)

        # Save chat
        cursor.execute(
            "INSERT INTO chats VALUES (?,?,?)",
            (username, message, response)
        )

        conn.commit()