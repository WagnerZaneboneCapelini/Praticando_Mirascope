from mirascope import llm
import os


@llm.call(provider="google", model="gemini-2.0-flash")
def get_capital(country: str) -> str:
    return f"What is the capital of {country}?"


response = get_capital("Alemanha")
print(response.content)
