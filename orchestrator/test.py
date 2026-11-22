
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Load .env from project root
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY was not found in .env")


def generate_text(prompt: str) -> str:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        "models/gemini-3.5-flash-lite:generateContent"
    )

    http_response = requests.post(
        url,
        params={"key": API_KEY},
        json={
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        },
        timeout=60
    )

    print("HTTP Status:", http_response.status_code)

    # Raise an exception if the request failed
    if not http_response.ok:
        print("Error details:", http_response.text)

    http_response.raise_for_status()

    data = http_response.json()

    # Extract generated text
    return data["candidates"][0]["content"]["parts"][0]["text"]


if __name__ == "__main__":
    result = generate_text(
        "Give me three features for a music player."
    )

    print("\nGenerated response:")
    print(result)
