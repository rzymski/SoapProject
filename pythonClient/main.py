from tkinter import Tk
from interface import AirportInterface
from logic import AirportLogic
from client import AirportClient

if __name__ == "__main__":
    try:
        rootInterface = Tk()
        app = AirportInterface(rootInterface, AirportLogic(AirportClient(8080, [8085, 8084], "localhost", "SoapProject/AirportServerImplService", proxyInClientSide=True)))
        # app = AirportInterface(rootInterface, AirportLogic(AirportClient(8080, [], "localhost", "SoapProject/AirportServerImplService")))
        rootInterface.mainloop()
    except ValueError as e:
        print(e)
