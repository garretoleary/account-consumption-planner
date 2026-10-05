import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import APIConnectionError, OpenAI


env_path = Path(__file__).resolve().with_name(".env")
load_dotenv(env_path)

if not os.environ.get("OPENAI_API_KEY"):
    print("ERROR: OPENAI_API_KEY was not found in .env.", file=sys.stderr)
    raise SystemExit(2)

try:
    response = OpenAI().responses.create(
        model="gpt-6-astra",
        input="hello",
    )
except APIConnectionError:
    print("ERROR: The OpenAI API network connection is blocked or unavailable.", file=sys.stderr)
    raise SystemExit(3)

print(response.output_text)
