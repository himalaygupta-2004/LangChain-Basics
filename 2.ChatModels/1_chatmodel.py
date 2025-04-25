from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
# Load the Google Generative AI model 
api_key = os.getenv("API_KEY")


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
result=model.invoke("Famous Open SourcE models ? give me only names")
print(result.content)