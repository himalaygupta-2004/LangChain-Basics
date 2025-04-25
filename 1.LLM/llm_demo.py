from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

result = llm.invoke("What is the capital of India?")
print(result.content) 