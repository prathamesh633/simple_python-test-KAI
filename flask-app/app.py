from flask import Flask, jsonify, request
from utils import add_numbers

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello World"})

@app.route("/add")
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        result = add_numbers(a, b)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
