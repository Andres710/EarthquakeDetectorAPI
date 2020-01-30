# coding=utf-8

from sqlalchemy import Column, String, Integer, Float
from app import db


class Earthquake(db.Model):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200))
    city = db.Column(db.String(200))
    date = db.Column(db.String(10))
    time = db.Column(db.String(5))
    magnitude = db.Column(db.Float)

    def __init__(self, country, city, date, time, magnitude):
        self.country = country
        self.city = city
        self.date = date
        self.time = time
        self.magnitude = magnitude
