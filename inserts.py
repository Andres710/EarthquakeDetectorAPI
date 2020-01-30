# File for inserting data into the database manually

from earthquake import Earthquake
from app import db

# Create earthquakes
first_earthquake = Earthquake("Colombia", "Bogota", "29/01/2020", "16:04", 4.0)
second_earthquake = Earthquake("Ecuador", "Guayaquil", "30/01/2020", "08:48", 5.4)
third_earthquake = Earthquake("Italy", "Rome", "30/01/2020", "08:51", 7.5)


# Persist data
db.session.add(first_earthquake)
db.session.add(second_earthquake)
db.session.add(third_earthquake)

# Commit and close session
db.session.commit()
db.session.close()
