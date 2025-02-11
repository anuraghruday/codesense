from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Database connection
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

class CodeRequest(BaseModel):
    code_snippet: str

@app.post("/analyze")
def analyze_code(request: CodeRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI code reviewer. Provide feedback and improvements."},
                {"role": "user", "content": request.code_snippet}
            ]
        )
        review = response["choices"][0]["message"]["content"]
        return {"review": review}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))