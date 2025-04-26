from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
# this model dosent support structured output, so we need to add custom output parsers

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-3-27b-it",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

parser = JsonOutputParser()

template= PromptTemplate(
    template="Give me the name , age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    # additional instructions in the prompt
)

# prompt = template.format()

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# using chain
chain = template | model | parser

final_result = chain.invoke({})

print(final_result)
# print(type(final_result)) <class 'dict'>
