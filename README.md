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

# Prompt Playground

A Python command-line tool that connects to the OpenAI Chat Completions API. This project demonstrates foundational AI engineering practices, including environment setup, API key security, and systematic prompt engineering.

## Prerequisites
- Python 3.11+ (from python.org)
- VS Code or any code editor
- Git
- An OpenAI account and API key (platform.openai.com)

## Setup & Installation

Follow these exact steps to set up the project environment and run the script:

1. Clone or open your repository directory in your terminal.
2. Run the following commands to set up your virtual environment and install dependencies:

   python3 -m venv ai_env && source ai_env/bin/activate (Mac/Linux) or ai_env\Scripts\activate (Windows)
   pip install openai python-dotenv
   pip freeze > requirements.txt

3. Create a `.gitignore` file to ensure your secrets are not tracked by Git:
   
   Create a .gitignore file containing .env and ai_env/

4. Set up your environment variables:
   - Create a `.env` file in the root directory:
     OPENAI_API_KEY=your_actual_api_key_here
     (Note: Never commit this file to GitHub!)
   
   - Create a `.env.example` file in the root directory (this is safe to commit):
     OPENAI_API_KEY=your_openai_api_key_here

5. Create your Python script named `prompt_playground.py` and write your API call code.

## How to Run the Script
To run your script, make sure your virtual environment is active and execute:
python prompt_playground.py

---

## Prompt Experiments

Below is the documentation for the three prompt experiments conducted to evaluate how prompt structure, system instructions, and constraints affect LLM outputs.

### 🧪 Experiment 1: Vague vs. Specific Prompt
* Goal: Test the impact of context and formatting constraints on output quality.

#### Variant A (Vague Prompt)
* Prompt: 
  Tell me about solar panels.
* Output:
  Solar panels are devices that convert light into electricity. They are made of solar cells, which are typically made of silicon. When sunlight hits these cells, it creates an electric field, producing electricity. People install them on roofs to save money on energy bills and reduce their carbon footprint. They are growing in popularity worldwide.

#### Variant B (Specific Prompt)
* Prompt: 
  Explain how residential solar panels convert sunlight into electricity. Provide a clear, 3-step bulleted list suitable for a homeowner with no technical background. Keep the explanation simple and focus on the practical flow of energy.
* Output:
  Here is how solar panels power your home in three simple steps:
  
  1. Sunlight Capture: Your rooftop solar panels absorb sunlight using silicon cells. This light energy frees up electrons, creating a flow of direct current (DC) electricity.
  2. Power Conversion: Since homes run on alternating current (AC) electricity, a device called an inverter converts the raw DC electricity from your panels into usable AC power.
  3. Home Distribution: This converted electricity flows directly into your home's electrical panel to power your lights and appliances, with any excess power sent back to the local utility grid.

#### 📊 Comparison & Analysis
* Why Variant B is better: Variant A generated a generic, unstructured paragraph that was too brief and lacked clear focus. Variant B successfully applied three specific constraints: a target audience (non-technical homeowner), a specific structure (3-step bulleted list), and a clear scope (the flow of energy). This resulted in an easily readable, highly educational output that directly answered the user's practical needs.

---

### 🧪 Experiment 2: No System Prompt vs. System Prompt
* Goal: Test how defining a system persona shapes the model's behavior, tone, and explanation style.

#### Variant A (No System Prompt / Default)
* System Prompt: (None - default assistant behavior)
* User Prompt: 
  Explain recursion in programming.
* Output:
  Recursion is a programming technique where a function calls itself, either directly or indirectly, to solve a problem. To prevent infinite loops, a recursive function must have a base case (a condition that stops the recursion) and a recursive step (which reduces the problem toward the base case). For example, calculating factorials or traversing tree structures are common use cases.

#### Variant B (With Custom System Prompt)
* System Prompt: 
  You are a friendly, encouraging high school computer science teacher who uses fun food-related analogies to explain complex coding concepts.
* User Prompt: 
  Explain recursion in programming.
* Output:
  Hey there! Don't let the word "recursion" scare you—it's actually super cool! 
  
  Think of recursion like baking a giant, multi-layered cake using a recipe that says: "To make a 5-layer cake, make a 4-layer cake and add one layer." 
  
  To find out how to make that 4-layer cake, you have to look at the rule for a 3-layer cake, and so on. You keep going down until you reach the Base Case: a single, simple layer of cake (which you know how to bake instantly!). Once you bake that base layer, you can easily stack the next layer on top, all the way up until your beautiful 5-layer masterpiece is complete! In code, recursion is just a function calling a smaller version of itself until it hits that simple base step. You've got this!

#### 📊 Comparison & Analysis
* Why Variant B is better: Without a system prompt, Variant A returned a dry, academic definition that might intimidate a beginner. Variant B's system prompt successfully transformed the model's persona, adopting an encouraging tone and a highly creative analogy (the layered cake). This shows how system prompts are essential for aligning an AI's voice and pedagogical style with a specific user demographic.

---

### 🧪 Experiment 3: Opinion vs. Structured Analysis
* Goal: Test the model's ability to provide balanced, objective analysis instead of subjective opinions.

#### Variant A (Asking for an Opinion)
* Prompt: 
  Is remote work better than in-office work?
* Output:
  Yes, remote work is generally much better than in-office work. It eliminates long, stressful daily commutes, saves employees money on transportation and food, and allows for a much better work-life balance. Most workers report being happier and more productive when they have the flexibility to work from home.

#### Variant B (Asking for a Structured Analysis)
* Prompt: 
  Analyze the shift to remote and hybrid work. Provide a balanced breakdown of 2 pros and 2 cons for both employers and employees, followed by a summary of key success factors.
* Output:
  ### Remote & Hybrid Work Analysis
  
  #### For Employees
  * Pros:
    1. Flexibility & Time Savings: Eliminates commutes, returning hours back to the employee's day.
    2. Cost Reduction: Lowers personal spending on transit, professional wardrobe, and dining out.
  * Cons:
    1. Isolation: Potential for loneliness and reduced spontaneous social interaction.
    2. Work-Life Blur: Difficulty unplugging, leading to longer working hours and potential burnout.
  
  #### For Employers
  * Pros:
    1. Talent Pool Expansion: Ability to recruit globally rather than being limited by geography.
    2. Overhead Savings: Reduced real estate costs and office utility expenses.
  * Cons:
    1. Onboarding Challenges: Harder to assimilate new hires into company culture remotely.
    2. Communication Friction: Increased reliance on scheduled meetings rather than organic collaboration.
  
  #### Key Success Factors
  Successful hybrid setups rely on strong asynchronous communication documentation, clear objective-based performance tracking, and deliberate opportunities for team bonding.

#### 📊 Comparison & Analysis
* Why Variant B is better: Variant A resulted in a highly subjective, one-sided response that ignored the real organizational challenges of remote work. Variant B forced the model to evaluate the topic from multiple perspectives (both employers and employees) and detail both advantages and disadvantages. This structured prompt ensures the LLM delivers objective, comprehensive, and business-ready insights rather than simple generalizations.