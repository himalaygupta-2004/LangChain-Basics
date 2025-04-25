from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", 
    google_api_key=api_key         
)

# Embed a query
result = embeddings.embed_query("Delhi is the capital of India")
print(str(result))