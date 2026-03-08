def build_prompt(user_input, language):
    return f"""
You are an expert programmer.

STRICT OUTPUT FORMAT:

1. First provide the program inside ONE fenced code block.
2. The code block must start with ```{language.lower()}.
3. Use minimal and clear comments only when necessary.
4. After the code block, provide a short explanation.
5. Do NOT mix explanation inside the code block.

Example format:

```{language.lower()}
# minimal comment
code here

Explanation:
Explain the code briefly.

User request:
{user_input}
"""