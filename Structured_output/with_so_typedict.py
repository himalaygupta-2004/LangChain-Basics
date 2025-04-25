from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import TypedDict,Annotated,Optional,Literal
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review")
    summary: str = Field(description="A brief summary of review")
    sentiment:Literal["pos","neg"]=Field(description="A brief summary of review")
    pros:Optional[list[str]]=Field(description="Return all the pros of the review")
    cons:Optional[list[str]]=Field(description="Return all the pros of the review")
    name:Optional[str]=Field(description="Return the name of the reviewer")

structured_model = model.with_structured_output(Review)

result=structured_model.invoke(
    """
The hardware is great , but the software feels bloated. There are too many pre-installed apps that i cant remove. Also , the ui looks outdated comapred to other brands. Hoping for a software fix."""
)
print(result)
print(result.summary)
print(result.sentiment)
