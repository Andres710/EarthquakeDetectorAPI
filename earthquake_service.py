from earthquake import Earthquake
from schema import EarthquakeSchema
from app import db


# Gets all earthquakes from DB
def get_all_earthquakes():
    earthquakes = db.session.query(Earthquake).all()
    print(earthquakes)
    result = EarthquakeSchema(many=True).dump(earthquakes)
    return result


def get_an_earthquake(identifier):
    earthquake = db.session.query(Earthquake).filter(Earthquake.id == identifier).first()
    print(earthquake)
    result = EarthquakeSchema().dump(earthquake)
    return result


def post_earthquake(data):
    new_earthquake = Earthquake(data['country'], data['city'], data['date'], data['time'], data['magnitude'])
    db.session.add(new_earthquake)
    db.session.commit()
    return EarthquakeSchema().dump(new_earthquake)
