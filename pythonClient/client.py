from zeep import Client
from zeep.plugins import HistoryPlugin
from zeep.transports import Transport
from zeep.exceptions import Fault
from requests import Session
from requests.exceptions import ProxyError, ConnectionError, Timeout
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from lxml import etree

# Loggi z requestami
# import logging
# logging.basicConfig(level=logging.DEBUG)


class AirportClient:
    def __init__(self, serverPort, proxyPorts, ipAddress, serviceUrl, username=None, password=None):
        self.serverPort = serverPort
        self.proxyPorts = proxyPorts
        self.ipAddress = ipAddress
        self.serviceUrl = serviceUrl
        self.username = username
        self.password = password
        self.plugin = HistoryPlugin()
        self.session = Session()
        for proxyPort in proxyPorts + [None]:
            try:
                self.session.headers.update({
                    'username': username,
                    'password': password,
                })
                self.session.proxies = {'http': f'http://{ipAddress}:{proxyPort}/{serviceUrl}?WSDL'} if proxyPort else None
                transport = Transport(session=self.session, timeout=1)
                wsdlUrl = f'http://{ipAddress}:{serverPort}/{serviceUrl}?WSDL'
                self.client = Client(wsdl=wsdlUrl, transport=transport, plugins=[self.plugin])
                break
            except (ProxyError, ConnectionError, Timeout) as e:
                print(f"Nie udało się połączyć z proxy na porcie {proxyPort if proxyPort is not None else serverPort}.")

    def setUser(self, username, password):
        if self.client:
            try:
                self.session.headers.update({
                    'username': username,
                    'password': password,
                })
            except Exception as e:
                print(f"Wystąpił problem podczas aktualizacji danych użytkownika: {e}")
        else:
            print("Klient nie został poprawnie zainicjalizowany.")

    def service(self, serviceName, *args):
        kwargs = {f"arg{idx}": arg for idx, arg in enumerate(args)}
        # print(f"Argumenty = {kwargs}")
        try:
            return getattr(self.client.service, serviceName)(**kwargs)
        except Fault as fault:
            print(f"W service wystąpił błąd {fault.code} z komunikatem: {fault}")
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
                print("W printService wystąpił błąd:", e)
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

    def getHeaderValue(self, serviceName, *args):
        result = self.service(serviceName, *args)
        if not result:
            return None
        responseXML = etree.tostring(self.plugin.last_received["envelope"], encoding="unicode", pretty_print=True) if len(self.plugin.last_received["envelope"]) > 0 else None
        # print(responseXML)
        if not responseXML:
            return None
        root = ET.fromstring(responseXML)
        namespace = {'SOAP-ENV': 'http://schemas.xmlsoap.org/soap/envelope/'}
        header = root.find('.//SOAP-ENV:Header', namespaces=namespace)
        usernameValidation = header.find(".//{http://" + str(self.ipAddress) + ":" + str(self.serverPort) + "/" + self.serviceUrl + "}usernameValidation").text
        print("Wartość usernameValidation:", usernameValidation)
        return usernameValidation == "true"


if __name__ == "__main__":
    # soapService = Service(8080, [8085, 8084], "localhost", "SoapProject/AirportServerImplService")
    soapService = AirportClient(8080, [], "localhost", "SoapProject/AirportServerImplService")
    # soapService.setUser("user", "admin")

    soapService.printService("echo", "PIZZA IS THE BEST")
    # soapService.getHeaderValue("echo", "PIZZA IS THE BEST")
    # soapService.printService("getFlightsData")
    # soapService.printService("getFlightsByFromCity", "Tokyo")
    # soapService.printService("getFlightsByToCity", "New York")
    # soapService.printService("getFlightsFromCityToCity", "Rome", "new york")
    # soapService.printService("getFlightsFromCityToCityWithinDateRange", "rome", "kair", "2024-05-11T03:30:00", "2024-05-21T03:30:00")
    # soapService.printService("getAllFlightsWithParameters", None, "rome", None, "2024-05-10T03:30:00")
    # soapService.printService("findAvailableAirports")
    # soapService.printService("downloadImage")
    # soapService.printService("getFlightById", "1010")
    # soapService.printService("checkFlightReservation", "653")
    # soapService.printService("reserveFlight", 1025, 5)
    # soapService.printService("cancelFlightReservation", 1099)
    # soapService.printService("createUser", "pythonClient", "xd", "python@gmail.com")
    # soapService.generatePDF(653)
    soapService.printService("getUserReservations")
