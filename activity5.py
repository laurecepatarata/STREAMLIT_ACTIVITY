import pandas as pd
import streamlit as st
import sqlite3

# Set page config
st.set_page_config(
    page_title="📚 Student Records",
    layout="centered",
    page_icon="🧑‍🎓"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f7fbff;
    }
    </style>
""", unsafe_allow_html=True)

# Connect to SQLite
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")
conn.commit()

# Title
st.title("🧑‍🎓 Student Record Manager")
st.markdown("Add new students and view your saved records below.")

# Form layout
with st.form("student_form", clear_on_submit=True):
    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", min_value=1, max_value=120)
    submitted = st.form_submit_button("➕ Add Student")

    if submitted:
        if name.strip() == "":
            st.warning("⚠️ Please enter a valid name.")
        else:
            cursor.execute("INSERT INTO students VALUES (?, ?)", (name.strip(), age))
            conn.commit()
            st.success(f"✅ Added {name} (Age {age}) to the database.")

# Divider
st.markdown("---")

# Display records
st.subheader("📋 Current Student Records")

students = cursor.execute("SELECT rowid, * FROM students").fetchall()

if students:
    st.dataframe(
        pd.DataFrame(students, columns=["ID", "Name", "Age"]),
        use_container_width=True
    )
else:
    st.info("No records found. Start adding students above! 🎓")
