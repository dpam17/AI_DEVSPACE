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

   ```bash
   python3 -m venv ai_env && source ai_env/bin/activate  # Mac/Linux
   # or
   ai_env\Scripts\activate  # Windows
   pip install openai python-dotenv
   pip freeze > requirements.txt
   ```

3. Create a `.gitignore` file to ensure your secrets are not tracked by Git:

   ```
   .env
   ai_env/
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```
     > ⚠️ **Never commit this file to GitHub!**

   - Create a `.env.example` file in the root directory (this is safe to commit):
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. Create your Python script named `prompt_playground.py` and write your API call code.

## How to Run the Script

Make sure your virtual environment is active, then execute:

```bash
python prompt_playground.py
```

---

## Configuration

This project requires an OpenAI API key to communicate with the AI. You must set this key as an environment variable.

On macOS and Linux:
```bash
export OPENAI_API_KEY="your-actual-api-key-here"
```

> **Pitfall:** Hardcoding your API key directly into your Python script is a major security risk. If you upload your code to GitHub, bots will steal your key within seconds. Always use environment variables instead.

> **Check:** Try running your script without setting the environment variable — it should fail with a clear error. Then set the variable and run again. It should succeed.

---

## 🧪 Prompt Engineering Experiments

### Experiment 1: Vague vs. Specific Prompting

**Objective:** Test the impact of prompt specificity and context on output quality.

**Variant A (Vague):**
> "Tell me about solar panels."

**Variant B (Specific):**
> "Explain how residential solar panels convert sunlight into electricity. Provide a clear, 3-step bulleted list suitable for a homeowner with no technical background. Keep the explanation simple and focus on the practical flow of energy."

**Variant A Output:**
> Solar panels are devices that convert light into electricity. They are made of solar cells, which are typically made of silicon. When sunlight hits these cells, it creates an electric field, producing electricity. People install them on roofs to save money on energy bills and reduce their carbon footprint. They are growing in popularity worldwide.

**Variant B Output:**
> Here is how solar panels power your home in three simple steps:
>
> 1. **Sunlight Capture:** Your rooftop solar panels absorb sunlight using silicon cells. This light energy frees up electrons, creating a flow of direct current (DC) electricity.
> 2. **Power Conversion:** Since homes run on alternating current (AC) electricity, a device called an inverter converts the raw DC electricity from your panels into usable AC power.
> 3. **Home Distribution:** This converted electricity flows directly into your home's electrical panel to power your lights and appliances, with any excess power sent back to the local utility grid.

**Analysis & Comparison:**
Variant A returned a generic, unstructured paragraph with no clear focus or audience. Variant B applied three explicit constraints — a target audience (non-technical homeowner), a fixed structure (3-step list), and a defined scope (energy flow only) — which forced the model to produce output that was both organized and immediately actionable. The added specificity didn't just improve style; it changed the information architecture of the entire response.

---

### Experiment 2: No System Prompt vs. Role-Defined System Prompt

**Objective:** Test how a system prompt influences the assistant's behavior and persona.

**Variant A (No System Prompt / Default):**
- *System:* None (default assistant behavior)
- *User:* "Explain recursion in programming."

**Variant B (With System Prompt):**
- *System:* "You are a friendly, encouraging high school computer science teacher who uses fun food-related analogies to explain complex coding concepts."
- *User:* "Explain recursion in programming."

**Variant A Output:**
> Recursion is a programming technique where a function calls itself, either directly or indirectly, to solve a problem. To prevent infinite loops, a recursive function must have a base case (a condition that stops the recursion) and a recursive step (which reduces the problem toward the base case). For example, calculating factorials or traversing tree structures are common use cases.

**Variant B Output:**
> Hey there! Don't let the word "recursion" scare you — it's actually super cool!
>
> Think of recursion like baking a giant, multi-layered cake using a recipe that says: "To make a 5-layer cake, make a 4-layer cake and add one layer."
>
> To find out how to make that 4-layer cake, you have to look at the rule for a 3-layer cake, and so on. You keep going down until you reach the **Base Case**: a single, simple layer of cake (which you know how to bake instantly!). Once you bake that base layer, you can easily stack the next layer on top, all the way up until your beautiful 5-layer masterpiece is complete! In code, recursion is just a function calling a smaller version of itself until it hits that simple base step. You've got this!

**Analysis & Comparison:**
Without a system prompt, the model defaulted to a dry, technically accurate definition that assumes prior familiarity — fine for a developer, alienating for a beginner. The system prompt in Variant B didn't just change tone; it changed the entire explanatory strategy, producing a concrete analogy (layered cake) that maps directly onto how recursion actually works. This demonstrates that system prompts shape *how* a model reasons about explanation, not just *how* it sounds.

---

### Experiment 3: Opinion-Based vs. Structured Analysis

**Objective:** Test how prompting for structured analysis versus a simple opinion influences reasoning quality.

**Variant A (Opinion-Based):**
> "Is remote work better than in-office work?"

**Variant B (Structured Analysis):**
> "Analyze the shift to remote and hybrid work. Provide a balanced breakdown of 2 pros and 2 cons for both employers and employees, followed by a summary of key success factors."

**Variant A Output:**
> Yes, remote work is generally much better than in-office work. It eliminates long, stressful daily commutes, saves employees money on transportation and food, and allows for a much better work-life balance. Most workers report being happier and more productive when they have the flexibility to work from home.

**Variant B Output:**
> ### Remote & Hybrid Work Analysis
>
> #### For Employees
> - **Pros:**
>   1. Flexibility & Time Savings: Eliminates commutes, returning hours back to the employee's day.
>   2. Cost Reduction: Lowers personal spending on transit, professional wardrobe, and dining out.
> - **Cons:**
>   1. Isolation: Potential for loneliness and reduced spontaneous social interaction.
>   2. Work-Life Blur: Difficulty unplugging, leading to longer working hours and potential burnout.
>
> #### For Employers
> - **Pros:**
>   1. Talent Pool Expansion: Ability to recruit globally rather than being limited by geography.
>   2. Overhead Savings: Reduced real estate costs and office utility expenses.
> - **Cons:**
>   1. Onboarding Challenges: Harder to assimilate new hires into company culture remotely.
>   2. Communication Friction: Increased reliance on scheduled meetings rather than organic collaboration.
>
> #### Key Success Factors
> Successful hybrid setups rely on strong asynchronous communication documentation, clear objective-based performance tracking, and deliberate opportunities for team bonding.

**Analysis & Comparison:**
Variant A produced a confident, one-sided answer — the model picked a side and ignored organizational complexity entirely. Variant B's structural constraints forced multi-perspective reasoning: the model couldn't give a clean "winner" because the prompt required it to fill boxes on both sides. This reveals a core prompt engineering principle — opinion-framed questions invite bias, while format-constrained prompts impose analytical discipline.

---

## Key Takeaways

1. **Specificity drives quality:** Vague prompts produce vague outputs. Constraints around audience, format, and scope are not restrictions — they are instructions the model actually needs.
2. **System prompts change reasoning, not just tone:** A well-defined persona alters how the model structures an explanation, not just how it sounds.
3. **Format constraints prevent bias:** Asking for opinions invites one-sided answers. Asking for structured analysis forces the model to reason from multiple perspectives before concluding.