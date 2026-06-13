import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# The user is asking an off-topic question to a supposed banking bot
user_input = "Who is the best football player in the world?"

# Variant A: A helpful assistant with no boundaries
system_prompt_a = "You are a helpful banking assistant."

# Variant B: A banking assistant with strict guardrails
system_prompt_b = (
 "You are a helpful banking assistant. You only answer questions related to personal finance, "
 "loans, and bank accounts. If a user asks an off-topic question, politely refuse to answer "
 "and remind them of your purpose."
)

def run_prompt(system_instruction, user_message):
 response = client.chat.completions.create(
 model="gpt-4o-mini",
 temperature=0.0,
# Temperature 0 ensures strict adherence to the rules
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
