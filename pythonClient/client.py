from zeep import Client

# Adres URL usługi
url = 'http://localhost:8080/SoapProject/AirportServerImplService?WSDL'
# Tworzymy klienta SOAP
client = Client(url)

try:
    response = client.service.echo("DZIALA")
    print("Odpowiedź z serwera:", response)
except Exception as e:
    print("Wystąpił błąd:", e)


try:
    response = client.service.getFlightsData()
    if response:
        # print(response)
        # print("Lista lotów:")
        # for flight in response:
        #     print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")
        flight = response[0]
        print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")

    else:
        print("Brak lotów.")
except Exception as e:
    print("Wystąpił błąd:", e)


try:
    response = client.service.downloadImage()
    if response:
        pass
        # print(response)
    else:
        print("Brak lotów.")
except Exception as e:
    print("Wystąpił błąd:", e)
