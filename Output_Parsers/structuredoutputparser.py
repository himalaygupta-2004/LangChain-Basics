from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os

load_dotenv()
api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)


schema = [
    ResponseSchema(name='fact_1',description="fact 1 about the topic"),
    ResponseSchema(name='fact_2',description="fact 2 about the topic"),
    ResponseSchema(name='fact_3',description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about the topic {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# chain = template | model  | parser

prompt =  template.invoke(template)

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)





