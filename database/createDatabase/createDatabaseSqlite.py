from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flight import Base, Flight
import random
from datetime import datetime, timedelta

engine = create_engine('sqlite:///../airport.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

flights_data = []

ports = ['Warsaw', 'Paris', 'Rome', 'Moscow', 'Berlin', 'London', 'Los Angeles', 'New York', 'Tokyo', 'Beijing', 'Kair']

counter = 0
for day in range(7):
    for hour in range(24):
        b = random.randint(0, 11)
        if (b*day*hour) % 3 == 0:
            selected_ports = random.sample(ports, 2)
            departureTime = datetime(2024, 5, 6+day, hour, 5*b, 0)
            arrivalTime = departureTime + timedelta(hours=b+1)
            counter += 1
            flight = {'flightCode': f'LOT {counter}', 'departureAirport': selected_ports[0], 'departureTime': departureTime, 'destinationAirport': selected_ports[1], 'arrivalTime': arrivalTime}
            flights_data.append(flight)
            print(flight)

print(f"LIczba lotów = {len(flights_data)}")

for flight_data in flights_data:
    flight = Flight(**flight_data)
    session.add(flight)

session.commit()
session.close()
