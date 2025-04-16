from mirascope import llm
from pydantic import BaseModel


class Capital(BaseModel):
    city: str
    country: str


@llm.call(provider="google", model="gemini-2.0-flash", response_model=Capital)
def extract_capital(query: str) -> str:
    return f"{query}"


capital = extract_capital("The capital of France is Paris")
print(capital)
