from flask_marshmallow import Marshmallow
from app import app

ma = Marshmallow(app)


class EarthquakeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'city', 'date', 'time', 'magnitude')
