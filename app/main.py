from flask import Flask, jsonify
from .utils import get_random_quote

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"quote": get_random_quote()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
