import streamlit as st
import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

def questionnaire(username):

    st.title("Medical Questionnaire")

    name = st.text_input("Name")
    age = st.number_input("Age")

    sex = st.radio(
        "Sex",
        ["Male","Female","Other"]
    )

    occupation = st.text_input("Occupation")

    st.subheader("Current Medical Conditions")

    conditions = st.multiselect(
        "Diagnosed Conditions",
        [
        "None",
        "Diabetes",
        "Hypertension",
        "Thyroid disorder",
        "Depression/Anxiety",
        "Other"
        ]
    )

    pregnancy = st.radio(
        "Pregnancy Status",
        ["No","Pregnant","Breastfeeding"]
    )

    st.subheader("Past Medical History")

    past_history = st.multiselect(
        "Previous Diagnoses",
        [
        "Iron deficiency anemia",
        "Vitamin B12 deficiency",
        "Vitamin D deficiency",
        "Thyroid disorder",
        "Diabetes",
        "PCOS",
        "Gastrointestinal disorder",
        "Liver disease",
        "Kidney disease",
        "None"
        ]
    )

    surgery = st.text_input(
        "Major surgery (if any)"
    )

    family_history = st.multiselect(
        "Family History",
        [
        "Diabetes",
        "Thyroid disorder",
        "Hypertension",
        "Heart problems",
        "None"
        ]
    )

    st.subheader("Lifestyle")

    activity = st.selectbox(
        "Physical Activity",
        ["Sedentary","Light","Moderate","Intense"]
    )

    sunlight = st.selectbox(
        "Sunlight exposure",
        ["<15 minutes","15–30 minutes",">30 minutes"]
    )

    sleep = st.selectbox(
        "Sleep duration",
        ["<5 hours","5–6 hours","7–8 hours",">8 hours"]
    )

    stress = st.selectbox(
        "Stress level",
        ["Low","Moderate","High"]
    )

    smoking = st.selectbox(
        "Smoking",
        ["Never","Occasional","Regular"]
    )

    alcohol = st.selectbox(
        "Alcohol consumption",
        ["Never","Occasional","Weekly","Frequent"]
    )

    st.subheader("Diet")

    diet = st.radio(
        "Diet type",
        ["Vegan","Vegetarian","Eggetarian","Non-vegetarian"]
    )

    water = st.selectbox(
        "Water intake",
        ["<1L","1-2L",">2L"]
    )

    medication = st.text_area(
        "Current medications"
    )
    if st.button("Save Medical Profile"):
        cursor.execute("""
    INSERT INTO medical_history VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        username,
        name,
        age,
        sex,
        occupation,
        str(conditions),
        pregnancy,
        str(past_history),
        surgery,
        str(family_history),
        activity,
        sunlight,
        sleep,
        stress,
        smoking,
        alcohol,
        diet,
        water,
        medication
    ))

    conn.commit()

    st.success("Medical profile saved")

    # Move user to chatbot
    st.session_state["page"] = "Chatbot"
    st.rerun()