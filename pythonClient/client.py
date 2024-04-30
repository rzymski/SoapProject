from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.exceptions import ProxyError, ConnectionError, Timeout
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

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
                imageData = BytesIO(responseText)
                showImage = Image.open(imageData)
                plt.imshow(showImage)
                plt.axis('off')
                plt.show()
            except Exception as e:
                print("Wystąpił błąd:", e)
        else:
            print(responseText)

    def generatePDF(self, reservationID):
        pdfBytes = self.service("generatePdf", reservationID)
        root = tk.Tk()
        root.withdraw()
        if pdfBytes:
            filePath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Pliki PDF", "*.pdf")], initialfile=f"ticketConfirmation{reservationID}", title="Zapisz pdf-a", initialdir="../pdfs")
            if filePath:
                try:
                    with open(filePath, 'wb') as file:
                        file.write(pdfBytes)
                        print("Save pdf file at " + filePath)
                except IOError as e:
                    print("Błąd podczas zapisywania pliku:", e)
            else:
                print("Zapis pliku został anulowany.")


if __name__ == "__main__":
    # soapService = Service(8080, [8085, 8084], "localhost", "SoapProject/AirportServerImplService?WSDL")
    soapService = Service(8080, [], "localhost", "SoapProject/AirportServerImplService?WSDL")

    # soapService.printService("echo", "PIZZA IS THE BEST")
    # soapService.printService("getFlightsData")
    # soapService.printService("getFlightsByFromCity", "Tokyo")
    # soapService.printService("getFlightsByToCity", "New York")
    # soapService.printService("getFlightsFromCityToCity", "Rome", "new york")
    # soapService.printService("getFlightsFromCityToCityWithinDateRange", "rome", "kair", "2024-05-11T03:30:00", "2024-05-21T03:30:00")
    # soapService.printService("getAllFlightsWithParameters", None, "rome", None, "2024-05-10T03:30:00")
    soapService.printService("findAvailableAirports")
    # soapService.printService("downloadImage")
    # soapService.printService("getFlightById", "1010")
    # soapService.printService("checkFlightReservation", "653")
    # soapService.printService("reserveFlight", 1025, 5)
    # soapService.printService("cancelFlightReservation", 1099)
    # soapService.printService("createUser", "pythonClient", "python", "python@gmail.com")
    soapService.generatePDF(653)
