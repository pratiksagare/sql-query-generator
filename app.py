import streamlit as st
from agent import generate_sql_query

st.set_page_config(page_title="AI SQL Query Generator", page_icon="🧠", layout="centered")

st.title("🧠 AI SQL Query Generator")
st.caption("Generate SQL queries from natural language using Gemini")

schema_input = st.text_area(
    "📋 Enter your database schema:",
    placeholder="Example:\n\nTable: users(id, name, email)\nTable: orders(id, user_id, amount, date)"
)

user_request = st.text_area(
    "💬 What query do you want to generate?",
    placeholder="Example: Get all users who have placed more than 5 orders."
)

if st.button("🔍 Generate SQL"):
    if not schema_input or not user_request:
        st.warning("Please enter both schema and your query request.")
    else:
        with st.spinner("Generating SQL query..."):
            query = generate_sql_query(schema_input, user_request)
        st.code(query, language="sql")
