from earthquake import Earthquake

from app import Session, engine, Base

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Create earthquakes
first_earthquake = Earthquake("Colombia", "Bogota", "29/01/2020", "16:04", 4.0)
second_earthquake = Earthquake("Ecuador", "Guayaquil", "30/01/2020", "08:48", 5.4)
third_earthquake = Earthquake("Italy", "Rome", "30/01/2020", "08:51", 7.5)


# Persist data
session.add(first_earthquake)
session.add(second_earthquake)
session.add(third_earthquake)

# Commit and close session
session.commit()
session.close()
