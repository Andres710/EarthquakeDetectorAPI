# coding=utf-8

from sqlalchemy import Column, String, Integer, Float

from app import Base


class Earthquake(Base):
    __tablename__ = 'earthquakes'

    id = Column(Integer, primary_key=True)
    country = Column(String(200))
    city = Column(String(200))
    date = Column(String(10))
    time = Column(String(5))
    magnitude = Column(Float)

    def __init__(self, country, city, date, time, magnitude):
        self.country = country
        self.city = city
        self.date = date
        self.time = time
        self.magnitude = magnitude
