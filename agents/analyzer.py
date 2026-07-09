from agents.gemini import ask_gemini

def analyze_code(code):

    prompt = f"""
You are an expert Python code reviewer.

Analyze the following Python code.

Provide:

1. Summary
2. Strengths
3. Bugs
4. Performance Issues
5. Security Issues
6. Best Practices
7. Code Quality Score out of 100

Code:

{code}
"""

    return ask_gemini(prompt)