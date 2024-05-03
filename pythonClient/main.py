from client import *

if __name__ == "__main__":
    soapService = AirportClient(8080, [], "localhost", "SoapProject/AirportServerImplService")
    soapService.generatePDF(653)

