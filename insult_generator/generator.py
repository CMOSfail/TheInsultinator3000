"""
Generates random insults using templates.
"""

import random
from insult_generator.templates import insult_templates

def generate_insult(name: str) -> str:
    """
    Generates a random insult by substituting the name into a template.

    Args:
        name: The name to be used in the insult.

    Returns:
        A formatted insult string.
    """
    template = random.choice(insult_templates)
    return template.format(name=name)