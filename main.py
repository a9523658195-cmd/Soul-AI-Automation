
import os
from google import genai
from google.genai import types

def main():
    print("STEP 1: Starting Soul AI...", flush=True)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing!")

    print("STEP 2: Connecting to Gemini...", flush=True)

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=45000)
    )

    prompt = """
    Create a 45-second Hindi YouTube Shorts script
    for Soul AI about how AI is changing daily life.

    Include:
    1. Catchy title
    2. Opening hook
    3. Hindi voiceover
    4. Scene-wise visual suggestions
    5. Ending CTA
    6. Hashtags

    Use simple conversational Hindi.
    """

    print("STEP 3: Sending prompt...", flush=True)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    print("\n===== GENERATED SCRIPT =====", flush=True)
    print(response.text, flush=True)
    print("\n===== COMPLETE =====", flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("SOUL AI ERROR:", repr(e), flush=True)
        raise
