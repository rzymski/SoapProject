from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.exceptions import ProxyError, ConnectionError, Timeout
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime

# Loggi z requestami
# import logging
# logging.basicConfig(level=logging.DEBUG)


class Service:
    def __init__(self, serverPort, proxyPorts, ipAddress, serviceUrl):
        for proxyPort in proxyPorts + [None]:
            try:
                session = Session()
                session.headers.update({
                    'username': 'user',
                    'password': 'admin',
                })
                if proxyPort:
                    session.proxies = {'http': f'http://{ipAddress}:{proxyPort}/{serviceUrl}'}
                transport = Transport(session=session, timeout=1)
                self.wsdl_url = f'http://{ipAddress}:{serverPort}/{serviceUrl}'
                self.client = Client(wsdl=self.wsdl_url, transport=transport)
                break
            except (ProxyError, ConnectionError, Timeout) as e:
                print(f"Nie udało się połączyć z proxy na porcie {proxyPort}.")

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
                plt.imshow(image)
                plt.axis('off')
                plt.show()
            except Exception as e:
                print("Wystąpił błąd:", e)
        else:
            print(responseText)


# soapService = Service(8080, [8085, 8084], "localhost", "SoapProject/AirportServerImplService?WSDL")
soapService = Service(8080, [], "localhost", "SoapProject/AirportServerImplService?WSDL")

# soapService.printService("echo", "PIZZA IS THE BEST")
# soapService.printService("getFlightsData")
# soapService.printService("getFlightsByFromCity", "Tokyo")
# soapService.printService("getFlightsByToCity", "New York")
# soapService.printService("downloadImage")
# soapService.printService("getFlightById", "1010")
# soapService.printService("checkFlightReservation", "653")
# soapService.printService("reserveFlight", 1025, 5)
# soapService.printService("cancelFlightReservation", 1099)
# soapService.printService("createUser", "pythonClient", "python", "python@gmail.com")

