from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

import os
api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

prompt = PromptTemplate(
    template='Generate a 5 line summary on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({'topic':'virat kohli'})
print(result)

chain.get_graph().print_ascii()