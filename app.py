from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def index():
    print("Welcome to Intelimetrica Test Backend")
    result = {'message': 'Index', 'status': '200', 'payload': []}
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)