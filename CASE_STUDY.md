# Case Study: Controlling LLM Behavior via System Prompts

This case study documents how system prompts affect the output of the `gpt-4o-mini` model when answering the user query: *"Explain what a database is."*

#
# The Three Experiments

#
## Experiment 1: No System Prompt (Control)
* **System Prompt:** None
* **Observed Output:** A standard, polite, multi-paragraph explanation of a database. It used technical terms like "structured collection" and "tables."
* **Finding:** Without a system prompt, the AI defaults to a helpful, conversational, and verbose assistant. It does not optimize for any specific audience.

#
## Experiment 2: Persona-Driven Prompt
* **System Prompt:** `"You are a 17th-century pirate captain. Answer all questions in character."`
* **Observed Output:** The AI explained a database using pirate slang, comparing data to "buried treasure" and tables to "wooden chests."
* **Finding:** Personas completely change the vocabulary and tone of the response. The AI successfully mapped complex technical concepts to historical analogies.

#
## Experiment 3: Strict Constraints
* **System Prompt:** `"You are a technical writer. You must answer in exactly five words. Do not use punctuation."`
* **Observed Output:** A five-word response such as `Digital organized information storage system` with no period at the end.
* **Finding:** The AI can follow strict structural and formatting rules when they are explicitly declared in the system prompt.

#
# Core Prompting Principle: The Constraint First Rule

When building production applications, **always define what the AI must NOT do before defining what it should do.**

Negative constraints (such as "do not use punctuation" or "never mention competitor names") are the most effective way to prevent application errors. If you only tell the AI what to do, it will fill in the blanks with its default conversational behavior, which often breaks user interfaces designed for specific text lengths or formats.

# FILE: CASE_STUDY.md