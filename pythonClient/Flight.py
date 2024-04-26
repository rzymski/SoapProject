class Flight:

    id = Column(Integer, primary_key=True)
    flightCode = Column(String)
    departureAirport = Column(String)
    departureTime = Column(DateTime)
    destinationAirport = Column(String)
    arrivalTime = Column(DateTime)
