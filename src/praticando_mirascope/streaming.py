from mirascope import llm
import os


@llm.call(provider="google", model="gemini-2.0-flash", stream=True)
def stream_city_info(city: str) -> str:
    return f"Provide a brief description of {city}."


for chunk, _ in stream_city_info("Brasília"):
    print(chunk.content, end="", flush=True)
