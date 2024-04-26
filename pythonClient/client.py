from zeep import Client
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt


class Service:
    def __init__(self, wsdl_url):
        self.wsdl_url = wsdl_url
        self.client = Client(wsdl=wsdl_url)

    def service(self, serviceName, *args):
        kwargs = {f"arg{idx}": arg for idx, arg in enumerate(args)}
        # print(f"Argumenty = {kwargs}")
        try:
            return getattr(self.client.service, serviceName)(**kwargs)
        except Exception as e:
            print("Wystąpił błąd:", e)
            return None

    def printService(self, serviceName, *args):
        print(f"{serviceName} zwrócił: ")
        responseText = self.service(serviceName, *args)
        if serviceName in ["getFlightsData", "getFlightsByFromCity", "getFlightsByToCity"]:
            for flight in responseText:
                print(f"Id: {flight['id']}, flightCode: {flight['flightCode']} z {flight['departureAirport']} o {flight['departureTime']} do {flight['destinationAirport']} o {flight['arrivalTime']}")
        elif serviceName == "downloadImage":
            try:
                image_data = BytesIO(responseText)
                image = Image.open(image_data)
                # Wyświetl obraz
                plt.imshow(image)
                plt.axis('off')  # Ukryj osie
                plt.show()
            except Exception as e:
                print("Wystąpił błąd:", e)
        else:
            print(responseText)


wsdl_url = 'http://localhost:8080/SoapProject/AirportServerImplService?WSDL'
soapService = Service(wsdl_url)

soapService.printService("echo", "PIZZA IS THE BEST")
# soapService.printService("getFlightsData")
# soapService.printService("getFlightsByFromCity", "Tokyo")
# soapService.printService("getFlightsByToCity", "New York")
# soapService.printService("downloadImage")
# soapService.printService("getFlightById", "1010")
soapService.printService("checkFlightReservation", "653")
# soapService.printService("reserveFlight", 1099, 1)
# soapService.printService("cancelFlightReservation", 1099)
