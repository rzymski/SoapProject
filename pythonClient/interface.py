from tkinter import *
import tkinter.font as font
from icecream import ic


class AirportInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Airport interface")
        boldFont18 = font.Font(size=18, weight="bold")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        root.state("zoomed")
        # Top frame, its weights and buttons login, register, logout
        self.topFrame = self.createLabelFrame(self.root, pad=[10, 10], side="top", fill="both")
        self.topFrame.grid_columnconfigure(0, weight=1)  # Kolumna do rozciągania
        self.topFrame.grid_columnconfigure(1, weight=0)  # Kolumna dla przycisku login
        self.topFrame.grid_columnconfigure(2, weight=0)  # Kolumna dla przycisku register
        # self.loggedUserLabel = Label(self.topFrame, text="Zalogowany uzytkownik")
        self.loggedUserLabel = self.createLabel(self.topFrame, text="NAZWA UZYTKOWNIKA", grid=[0, 0], labelFont=[32, "bold"])
        self.loginButton = self.createButton(self.topFrame, text="Zaloguj się", command=self.login, pad=[20, 20], grid=[0, 1], buttonFont=[24, "bold"])
        self.registerButton = self.createButton(self.topFrame, text="Zarejestruj się", command=self.register, pad=[20, 20], grid=[0, 2], buttonFont=[24, "bold"])
        self.logoutButton = self.createButton(self.topFrame, text="Wyloguj się", command=self.logout, pad=[20, 20], grid=[0, 3], buttonFont=[24, "bold"])
        # Left frame buttons checkFlights, findFlight, reserve flight, cancel reservation
        self.leftFrame = self.createLabelFrame(self.root, pad=[0, 0], side="left", fill="both")
        self.checkFlightsButton = self.createButton(self.leftFrame, text="Sprawdź listę lotów", command=self.checkFlightList, pad=[10, 10], grid=[0, 0], buttonFont=[28, "bold"])
        self.findFlightLabel = self.createLabel(self.leftFrame, text='', grid=[1, 0], sticky="WE")
        self.findFlightButton = self.createButton(self.findFlightLabel, text="Wyszukaj lot", command=self.findFlight, pad=[10, 10], grid=[0, 0], span=(2, 1), buttonFont=[28, "bold"])
        # dropdown departure city
        self.fromLabel = self.createLabel(self.findFlightLabel, "Z:", grid=[0, 1], labelFont=[18, "bold"])
        self.fromAirportVar = StringVar()
        # pozniej trzeba zrobic, zeby opcje pobieral z WSDL
        self.options = [''] + ['Warsaw', 'Paris', 'Rome', 'Moscow', 'Berlin', 'London', 'Los Angeles', 'New York', 'Tokyo', 'Beijing', 'Kair', "Madrid", 'Brasilia', 'Seul']
        self.fromDropdown = OptionMenu(self.findFlightLabel, self.fromAirportVar, *self.options)
        self.fromDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.fromDropdown['font'] = boldFont18
        self.fromDropdown.grid(row=0, column=2)
        # dropdown destination city
        self.toLabel = self.createLabel(self.findFlightLabel, "Do:", grid=[1, 1], labelFont=[18, "bold"])
        self.toAirportVar = StringVar()
        self.toDropdown = OptionMenu(self.findFlightLabel, self.toAirportVar, *self.options)
        self.toDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.toDropdown['font'] = boldFont18
        self.toDropdown.grid(row=1, column=2)
        # reserve button
        self.reserveFlightButton = self.createButton(self.leftFrame, text="Zarezerwuj lot", command=self.reserveFlight, pad=[10, 10], grid=[2, 0], buttonFont=[28, "bold"])
        # cancel reservation
        self.cancelReservationButton = self.createButton(self.leftFrame, text="Anuluj rezerwacje", command=self.cancelReservation, pad=[10, 10], grid=[3, 0], buttonFont=[28, "bold"])
        # flights
        self.flightsLabel = self.createLabelFrame(self.root, expand=True, pad=[0, 0])

        self.flightsHeader = self.createLabel(self.flightsLabel, pack=[None, False, "x"], pad=[10, 10])
        self.flightsHeaderFlightCode = self.createLabel(self.flightsHeader, "KOD LOTU", pack=["left", True, "x"], pad=[20, 10])
        self.flightsHeaderDepartureAirport = self.createLabel(self.flightsHeader, "LOTNISKO ODLOTU", pack=["left", True, "x"], pad=[20, 10])
        self.flightsHeaderDepartureTime = self.createLabel(self.flightsHeader, "CZAS ODLOTU", pack=["left", True, "x"], pad=[20, 10])
        self.flightsHeaderDestinationAirport = self.createLabel(self.flightsHeader, "LOTNISKO DOCELOWE", pack=["left", True, "x"], pad=[20, 10])
        self.flightsHeaderArrivalTime = self.createLabel(self.flightsHeader, "CZAS PRZYLOTU", pack=["right", True, "x"], pad=[20, 10])


        # hide buttons which shouldn't be displayed to not logged user
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.reserveFlightButton, self.cancelReservationButton])  # ukrycie przyciskow rezerwowania i usuwania rezerwacji
        # self.showButtonsAndLabels([[self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])  # wyswietlenie przyciskow rezerwowania i usuwania rezerwacji

        self.scrollableFrame = self.createScrollableFrame(self.flightsLabel)


        for i in range(200):
            # label = Label(self.scrollableFrame, text=f"Etykieta {i + 1}", padx=10, pady=5, font=font.Font(size=12))
            # label.pack(anchor="w")
            label = self.createFlightRow(self.scrollableFrame, f"Flight {i + 1}")

    def createFlightRow(self, frame, flightCode="KOD", departureAirport="ODLOT Z", departureTime="YYYY-MM-DD HH:mm:ss", destinationAirport="PRZYLOT DO", arrivalTime="YYYY-MM-DD HH:mm:ss"):
        mainLabel = self.createLabel(frame, pack=[None, True, "x"], pad=[5, 5])
        flightsHeaderFlightCode = self.createLabel(mainLabel, flightCode, pack=["left", True, "x"], pad=[20, 5])
        flightDepartureAirport = self.createLabel(mainLabel, departureAirport, pack=["left", True, "x"], pad=[20, 5])
        flightDepartureTime = self.createLabel(mainLabel, departureTime, pack=["left", True, "x"], pad=[20, 5])
        flightDestinationAirport = self.createLabel(mainLabel, destinationAirport, pack=["left", True, "x"], pad=[20, 5])
        flightArrivalTime = self.createLabel(mainLabel, arrivalTime, pack=["right", True, "x"], pad=[20, 5])
        return mainLabel

    def createScrollableFrame(self, parent, padx=10, pady=10):
        # Utworzenie ramki zawierającej Canvas i Scrollbar
        container = Frame(parent)
        container.pack(expand=True, fill="both")
        # Utworzenie Canvas i pionowego paska przewijania
        canvas = Canvas(container, bg="white")
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", expand=True, fill="both")
        # Konfiguracja Canvas i tworzenie okna wewnątrz Canvas
        innerFrame = Frame(canvas)
        canvas.create_window((0, 0), window=innerFrame, anchor="nw")
        # Konfiguracja Scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Aktualizacja rozmiaru przewijania
        def update_scrollregion(event):
            canvas.config(scrollregion=canvas.bbox("all"))
        # Ustawienie eventu na zmianę rozmiaru
        innerFrame.bind("<Configure>", update_scrollregion)
        return innerFrame

    def createLabelFrame(self, frame, pad, side=None, fill="both", expand=False, text="", labelFont=[18, "bold"]):
        labelFrame = LabelFrame(frame, padx=pad[0], pady=pad[1], text=text)
        labelFrame.pack(side=side, fill=fill, expand=expand)
        labelFrame['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        return labelFrame

    def createLabel(self, frame, text='', grid=None, pack=None, sticky="WE", span=(1, 1), pad=[0, 0], labelFont=[18, "bold"]):
        label = Label(frame, text=text, padx=pad[0], pady=pad[1])
        if grid:
            label.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        if pack:
            label.pack(side=pack[0], expand=pack[1], fill=pack[2])
        label['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        return label

    def createButton(self, frame, text, command, pad, grid, sticky="WE", span=(1, 1), buttonFont=[18, "bold"]):
        button = Button(frame, text=text, command=command, padx=pad[0], pady=pad[1])
        button.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        button['font'] = font.Font(size=buttonFont[0], weight=buttonFont[1])
        return button

    def showButtonsAndLabels(self, elementsWithGridPositions):
        for data in elementsWithGridPositions:
            data[0].grid(row=data[1][0], column=data[1][1], sticky=data[1][2])

    def hideButtonsAndLabels(self, elements):
        for element in elements:
            element.grid_forget()

    def register(self):
        ic("Register")
        self.hideButtonsAndLabels([self.loginButton, self.registerButton])
        self.showButtonsAndLabels([[self.loggedUserLabel, (0, 0, "WE")], [self.logoutButton, (0, 3, "E")], [self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])

    def login(self):
        ic("Login")
        self.hideButtonsAndLabels([self.loginButton, self.registerButton])
        self.showButtonsAndLabels([[self.loggedUserLabel, (0, 0, "WE")], [self.logoutButton, (0, 3, "E")], [self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])

    def logout(self):
        ic("Logout")
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.reserveFlightButton, self.cancelReservationButton])
        self.showButtonsAndLabels([[self.loginButton, (0, 1, "E")], [self.registerButton, (0, 2, "E")]])


    def checkFlightList(self):
        ic("Check flight list")

    def findFlight(self):
        departureAirport = self.fromAirportVar.get()
        destinationAirport = self.toAirportVar.get()
        ic("find flight", departureAirport, destinationAirport)

    def reserveFlight(self):
        ic("reserve flight")

    def cancelReservation(self):
        ic("Anuluj rezerwacje")


if __name__ == "__main__":
    rootInterface = Tk()
    app = AirportInterface(rootInterface)
    rootInterface.mainloop()
