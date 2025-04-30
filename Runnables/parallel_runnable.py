from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence
from typing import Literal
import os

load_dotenv()

api_key =os.getenv("API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)


parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a linkedin post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'AI'})
print(result['linkedin'])


