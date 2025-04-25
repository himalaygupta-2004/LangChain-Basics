from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

api_key = os.getenv("API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", 
    google_api_key=api_key         
)

documents = ["Virat Kohli is known for its aggressive batting and leadership",
             "Ms Dhoni is a former Indian captiain Famous for his calm behaviour",
             "Sachin Tendulkar is regarded as one of the greatest batsmen in cricket history",
             "Rohit Sharma is the current captain of the Indian cricket team and known for his explosive batting style",
             "Brian Lara is a legendary West Indian cricketer known for his exceptional batting skills"]

query = "tell me about Virat Kohli"

doc_embedding = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]
index , score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])

print("similarity score is : ",score)