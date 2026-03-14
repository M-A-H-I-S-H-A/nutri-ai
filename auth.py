import streamlit as st
import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

def signup(username,password):

    cursor.execute(
        "INSERT INTO users VALUES (?,?)",
        (username,password)
    )
    conn.commit()

def login(username,password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    return cursor.fetchone()