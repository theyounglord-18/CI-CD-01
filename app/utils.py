import random

QUOTES = [
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency."
]

def get_random_quote():
    return random.choice(QUOTES)
