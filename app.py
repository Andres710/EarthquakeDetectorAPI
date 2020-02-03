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
def get_all_earthquakes():
    print(request.args)
    country_filter = request.args.get('country')
    city_filter = request.args.get('city')
    earthquakes = earthquake_service.get_all_earthquakes_with_filter(country_filter, city_filter)
    return jsonify(earthquakes)


# Get an earthquake by his identifier
@app.route('/earthquakes/<identifier>', methods=['GET'])
def get_an_earthquake(identifier):
    print(identifier)
    earthquake = earthquake_service.get_an_earthquake(identifier)
    print(earthquake)
    if earthquake:
        return jsonify(earthquake)
    else:
        data = {
            'status_code': 404,
            'message': 'There is no earthquake with the given identifier'
        }
        return data, 404


@app.route('/earthquakes/strongest', methods=['GET'])
def get_strongest_earthquake():
    earthquake = earthquake_service.get_strongest_earthquake()
    return jsonify(earthquake)


@app.route('/earthquakes/weakest', methods=['GET'])
def get_weakest_earthquake():
    earthquake = earthquake_service.get_weakest_earthquake()
    return jsonify(earthquake)


# Register a new earthquake
@app.route('/earthquakes', methods=['POST'])
def post_earthquake():
    req_data = request.json
    result = earthquake_service.post_earthquake(req_data)
    return jsonify(result)


# Delete an earthquake using an identifier
@app.route('/earthquakes/<identifier>', methods=['DELETE'])
def delete_earthquake(identifier):
    result = earthquake_service.delete_earthquake(identifier)
    if result:
        data = {
            'status_code': 200,
            'message': 'Earthquake deleted successfully.'
        }
        return jsonify(data), 200
    else:
        data = {
            'status_code': 404,
            'message': 'Earthquake with given identifier does not exist.'
        }
        return jsonify(data), 404


if __name__ == "__main__":
    app.run(debug=True)
