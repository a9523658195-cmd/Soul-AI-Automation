
import os
from google import genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY secret is missing!")

    client = genai.Client(api_key=api_key)

    prompt = """
    You are an expert Hindi YouTube Shorts script writer
    for a technology channel called Soul AI.

    Create a viral 45-second YouTube Shorts script
    about: How AI is changing our daily lives.

    Write in simple conversational Hindi.

    Include:
    1. Catchy title
    2. Powerful opening hook
    3. Complete voiceover script
    4. Visual suggestions for each scene
    5. Strong ending and CTA
    6. Relevant hashtags
    """

    print("Connecting to Gemini AI...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    print("\n===== SOUL AI GENERATED SCRIPT =====\n")
    print(response.text)
    print("\n===== SCRIPT GENERATION COMPLETE =====")

if __name__ == "__main__":
    main()
