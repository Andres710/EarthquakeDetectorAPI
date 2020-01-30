import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
engine = create_engine("mysql://root:bases123@localhost:3306/earthquakes")
Session = sessionmaker(bind=engine)

Base = declarative_base()


@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
