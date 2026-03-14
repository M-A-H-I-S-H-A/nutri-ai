import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS medical_history(
username TEXT,
name TEXT,
age TEXT,
sex TEXT,
occupation TEXT,
conditions TEXT,
pregnancy TEXT,
past_history TEXT,
surgery TEXT,
family_history TEXT,
activity TEXT,
sunlight TEXT,
sleep TEXT,
stress TEXT,
smoking TEXT,
alcohol TEXT,
diet TEXT,
water TEXT,
medication TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
username TEXT,
message TEXT,
response TEXT
)
""")

conn.commit()