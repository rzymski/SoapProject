from datetime import datetime
from icecream import ic


class AirportLogic:
    def __init__(self, client):
        self.client = client
        self.username, self.email, self.password = [None] * 3
        self.javaDateFormat = "%Y-%m-%dT%H:%M:%S"

    def validateUser(self, username, password):
        ic("Logika walidacja: ", username, password)
        self.client.setUser(username, password)
        result = self.client.getHeaderValue("echo", "Check if user is correct")
        if result:
            self.username = username
            self.password = password
        return result

    def createUser(self, username, password, email):
        ic("Logika tworzenie uzytkownika: ", username, password, email)
        result = self.client.service("createUser", username, password, email)
        if result:
            self.username = username
            self.password = password
            self.email = email
            self.client.setUser(username, password)
        return result

    def logoutUser(self):
        ic("Logika wylogowano uzytkownika")
        self.username, self.email, self.password = [None] * 3
        self.client.setUser(None, None)

    @staticmethod
    def removeLeadingZero(s):
        return s[1:] if s[0] == "0" else s

    def getAllFlights(self):
        flightsData = self.client.service("getFlightsData")
        flights = []
        for flightData in flightsData:
            departureTime = AirportLogic.removeLeadingZero(datetime.strptime(flightData['departureTime'], self.javaDateFormat).strftime("%H:%M %d/%m/%Y"))
            arrivalTime = AirportLogic.removeLeadingZero(datetime.strptime(flightData['arrivalTime'], self.javaDateFormat).strftime("%H:%M %d/%m/%Y"))
            flight = {"flightCode": flightData['flightCode'], "departureAirport": flightData['departureAirport'], "departureTime": departureTime, "destinationAirport": flightData['destinationAirport'], "arrivalTime": arrivalTime}
            flights.append(flight)
        return flights
