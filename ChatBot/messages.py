from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

import os
api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)\


message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="tell me about langchain")
]
result = model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)