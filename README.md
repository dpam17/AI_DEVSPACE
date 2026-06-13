# Prompt Playground

A Python command-line tool that lets you test how different system prompts change the responses of an AI model.

#
# Prerequisites

Before you begin, make sure you have the following installed:
* Python 3.11 or higher
* pip (Python's package installer)

#
# Installation

Follow these steps to set up the project on your computer:

1. Clone this repository to your local machine:
 ```bash
 git clone https://github.com/dpam17/AI_DEVSPACE
# adapt to match your project repository URL
 cd prompt-playground


<!-- FILE: README.md -->

> **Pitfall:** Many beginners forget to tell users to activate the virtual environment before running `pip install`. If you do not activate the environment, Python will install the libraries globally on your computer. This can cause version conflicts with other projects. Always list the activation command clearly before the installation command.

> **Check:** Open your terminal, navigate to your project folder, and run the commands exactly as written in your README. If the virtual environment activates and the `openai` library installs without errors, your instructions are correct.

#
## Explaining Configuration and Usage

Now that the user has installed the code, they need to know how to configure their API key and run the command-line tool.

1. Add a new section header for Configuration.
2. Explain how to set the `OPENAI_API_KEY` environment variable.
3. Add a Usage section showing the exact terminal command to run your Python script.

```markdown
#
# Configuration

This project requires an OpenAI API key to communicate with the AI. You must set this key as an environment variable.

On macOS and Linux:
```bash
export OPENAI_API_KEY="your-actual-api-key-here"
# sets the environment variable for your current session

<!-- FILE: README.md -->

> **Pitfall:** Hardcoding (writing sensitive data directly into your source code) your API key in your Python script is a major security risk. If you upload your code to GitHub, bots will steal your key within seconds. Always instruct users to use environment variables instead of pasting keys directly into the code.

> **Check:** Try running your script without setting the environment variable. It should fail with a clear error. Then, set the variable and run it again. It should succeed.

#
## Writing the Prompting Case Study

The core value of this project is understanding how different system prompts change the AI's behavior. This section documents your three experiments so others can see your findings immediately.

1. Create a Case Study section in your README.
2. Document Experiment 1 (e.g., a pirate assistant) showing the system prompt, user input, and the AI's output.
3. Document Experiment 2 (e.g., forcing a specific output format like JSON).
4. Document Experiment 3 (e.g., a Socratic tutor that guides instead of answering).
5. Summarize what these experiments teach us about prompt engineering.

```markdown
#
# Prompt Engineering Case Study

We conducted three experiments to observe how changing the **system prompt** (the core instructions that guide the AI's persona) alters the output.

#
## Experiment 1: The Pirate Translator
* **Goal:** Force the AI to adopt a specific persona and vocabulary.
* **System Prompt:** `You are a grumpy 17th-century pirate captain. Respond to all questions in pirate slang.`
* **User Input:** `How do I write a loop in Python?`
* **AI Response:** `Arrr! Ye want to spin a wheel, do ye? To run a loop in Python, ye use the "for" keyword to sail through your list, like so: "for item in crew:"! Keep yer eyes on the deck or ye'll walk the plank!`

#
## Experiment 2: The Strict JSON Formatter
* **Goal:** Force the AI to return data in a structured format instead of conversational text.
* **System Prompt:** `You are a data extractor. You must only respond with a valid JSON object containing "city" and "population" keys. Do not write any conversational text.`
* **User Input:** `I live in Tokyo, which has about 14 million people.`
* **AI Response:** `{"city": "Tokyo", "population": 14000000}`

#
## Experiment 3: The Socratic Tutor
* **Goal:** Prevent the AI from giving direct answers, forcing it to guide the user instead.
* **System Prompt:** `You are a Socratic tutor. Never give the user the direct answer. Instead, ask helpful questions that guide them to find the answer themselves.`
* **User Input:** `What is 15 times 12?`
* **AI Response:** `Let us break this down. What is 15 times 10? Once you have that, what is 15 times 2? How might we combine those two numbers?`

#
## Key Takeaways
1. **Personas Work:** The AI adopts complex personas instantly when instructed in the system prompt.
2. **Format Control is Possible:** You can suppress conversational filler by explicitly telling the AI to return only data formats like JSON.
3. **Behavioral Constraints:** System prompts can completely change how an AI solves problems, transforming it from an answer-engine into a tutor.