import random
from datetime import datetime, timedelta
import csv

flights_data = []

ports = ['Warsaw', 'Paris', 'Rome', 'Moscow', 'Berlin', 'London', 'Los Angeles', 'New York', 'Tokyo', 'Beijing', 'Kair']

counter = 0
for day in range(10):
    for hour in range(24):
        b = random.randint(0, 11)
        if (b*day*hour) % 3 == 0:
            selected_ports = random.sample(ports, 2)
            departureTime = datetime(2024, 5, 6+day, hour, 5*b, 0)
            arrivalTime = departureTime + timedelta(hours=b + 1)
            counter += 1
            flight = {'flightCode': f'LOT {counter}', 'departureAirport': selected_ports[0], 'departureTime': departureTime, 'destinationAirport': selected_ports[1], 'arrivalTime': arrivalTime}
            flights_data.append(flight)

print(f"Liczba lotów = {len(flights_data)}")

csv_path = '../flights.csv'

with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["flightCode", "departureAirport", "departureTime", "destinationAirport", "arrivalTime"])
    writer.writeheader()
    for flight in flights_data:
        print(flight)
        writer.writerow(flight)


