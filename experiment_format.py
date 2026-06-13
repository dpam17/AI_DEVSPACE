import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
user_input = input("List three primary colors: ")
system_prompt_a = "Respond in JSON format."
system_prompt_b = "Respond only with a raw JSON array of strings. Do not include any additional text, markdown formatting, or explanations."

def run_prompt(system_instruction, user_message):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        temperature = 0.0,
        
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_message}
        ]
    )
    
    return response.choices[0].message.content

print ("--- VARIANT A RESPONSE ---")
print (run_prompt(system_prompt_a, user_input))

print ("\n--- VARIANT B RESPONSE ---")
print (run_prompt(system_prompt_b, user_input))