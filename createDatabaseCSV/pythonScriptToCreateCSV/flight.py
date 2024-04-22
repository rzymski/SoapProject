from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    flightCode = Column(String)
    departureAirport = Column(String)
    departureTime = Column(DateTime)
    destinationAirport = Column(String)
    arrivalTime = Column(DateTime)
