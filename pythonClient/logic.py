from datetime import datetime
from functools import wraps
from icecream import ic


class AirportLogic:
    javaDateFormat = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, client):
        self.client = client
        self.username, self.email, self.password = [None] * 3

    def getAllAirports(self):
        return [airport.title() for airport in self.client.service("findAvailableAirports")]

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
    def refactorFlight(flightData):
        departureTime = datetime.strptime(flightData['departureTime'], AirportLogic.javaDateFormat).strftime("%H:%M %d/%m/%Y")
        arrivalTime = datetime.strptime(flightData['arrivalTime'], AirportLogic.javaDateFormat).strftime("%H:%M %d/%m/%Y")
        departureTime = departureTime if departureTime[0] != "0" else departureTime[1:]
        arrivalTime = arrivalTime if arrivalTime[0] != "0" else arrivalTime[1:]
        return {"id": flightData['id'], "flightCode": flightData['flightCode'], "departureAirport": flightData['departureAirport'], "departureTime": departureTime, "destinationAirport": flightData['destinationAirport'], "arrivalTime": arrivalTime}

    @staticmethod
    def refactorFlightList(flightsData):
        flights = []
        for flightData in flightsData:
            flight = AirportLogic.refactorFlight(flightData)
            flights.append(flight)
        return flights

    @staticmethod
    def convertEmptyToNoneDecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Zamień wszystkie puste ciągi na None w argumentach pozycyjnych
            newArgs = [None if arg == "" else arg for arg in args]
            # Zamień wszystkie puste ciągi na None w argumentach nazwanych
            newKwargs = {k: (None if v == "" else v) for k, v in kwargs.items()}
            # Wywołaj oryginalną funkcję z nowymi argumentami
            return func(*newArgs, **newKwargs)
        return wrapper

    def getAllFlights(self):
        flightsData = self.client.service("getFlightsData")
        return AirportLogic.refactorFlightList(flightsData)

    @convertEmptyToNoneDecorator
    def getFlightsWithParameters(self, departureAirport, destinationAirport, departureTime, arrivalTime):
        flightsData = self.client.service("getAllFlightsWithParameters", departureAirport, destinationAirport, departureTime, arrivalTime)
        ic(flightsData)
        return AirportLogic.refactorFlightList(flightsData)

    @staticmethod
    def refactorReservation(reservationData):
        departureTime = datetime.strptime(reservationData['departureTime'], AirportLogic.javaDateFormat).strftime("%H:%M %d/%m/%Y")
        arrivalTime = datetime.strptime(reservationData['arrivalTime'], AirportLogic.javaDateFormat).strftime("%H:%M %d/%m/%Y")
        departureTime = departureTime if departureTime[0] != "0" else departureTime[1:]
        arrivalTime = arrivalTime if arrivalTime[0] != "0" else arrivalTime[1:]
        return {"id": reservationData['id'], "reservationId": reservationData['reservationId'], "flightCode": reservationData['flightCode'], "airports": f"{reservationData['departureAirport']} ---> {reservationData['destinationAirport']}", "dates": f"{arrivalTime}", "seats": f"{reservationData['numberOfReservedSeats']}/{reservationData['capacity']}"}

    @staticmethod
    def refactorReservationList(reservationsData):
        reservations = []
        for reservationData in reservationsData:
            reservation = AirportLogic.refactorReservation(reservationData)
            reservations.append(reservation)
        return reservations

    def getFlightReservations(self):
        reservationsData = self.client.service("getUserReservations")
        return AirportLogic.refactorReservationList(reservationsData)

