from earthquake import Earthquake
from schema import EarthquakeSchema
from app import db


# Gets all earthquakes from DB, optional filters
def get_all_earthquakes_with_filter(country: str, city: str):
    earthquakes = None
    if country is not None and city is not None:
        earthquakes = db.session.query(Earthquake)\
            .filter(Earthquake.country == country)\
            .filter(Earthquake.city == city)\
            .all()
    elif country is not None:
        earthquakes = db.session.query(Earthquake).filter(Earthquake.country == country).all()
    elif city is not None:
        earthquakes = db.session.query(Earthquake).filter(Earthquake.city == city).all()
    else:
        earthquakes = db.session.query(Earthquake).all()

    return EarthquakeSchema(many=True).dump(earthquakes)


# Gets an earthquake given an identifier
def get_an_earthquake(identifier):
    earthquake = db.session.query(Earthquake).filter(Earthquake.id == identifier).first()
    result = EarthquakeSchema().dump(earthquake)
    return result


# Gets the strongest earthquake in the DB
def get_strongest_earthquake():
    earthquake = db.session.query(Earthquake).order_by(Earthquake.magnitude.desc()).first()
    return EarthquakeSchema().dump(earthquake)


# Gets the weakest earthquake in the DB
def get_weakest_earthquake():
    earthquake = db.session().query(Earthquake).order_by(Earthquake.magnitude).first()
    return EarthquakeSchema().dump(earthquake)


# Gets all earthquakes and calculates the average magnitude
def get_average_magnitude():
    earthquakes = db.session().query(Earthquake).all()
    print(earthquakes)
    length = len(earthquakes)
    average = 0
    for i in earthquakes:
        average += i.magnitude
    if length > 0:
        average = average/length
    response = {
        'number_of_earthquakes': length,
        'average_magnitude': average,
    }
    return response


# Registers a new earthquake into the DB
def post_earthquake(data):
    new_earthquake = Earthquake(data['country'], data['city'], data['date'], data['time'], data['magnitude'])
    db.session.add(new_earthquake)
    db.session.commit()
    return EarthquakeSchema().dump(new_earthquake)


# Deletes an earthquake from the DB given an identifier
def delete_earthquake(identifier):
    earthquake = db.session.query(Earthquake).filter(Earthquake.id == identifier).first()
    if earthquake is not None:
        db.session.delete(earthquake)
        db.session.commit()
        return True

    return False
