from flask import Flask
import random

app = Flask(__name__)

QUOTES = [
	"Life is what happens when you're busy making other plans. - John Lennon",
	"The best way to predict the future is to invent it. - Alan Kay",
	"Whether you think you can or you think you can't, you're right. - Henry Ford"
]

@app.route('/')
def hello_world():
	return random.choice(QUOTES)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)