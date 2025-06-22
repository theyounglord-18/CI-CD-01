from app.utils import get_random_quote

def test_quote_returned():
    quote = get_random_quote()
    assert quote in [
        "Stay hungry, stay foolish.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Simplicity is the soul of efficiency."
    ]
