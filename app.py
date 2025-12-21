from flask import Flask
from flask import jsonify
from flask import render_template
from random import choices

app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1,5,10,25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


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
        "La primera riqueza es la salud - Ralph Waldo Emerson",
        "Cuida tu cuerpo; es el único lugar que tienes para vivir - Jim Rohn",
        "La salud no lo es todo, pero sin ella todo lo demás es nada - Arthur Schopenhauer",
        "Mantener el cuerpo en buena salud es un deber… de lo contrario no podremos mantener nuestra mente fuerte y clara - Buda",
        "La felicidad radica, ante todo, en la salud - George William Curtis",
        "La buena salud y el buen juicio son dos bendiciones de la vida - Publilio Siro",
        "El cuerpo logra lo que la mente cree - Napoleon Hill",
        "La salud es la mayor posesión; la alegría es el mayor tesoro - Lao-Tsé",
        "La prevención es mejor que la cura - Desiderius Erasmus",
        "El ejercicio es la llave para una vida saludable y feliz - Henry David Thoreau",
        "La energía y la persistencia conquistan todas las cosas - Benjamin Franklin",
        "La fuerza no proviene de la capacidad física, sino de una voluntad indomable - Mahatma Gandhi",
        "La calma es la cuna del poder - Josiah Gilbert Holland",
        "Cada ser humano es el autor de su propia salud o enfermedad - Buda",
        "La salud de la mente es la verdadera salud - Séneca",
        "La alegría es la mejor medicina - Proverbio",
        "Quien tiene salud tiene esperanza, y quien tiene esperanza lo tiene todo - Proverbio árabe",
        "La mejor y más eficiente farmacia está dentro de tu propio sistema - Robert C. Peale",
        "El bienestar no es un destino, es un camino - Wayne Dyer",
        "Tu salud es una inversión, no un gasto - Anónimo",
    )
    return choices(frases)


@app.route("/")
def frase():
    """Return random frase"""

    my_frase = random_frase()
    return render_template("index.html", title="Random frases", frase=my_frase)
@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)
    
    
@app.route('/100/change/<dollar>/<cents>')
def change100route(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    amount100 = float(amount) * 100
    print(f"This is the {amount} X 100")
    result = change(amount100)
    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
