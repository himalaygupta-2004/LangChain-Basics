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

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


joke_chain = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
    # 'word_count':RunnableLambda(lamda X:len(x.split()))
})

final_Chain= RunnableSequence(joke_chain,parallel_chain)

result = final_Chain.invoke({'topic':'cricket'})

final_res = """{} \n word count - {} """.format(result['joke'], result['word_count'])

print(final_res)


