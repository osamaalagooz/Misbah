""" Prompt to generate the response to the question in a conversational way
```
Question: {question}
Answer: {answer}

Rewrite the answer to the question in a conversational way.
```

"""

from .base import Prompt


class GenerateResponsePrompt(Prompt):
    """Prompt to generate the response to the question in a conversational way"""

    text: str = """
Question: {question}
Answer: {answer}
Generated Code : {code}

Rewrite the answer to the question in a conversational way and add a summerized explanation for the answer depending on the generated code.
"""
