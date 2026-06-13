import os
from openai import OpenAI

client = OpenAI()

user_input = "Explain what a database is."

# We define three different system prompts to compare their outputs
experiments = {
 "Experiment 1 (No System Prompt)": "",
 "Experiment 2 (Persona - Pirate)": "You are a 17th-century pirate captain. Answer all questions in character.",
 "Experiment 3 (Strict Constraints)": "You are a technical writer. You must answer in exactly five words. Do not use punctuation."
}

# Loop through each experiment to send them to the API
for title, system_prompt in experiments.items():
	print(f"\n--- Running {title} ---")

	# We construct the messages list dynamically
	messages = []

	# Only add the system prompt if it is not empty
	if system_prompt:
		messages.append({"role": "system", "content": system_prompt})

	# Always add the user's input
	messages.append({"role": "user", "content": user_input})

	response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=messages,
		temperature=0.3
		# Lower temperature for more consistent, predictable results
	)

	print(response.choices[0].message.content)

# FILE: experiment.py