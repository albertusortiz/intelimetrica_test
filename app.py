import os

import pymysql

from flask import Flask, jsonify
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
USERNAME_DATABASE = os.getenv('USERNAME_DATABASE')
PASSWORD = os.getenv('PASSWORD')

print("HOST:",HOST)
print("DATABASE:",DATABASE)
print("USERNAME_DATABASE:",USERNAME_DATABASE)
print("PASWORD:",PASSWORD)

app = Flask(__name__)

miConexion = pymysql.connect(host=HOST,user=USERNAME_DATABASE,passwd=PASSWORD,db=DATABASE)
cur = miConexion.cursor()


@app.route("/")
def index():
    result = {'message': 'Index', 'status': '200', 'payload': []}
    return jsonify(result), 200


@app.route("/read")
def read():
    cur.execute("SELECT * FROM restaurants")
    for row in cur.fetchall():
        id = row[0]
        name = row[2]
        site = row[3]
        # Now print fetched result
        print ("id = {0}, name = {1}, site = {2}".format(id,name,site))
    
    restaurants = []
    restaurants = cur.fetchall()

    data_restaurants = {}
    for row in cur.fetchall():
        data_restaurants[row] = {
            id : row[0],
            name : row[2],
            site : row[3],
        }


    result = {'message': 'Index', 'status': '200', 'payload': data_restaurants}
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)