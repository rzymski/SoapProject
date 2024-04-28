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

        self.topframe = LabelFrame(self.root, padx=10, pady=10, labelanchor="n")
        self.topframe.pack(side="top", fill="both")
        # Ustawianie wag kolumn w top
        self.topframe.grid_columnconfigure(0, weight=1)  # Kolumna do rozciągania
        self.topframe.grid_columnconfigure(1, weight=0)  # Kolumna dla przycisku login
        self.topframe.grid_columnconfigure(2, weight=0)  # Kolumna dla przycisku register

        self.leftFrame = LabelFrame(self.root, padx=0, pady=0, labelanchor="w")
        self.leftFrame.pack(side="left", fill="both")

        # self.loginButton = Button(self.topframe, text="Zaloguj się", command=self.login, padx=20, pady=20)
        # self.loginButton.grid(row=0, column=1)
        # self.loginButton['font'] = boldFont18
        self.loginButton = self.createButton(self.topframe, text="Zaloguj się", command=self.login, pad=[20, 20], grid=[0, 1], buttonFont=[24, "bold"])

        # self.registerButton = Button(self.topframe, text="Zarejestruj się", command=self.register, padx=20, pady=20)
        # self.registerButton.grid(row=0, column=2)
        # self.registerButton['font'] = boldFont18
        self.registerButton = self.createButton(self.topframe, text="Zarejestruj się", command=self.register, pad=[20, 20], grid=[0, 2], buttonFont=[24, "bold"])

        # self.logoutButton = Button(self.topframe, text="Wyloguj się", command=self.logout, padx=20, pady=20)
        # self.logoutButton.grid(row=0, column=3)
        # self.logoutButton['font'] = boldFont18
        self.logoutButton = self.createButton(self.topframe, text="Wyloguj się", command=self.logout, pad=[20, 20], grid=[0, 3], buttonFont=[24, "bold"])

        # self.checkFlightsButton = Button(self.leftFrame, text="Sprawdź listę lotów", command=self.checkFlightList, padx=20, pady=20)
        # self.checkFlightsButton.grid(row=0, column=0, sticky="WE")
        # self.checkFlightsButton['font'] = boldFont18
        self.checkFlightsButton = self.createButton(self.leftFrame, text="Sprawdź listę lotów", command=self.checkFlightList, pad=[5, 5], grid=[0, 0], buttonFont=[28, "bold"])

        self.findFlightLabel = Label(self.leftFrame)
        self.findFlightLabel.grid(row=1, column=0, sticky="WE")
        # self.findFlightButton = Button(self.findFlightLabel, text="Wyszukaj lot", command=self.findFlight, padx=20, pady=20)
        # self.findFlightButton.grid(row=0, column=0, rowspan=2)
        # self.findFlightButton['font'] = boldFont18
        self.findFlightButton = self.createButton(self.findFlightLabel, text="Wyszukaj lot", command=self.findFlight, pad=[20, 20], grid=[0, 0], span=(2, 1), buttonFont=[18, "bold"])

        self.fromLabel = Label(self.findFlightLabel, text="Z:")
        self.fromLabel.grid(row=0, column=1)
        self.fromLabel['font'] = boldFont18
        # self.fromEntry = Entry(self.findFlightLabel, width=20, justify=CENTER)
        # self.fromEntry.grid(row=0, column=2)
        self.fromAirportVar = StringVar()
        # pozniej trzeba zrobic, zeby opcje pobieral z WSDL
        self.options = [''] + ['Warsaw', 'Paris', 'Rome', 'Moscow', 'Berlin', 'London', 'Los Angeles', 'New York', 'Tokyo', 'Beijing', 'Kair', "Madrid", 'Brasilia', 'Seul']
        self.fromDropdown = OptionMenu(self.findFlightLabel, self.fromAirportVar, *self.options)
        self.fromDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.fromDropdown['font'] = boldFont18
        self.fromDropdown.grid(row=0, column=2)

        self.toLabel = Label(self.findFlightLabel, text="Do:")
        self.toLabel.grid(row=1, column=1)
        self.toLabel['font'] = boldFont18
        # self.toEntry = Entry(self.findFlightLabel, width=20, justify=CENTER)
        # self.toEntry.grid(row=1, column=2)
        self.toAirportVar = StringVar()
        self.toDropdown = OptionMenu(self.findFlightLabel, self.toAirportVar, *self.options)
        self.toDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.toDropdown['font'] = boldFont18
        self.toDropdown.grid(row=1, column=2)

        # self.reserveFlightButton = Button(self.leftFrame, text="Zarezerwuj lot", command=self.reserveFlight, padx=20, pady=20)
        # self.reserveFlightButton.grid(row=2, column=0, sticky="WE")
        # self.reserveFlightButton['font'] = boldFont18
        self.reserveFlightButton = self.createButton(self.leftFrame, text="Zarezerwuj lot", command=self.reserveFlight, pad=[20, 20], grid=[2, 0], buttonFont=[18, "bold"])

        # self.cancelReservationButton = Button(self.leftFrame, text="Anuluj rezerwacje", command=self.cancelReservation, padx=20, pady=20)
        # self.cancelReservationButton.grid(row=3, column=0, sticky="WE")
        # self.cancelReservationButton['font'] = boldFont18
        self.cancelReservationButton = self.createButton(self.leftFrame, text="Anuluj rezerwacje", command=self.cancelReservation, pad=[20, 20], grid=[3, 0], buttonFont=[18, "bold"])

        self.hideButtons([self.logoutButton, self.reserveFlightButton, self.cancelReservationButton])  # ukrycie przyciskow rezerwowania i usuwania rezerwacji
        # self.showButtons([[self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])  # wyswietlenie przyciskow rezerwowania i usuwania rezerwacji

    def createButton(self, frame, text, command, pad, grid, sticky="WE", span=(1, 1), buttonFont=[18, "bold"]):
        button = Button(frame, text=text, command=command, padx=pad[0], pady=pad[1])
        button.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        button['font'] = font.Font(size=buttonFont[0], weight=buttonFont[1])
        return button

    def showButtons(self, buttonsWithGridPositions):
        for data in buttonsWithGridPositions:
            data[0].grid(row=data[1][0], column=data[1][1], sticky=data[1][2])

    def hideButtons(self, buttons):
        for button in buttons:
            button.grid_forget()

    def register(self):
        ic("Register")
        self.hideButtons([self.loginButton, self.registerButton])
        self.showButtons([[self.logoutButton, (3, 0, "E")], [self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])

    def login(self):
        ic("Login")
        self.hideButtons([self.loginButton, self.registerButton])
        self.showButtons([[self.logoutButton, (3, 0, "E")], [self.reserveFlightButton, (2, 0, "WE")], [self.cancelReservationButton, (3, 0, "WE")]])

    def logout(self):
        ic("Logout")
        self.hideButtons([self.logoutButton, self.reserveFlightButton, self.cancelReservationButton])
        self.showButtons([[self.loginButton, (0, 1, "E")], [self.registerButton, (0, 2, "E")]])


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
