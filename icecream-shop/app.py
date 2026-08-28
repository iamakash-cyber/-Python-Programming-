
from flask import Flask, render_template, request

app = Flask(__name__)

icecreams = [
    {"name": "Vanilla", "price": 80, "emoji": "🍦"},
    {"name": "Chocolate", "price": 100, "emoji": "🍫"},
    {"name": "Strawberry", "price": 90, "emoji": "🍓"},
    {"name": "Mango", "price": 100, "emoji": "🥭"},
    {"name": "Butterscotch", "price": 110, "emoji": "🍨"},
    {"name": "Pista", "price": 120, "emoji": "🍧"},
    {"name": "Coffee", "price": 130, "emoji": "☕"}
]


@app.route("/")
def home():
    return render_template("index.html", icecreams=icecreams)


@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    flavor = request.form.get("flavor")

    return f"""
    <h1>Thank you, {name}! 🍦</h1>
    <h2>Your order for {flavor} ice cream has been received.</h2>
    <a href="/">Back to Shop</a>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
