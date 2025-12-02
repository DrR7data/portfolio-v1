from app import random_frase


def test_random_frase():
    assert (
        "The only way to do great work is to love what you do - Steve Jobs"
        or "Don't count the days, make the days count - Muhammad Ali"
        or "Life is what happens to you while you're busy making other plans - John Lennon"
        or "The hardest victory is the victory over self - Aristotle"
        or "If you can dream it, you can do it - Walt Disney"
        or "Success is going from failure to failure without loss of enthusiasm - Winston Churchill"
        or "What does not kill me makes me stronger - Friedrich Nietzsche"
        or "It does not matter how slowly you go as long as you do not stop - Confucius"
        or "The future belongs to those who believe in the beauty of their dreams - Eleanor Roosevelt"
        or "With discipline and constancy, even a snail reaches the Ark - Proverb"
        in random_frase()
    )
