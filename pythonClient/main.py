from client import *

if __name__ == "__main__":
    soapService = Service(8080, [], "localhost", "SoapProject/AirportServerImplService?WSDL")
    soapService.generatePDF(653)

