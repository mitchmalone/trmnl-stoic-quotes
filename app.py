from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

with open('quotes.json', 'r') as quotes:
	QUOTES = json.load(quotes)

@app.route('/')
def hello_world():
	selected = random.choice(QUOTES)
	return jsonify(selected)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)