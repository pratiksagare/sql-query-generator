import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_sql_query(schema: str, user_request: str) -> str:
    """
    Takes database schema and user natural language request,
    returns generated SQL query.
    """
    prompt = f"""
    You are an expert SQL generator.
    Given the following database schema:
    {schema}

    Write an SQL query for the user's request below.
    The query should be syntactically correct and efficient.
    Do not explain, only return SQL.

    User request: {user_request}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
