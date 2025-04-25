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
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review"]
    summary:Annotated[str,"A brief summary of review"]
    sentiment:Annotated[Literal["pos","neg"],"Return sentiment of the review either negative , positive or neutral"]
    pros:Annotated[Optional[list[str]],"Return all the pros of the review"]
    cons:Annotated[Optional[list[str]],"Return all the cons of the review"]
    name:Annotated[Optional[list[str]],"Return the name of the reviewer"]


structured_model = model.with_structured_output(Review)

result=structured_model.invoke(
    """
The hardware is great , but the software feels bloated. There are too many pre-installed apps that i cant remove. Also , the ui looks outdated comapred to other brands. Hoping for a software fix."""
)
print(result)
print(result.summary)
print(result.sentiment)
