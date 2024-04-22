from zeep import Client

# Adres URL usługi
url = 'http://localhost:8080/SoapProject/AirportServerImplService?WSDL'
# Tworzymy klienta SOAP
client = Client(url)


def echo(text):
    try:
        response = client.service.echo(text)
        print("Odpowiedź z serwera:", response)
    except Exception as e:
        print("Wystąpił błąd:", e)


def getFlightsData():
    try:
        response = client.service.getFlightsData()
        if response:
            print(response)
            print("Lista lotów:")
            for flight in response:
                print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")
        else:
            print("Brak lotów.")
    except Exception as e:
        print("Wystąpił błąd:", e)


def getFlightsByFromCity(city):
    try:
        response = client.service.getFlightsByFromCity(city)
        if response:
            # print(response)
            print("Lista lotów:")
            for flight in response:
                print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")
        else:
            print("Brak lotów.")
    except Exception as e:
        print("Wystąpił błąd:", e)


def getFlightsByToCity(city):
    try:
        response = client.service.getFlightsByToCity(city)
        if response:
            # print(response)
            print("Lista lotów:")
            for flight in response:
                print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")
        else:
            print("Brak lotów.")
    except Exception as e:
        print("Wystąpił błąd:", e)


def downloadImage():
    try:
        response = client.service.downloadImage()
        if response:
            print(response)
        else:
            print("Brak lotów.")
    except Exception as e:
        print("Wystąpił błąd:", e)


# echo("PIZZA IS THE BEST")
# getFlightsData()
# getFlightsByFromCity("London")
# getFlightsByToCity("London")
# downloadImage()