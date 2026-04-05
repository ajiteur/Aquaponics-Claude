from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5",
    input="Explain the nitrogen cycle in aquaponics in 3 short bullet points."
)

print(response.output_text)