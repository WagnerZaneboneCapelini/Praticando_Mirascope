from mirascope import Messages, llm
from pydantic import BaseModel
import json


@llm.call(provider="google", model="gemini-2.0-flash", json_mode=True)
def city_info(city: str) -> str:
    return f"Provide information about {city} in JSON format"


response = city_info("Tokyo")
print(response.content)  # This will be a JSON-formatted string
