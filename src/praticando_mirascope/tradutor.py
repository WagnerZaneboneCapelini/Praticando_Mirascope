from mirascope import llm


@llm.call(provider="google", model="gemini-2.0-flash")
def summarize(text: str) -> str:
    return f"Summarize this text: {text}"


@llm.call(provider="google", model="gemini-2.0-flash")
def translate(text: str, language: str) -> str:
    return f"Translate this text to {language}: {text}"


summary = summarize("Life is full of surprises. Every day brings new opportunities to learn, grow, and explore. No matter the challenges, there is always a chance to make things better. Stay positive, keep moving forward, and embrace the journey ahead!")
translation = translate(summary.content, "português")
print(translation.content)
