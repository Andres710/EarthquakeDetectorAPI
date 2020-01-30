import mysql.connector
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import earthquake_service


app = Flask(__name__)

# Using flask_sqlalchemy for DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:bases123@localhost:3306/earthquakes";
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db)


# Get all earthquakes
@app.route('/earthquakes', methods=['GET'])
def index():
    earthquakes = earthquake_service.get_all_earthquakes()
    return jsonify(earthquakes)


# Get an earthquake by his identifier
@app.route('/earthquakes/<identifier>', methods=['GET'])
def get_an_earthquake(identifier):
    print(identifier)
    earthquake = earthquake_service.get_an_earthquake(identifier)
    return jsonify(earthquake)


# Register a new earthquake
@app.route('/earthquakes', methods=['POST'])
def post_earthquake():
    req_data = request.json
    result = earthquake_service.post_earthquake(req_data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
