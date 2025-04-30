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
    template = 'Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500 ,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence( report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))

