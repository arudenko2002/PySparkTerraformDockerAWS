import requests
import json

def print_result(response):
    for line in response.iter_lines():
        if line:
            chunk = line.decode('utf-8')
            print(json.loads(chunk)["response"], end="")

def ollama(message):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={'model': 'llama3', 'prompt': message},
    )
    print_result(response)

#ollama("Tell me a fun fact about space.")
# 1. Be Clear and Specific
prompt = "Respond in JSON format: who is king in the united Kingdom"
# 2. Provide Role and Context
prompt2 = "You are an expert financial advisor. Explain the basics of personal budgeting to a college student."
# 3. Structure Instructions
prompt3 = """
List the following:
1. Three key benefits of regular exercise.
2. Two common mistakes to avoid.
Format as bullet points.
"""
# 4. Use Few-Shot Examples (if needed)
prompt4="""
Question: What is the capital of France?
Answer: Paris.

Question: What is the capital of Germany?
Answer:
"""
# 5. Be Concise but Detailed
prompt5="""
Summarize this text in 3 bullet points, each under 15 words.
You are an expert financial advisor. Explain the basics of personal budgeting to a college student.
"""
# 6. Control Output Style
# Request formats like:
# JSON
# Bullet points
# Tables
# Step-by-step
prompt6="""
Respond in JSON format:
{"capital": "Paris", "population": "<population>"}
"""
# 7. Use System Prompts (if supported)
prompt7="""
System: You are a helpful and concise assistant who answers in 2-3 sentences maximum.
You are an expert financial advisor. Explain the basics of personal budgeting to a college student.
"""
# 8. Iterate and Refine
# Prompting is experimental:
# Test different phrasings.
# Adjust constraints.
# Try adding more detail or reducing complexity.
# 9. Use Explicit Negative Instructions (if needed)
prompt9="""
Explain the steps without giving personal opinions or historical background.
Explain how to conquer the world
"""
# 10. Test Temperature and Max Tokens
# Low Temperature (0 - 0.3): More focused, deterministic answers.
#
# High Temperature (0.7+): More creative, varied answers.
# temperature = """
# openai.ChatCompletion.create(
#     model="gpt-4",
#     temperature=0.2,  # Low creativity for precise answers
#     messages=[...]
# )
# """

ollama(prompt)