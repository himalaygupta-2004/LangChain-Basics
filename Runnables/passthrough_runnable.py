from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence,RunnablePassthrough
from typing import Literal
import os

load_dotenv()

api_key =os.getenv("API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)


parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write the explanation following joke - {topic}',
    input_variables=['topic']
)

joke_chain = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_chain,parallel_chain)

print(final_chain.invoke({'topic':'Bikes'}))