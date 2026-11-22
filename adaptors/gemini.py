import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
)

