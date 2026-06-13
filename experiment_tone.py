import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

user_input = "What is an API?"

# Variant A: A professional, clear educational persona
system_prompt_a = "You are a professional computer science teacher. Explain concepts clearly and simply."

# Variant B: A highly stylized, non-traditional persona
system_prompt_b = "You are a 17th-century pirate captain. Explain technical concepts using pirate slang and seafaring metaphors."

def run_prompt(system_instruction, user_message):
 response = client.chat.completions.create(
 model="gpt-4o-mini",
 temperature=0.7,
# Slightly higher temperature to allow for creative language
 messages=[
 {"role": "system", "content": system_instruction},
 {"role": "user", "content": user_message}
 ]
 )
 return response.choices[0].message.content

print("--- VARIANT A OUTPUT ---")
print(run_prompt(system_prompt_a, user_input))

print("\n--- VARIANT B OUTPUT ---")
print(run_prompt(system_prompt_b, user_input))
