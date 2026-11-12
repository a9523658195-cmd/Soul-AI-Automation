
import os
import time
from google import genai
from google.genai import types

def main():
    print("STEP 1: Starting Soul AI...", flush=True)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing!")

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
    Make the topic unique and engaging.
    """

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.5-flash-lite"
    ]

    response = None

    for model in models:
        try:
            print(f"Trying model: {model}", flush=True)

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            print(f"SUCCESS: {model}", flush=True)
            break

        except Exception as e:
            print(f"FAILED: {model} | {e}", flush=True)

            error_text = str(e)

            if "503" not in error_text and "UNAVAILABLE" not in error_text:
                raise

            time.sleep(2)

    if response is None:
        raise RuntimeError("All Gemini models are unavailable.")

    script = response.text or "No text returned"

    os.makedirs("output", exist_ok=True)

    with open("output/soul_ai_script.txt", "w", encoding="utf-8") as file:
        file.write(script)

    print("\n===== GENERATED SCRIPT =====", flush=True)
    print(script, flush=True)
    print("\nScript saved to output/soul_ai_script.txt", flush=True)
    print("\n===== SOUL AI COMPLETE =====", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("SOUL AI ERROR:", repr(e), flush=True)
        raise
