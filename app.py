import os

from flask import Flask, jsonify
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)

@app.route("/")
def index():
    print("Welcome to Intelimetrica Test Backend")
    result = {'message': 'Index', 'status': '200', 'payload': []}
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)