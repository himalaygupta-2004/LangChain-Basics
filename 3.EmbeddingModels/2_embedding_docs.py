from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", 
    google_api_key=api_key         
)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of france"
]

# Embed a query
result = embeddings.embed_documents(documents)
print(str(result))