from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_frase():
    """Returns random frase"""

    frases = (
        "The only way to do great work is to love what you do - Steve Jobs",
        "Don't count the days, make the days count - Muhammad Ali",
        "Life is what happens to you while you're busy making other plans - John Lennon",
        "The hardest victory is the victory over self - Aristotle",
        "If you can dream it, you can do it - Walt Disney",
        "Success is going from failure to failure without loss of enthusiasm - Winston Churchill",
        "What does not kill me makes me stronger - Friedrich Nietzsche",
        "It does not matter how slowly you go as long as you do not stop - Confucius",
        "The future belongs to those who believe in the beauty of their dreams - Eleanor Roosevelt",
        "With discipline and constancy, even a snail reaches the Ark - Proverb",
    )
    return choices(frases)


@app.route("/")
def frase():
    """Return random frase"""

    my_frase = random_frase()
    return render_template("index.html", title="Random frases", frase=my_frase)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
