from tkinter import *
from tkinter import ttk
import tkcalendar as tkc
import tkinter.font as font
from icecream import ic

from logic import AirportLogic
from client import AirportClient


class AirportInterface:
    def __init__(self, root, logicClass):
        print(ttk.Style().theme_names())

        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure("Treeview.Heading", font=(None, 24, "bold"))
        self.style.configure("Treeview", font=("Courier New", 18, "bold"), rowheight=int(18 * 2))
        self.root = root
        self.logic = logicClass
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
        # start date entry
        self.startDateLabel = self.createLabel(self.findFlightLabel, "Od:", grid=[2, 1], labelFont=[18, "bold"])
        self.startDateEntry = tkc.DateEntry(self.findFlightLabel)
        self.startDateEntry['font'] = boldFont18
        self.startDateEntry.grid(row=2, column=2)
        # show reservations
        self.checkReservationsButton = self.createButton(self.leftFrame, text="Sprawdź rezerwacje", command=self.checkReservationList, pad=[10, 10], grid=[2, 0], buttonFont=[28, "bold"])
        # reserve button
        self.reserveFlightButton = self.createButton(self.leftFrame, text="Zarezerwuj lot", command=self.reserveFlight, pad=[10, 10], grid=[3, 0], buttonFont=[28, "bold"])
        # cancel reservation
        self.cancelReservationButton = self.createButton(self.leftFrame, text="Anuluj rezerwacje", command=self.cancelReservation, pad=[10, 10], grid=[4, 0], buttonFont=[28, "bold"])
        # hide buttons which shouldn't be displayed to not logged user
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.checkReservationsButton, self.reserveFlightButton, self.cancelReservationButton])  # ukrycie przyciskow rezerwowania i usuwania rezerwacji
        # flights list
        self.flightsLabel, self.flightList = [None] * 2
        # login panel variables
        self.loginWindow, self.loginPanel, self.usernameLabel, self.usernameEntry, self.passwordLabel, self.passwordEntry, self.loginConfirmButton, self.otherAuthenticationOptionLabel = [None] * 8
        # registration panel variables
        self.registerWindow, self.registerPanel, self.emailLabel, self.emailEntry, self.registerConfirmButton, self.loginOptionLabel = [None] * 6
        # errors in login or registration
        self.noUsernameError, self.emailError, self.noPasswordError, self.noAuthorizationError = [None] * 4


    def validateUserInterface(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        ic("Validate user", username, password)
        self.noUsernameError['text'] = "Pole 'nazwa użytkownika' jest wymagane." if not username else ""
        self.noPasswordError['text'] = "Pole 'hasło' jest wymagane." if not password else ""
        # przykładowe sprawdzenie poprawnosci
        if self.logic.validateUser(username, password):
            self.userAuthorizedInterface(username)
        elif username and password:
            self.noAuthorizationError['text'] = "Nie udało się zalogować. Błędny login lub hasło"
        else:
            self.noAuthorizationError['text'] = ""

    def createUserInterface(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        ic("Create user", username, password, email)
        self.noUsernameError['text'] = "Pole 'nazwa użytkownika' jest wymagane." if not username else ""
        self.noPasswordError['text'] = "Pole 'hasło' jest wymagane." if not password else ""
        if username and password:
            if self.logic.createUser(username, password, email):
                self.userAuthorizedInterface(username)
            else:
                self.noAuthorizationError['text'] = "Nie udało się zarejestrować. Taki użytkownik już istnieje."
        else:
            self.noAuthorizationError['text'] = ""

    def userAuthorizedInterface(self, username):
        if self.loginWindow:
            self.loginWindow.destroy()
        if self.registerWindow:
            self.registerWindow.destroy()
        # change buttons when authorization completed
        self.hideButtonsAndLabels([self.loginButton, self.registerButton])
        self.loggedUserLabel['text'] = username
        self.showButtonsAndLabels([[self.loggedUserLabel, (0, 0, "WE")], [self.logoutButton, (0, 3, "E")], [self.checkReservationsButton, (2, 0, "WE")], [self.reserveFlightButton, (3, 0, "WE")], [self.cancelReservationButton, (4, 0, "WE")]])

    def register(self, event=None):
        ic("Register")
        # close if open login panel
        if self.loginWindow:
            self.loginWindow.destroy()
        # open register panel
        self.registerWindow, self.registerPanel = self.initNewWindow(self.root, size=[600, 675], title="Panel rejestracyjny")
        self.usernameLabel = self.createLabel(self.registerPanel, "Nazwa użytkownika*", grid=[0, 0], sticky="W", pad=[0, 5], labelFont=[32, "bold"])
        self.usernameEntry = self.createEntry(self.registerPanel, grid=[1, 0], pad=[0, 5], entryFont=[24, "bold"])
        self.noUsernameError = self.createLabel(self.registerPanel, "", grid=[2, 0], sticky="WE", pad=[0, 5], fg='red', labelFont=[12, 'normal'])
        self.emailLabel = self.createLabel(self.registerPanel, "Email", grid=[3, 0], sticky="W", pad=[0, 5], labelFont=[32, "bold"])
        self.emailEntry = self.createEntry(self.registerPanel, grid=[4, 0], width=30, pad=[0, 5], entryFont=[20, 'normal'])
        self.emailError = self.createLabel(self.registerPanel, "", grid=[5, 0], sticky="WE", pad=[0, 5], fg='red', labelFont=[12, 'normal'])
        self.passwordLabel = self.createLabel(self.registerPanel, "Hasło*", grid=[6, 0], sticky="W", pad=[0, 5], labelFont=[32, "bold"])
        self.passwordEntry = self.createEntry(self.registerPanel, grid=[7, 0], show="*", entryFont=[24, "bold"])
        self.noPasswordError = self.createLabel(self.registerPanel, "", grid=[8, 0], sticky="WE", pad=[0, 5], fg='red', labelFont=[12, 'normal'])
        self.loginConfirmButton = self.createButton(self.registerPanel, text="Zarejestruj się", command=self.createUserInterface, grid=[9, 0], margin=[0, 5], buttonFont=[40, 'bold'])
        self.noAuthorizationError = self.createLabel(self.registerPanel, "", grid=[10, 0], sticky="WE", pad=[0, 5], fg='red', labelFont=[12, 'normal'])
        self.otherAuthenticationOptionLabel = self.createLabel(self.registerPanel, "Masz już konto? Zaloguj się.", grid=[11, 0], pad=[0, 5], fg="blue", cursor="hand2", bind=["<Button-1>", self.login], labelFont=[16, 'normal'])

    def login(self, event=None):
        ic("Login")
        # close if open register panel
        if self.registerWindow:
            self.registerWindow.destroy()
        # open login panel
        self.loginWindow, self.loginPanel = self.initNewWindow(self.root, size=[550, 550], title="Panel logowania")
        self.usernameLabel = self.createLabel(self.loginPanel, "Nazwa użytkownika", grid=[0, 0], sticky="W", pad=[0, 0], labelFont=[32, "bold"])
        self.usernameEntry = self.createEntry(self.loginPanel, grid=[1, 0], entryFont=[24, "bold"])
        self.noUsernameError = self.createLabel(self.loginPanel, "", grid=[2, 0], sticky="WE", pad=[0, 5], fg='red', labelFont=[12, 'normal'])
        self.passwordLabel = self.createLabel(self.loginPanel, "Hasło", grid=[3, 0], sticky="W", pad=[0, 0], labelFont=[32, "bold"])
        self.passwordEntry = self.createEntry(self.loginPanel, grid=[4, 0], show="*", entryFont=[24, "bold"])
        self.noPasswordError = self.createLabel(self.loginPanel, "", grid=[5, 0], sticky="WE", pad=[0, 10], fg='red', labelFont=[12, 'normal'])
        self.loginConfirmButton = self.createButton(self.loginPanel, text="Zaloguj się", command=self.validateUserInterface, grid=[6, 0], margin=[0, 10], buttonFont=[40, 'bold'])
        self.noAuthorizationError = self.createLabel(self.loginPanel, "", grid=[7, 0], sticky="WE", pad=[0, 0], fg='red', labelFont=[12, 'normal'])
        self.otherAuthenticationOptionLabel = self.createLabel(self.loginPanel, "Nie masz konta? Zarejestruj się.", grid=[8, 0], pad=[0, 10], fg="blue", cursor="hand2", bind=["<Button-1>", self.register], labelFont=[16, 'normal'])

    def logout(self):
        ic("Logout")
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.checkReservationsButton, self.reserveFlightButton, self.cancelReservationButton])
        self.showButtonsAndLabels([[self.loginButton, (0, 1, "E")], [self.registerButton, (0, 2, "E")]])
        self.logic.logoutUser()

    @staticmethod
    def initNewWindow(frame, size, title):
        window = Toplevel(frame)
        window.title(title)
        window.wm_attributes("-topmost", True)  # ustawia ponad innymi oknami
        window.grab_set()  # blokuje dostep do innych okien
        window.resizable(False, False)  # blokowanie zmiany rozmiaru
        xPosition = (window.winfo_screenwidth() // 2) - (size[0] // 2)
        yPosition = (window.winfo_screenheight() // 2) - (size[1] // 2)
        window.geometry(f"{size[0]}x{size[1]}+{xPosition}+{yPosition}")
        # vertical center elements space
        window.grid_rowconfigure(0, weight=1)  # Przestrzeń przed
        window.grid_rowconfigure(1, weight=0)  # Miejsce na elementy
        window.grid_rowconfigure(2, weight=1)  # Przestrzeń po
        # horizontally center elements space
        window.grid_columnconfigure(0, weight=1)  # Przestrzeń przed
        window.grid_columnconfigure(1, weight=0)  # Miejsce na elementy
        window.grid_columnconfigure(2, weight=1)  # Przestrzeń po
        # elements space in window
        loginPanel = AirportInterface.createLabel(window, "", grid=[1, 1])
        return window, loginPanel


    def createList(self, frame, headers):
        flightsLabel = AirportInterface.createLabel(frame, pack=[None, True, "both"], border=0)
        scrollbarFlights = Scrollbar(flightsLabel, orient=VERTICAL)
        columns = [f"c{i}" for i in range(1, len(headers) + 1)]
        flightList = ttk.Treeview(flightsLabel, column=columns, show='headings', yscrollcommand=scrollbarFlights)
        for index, header in enumerate(headers, start=1):
            flightList.column(f"#{index}", anchor=CENTER)
            flightList.heading(f"#{index}", text=header)
        scrollbarFlights.config(command=flightList.yview)
        scrollbarFlights.pack(side=RIGHT, fill=Y)
        flightList.pack(fill="both", expand=True)
        return flightsLabel, flightList

    @staticmethod
    def createEntry(frame, textvariable=None, validationcommand=None, width=20, grid=(0, 0), span=(1, 1), pad=(0, 0), sticky="WE", justify=CENTER, entryFont=(18, "bold"), show=None):
        entry = Entry(frame, width=width, textvariable=textvariable, validate='all', validatecommand=validationcommand, justify=justify, show=show)
        entry.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky, padx=pad[0], pady=pad[1])
        entry['font'] = font.Font(size=entryFont[0], weight=entryFont[1])
        return entry


    @staticmethod
    def createLabelFrame(frame, pad, side=None, fill="both", expand=False, text="", labelFont=[18, "bold"]):
        labelFrame = LabelFrame(frame, padx=pad[0], pady=pad[1], text=text)
        labelFrame.pack(side=side, fill=fill, expand=expand)
        labelFrame['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        return labelFrame

    @staticmethod
    def createLabel(frame, text='', grid=None, pack=None, sticky="WE", span=(1, 1), pad=[0, 0], labelFont=[18, "bold"], border=1, fg=None, cursor=None, bind=None):
        label = Label(frame, text=text, padx=pad[0], pady=pad[1], bd=border, fg=fg, cursor=cursor)
        if grid:
            label.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        if pack:
            label.pack(side=pack[0], expand=pack[1], fill=pack[2])
        label['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        if bind:
            label.bind(bind[0], bind[1])
        return label

    @staticmethod
    def createButton(frame, text, command, grid, sticky="WE", span=(1, 1), pad=[0, 0], margin=[0, 0], buttonFont=[18, "bold"]):
        button = Button(frame, text=text, command=command, padx=pad[0], pady=pad[1])
        button.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky, padx=margin[0], pady=margin[1])
        button['font'] = font.Font(size=buttonFont[0], weight=buttonFont[1])
        return button

    @staticmethod
    def showButtonsAndLabels(elementsWithGridPositions):
        for data in elementsWithGridPositions:
            data[0].grid(row=data[1][0], column=data[1][1], sticky=data[1][2])

    @staticmethod
    def hideButtonsAndLabels(elements):
        for element in elements:
            element.grid_forget()

    def manageMainFieldSpace(self):
        if self.flightsLabel:
            self.flightsLabel.destroy()
        if self.flightList:
            self.flightList.destroy()

    def checkFlightList(self):
        ic("Check flight list")
        self.manageMainFieldSpace()
        self.flightsLabel, self.flightList = self.createList(self.root, headers=["KOD LOTU", "LOTNISKO ODLOTU", "CZAS ODLOTU", "LOTNISKO DOCELOWE", "CZAS PRZYLOTU"])
        data = self.logic.getAllFlights()
        for flight in data:
            self.flightList.insert('', END, values=(flight['flightCode'], flight['departureAirport'], flight['departureTime'], flight['destinationAirport'], flight['arrivalTime']))

    def findFlight(self):
        departureAirport = self.fromAirportVar.get()
        destinationAirport = self.toAirportVar.get()
        ic("find flight", departureAirport, destinationAirport)
        self.manageMainFieldSpace()
        self.flightsLabel, self.flightList = self.createList(self.root, headers=["KOD LOTU", "LOTNISKO ODLOTU", "CZAS ODLOTU", "LOTNISKO DOCELOWE", "CZAS PRZYLOTU"])
        data = self.logic.getFlightsWithParameters(departureAirport=departureAirport, destinationAirport=destinationAirport, departureTime=None, arrivalTime=None)
        for flight in data:
            self.flightList.insert('', END, values=(flight['flightCode'], flight['departureAirport'], flight['departureTime'], flight['destinationAirport'], flight['arrivalTime']))



    def checkReservationList(self):
        ic("Check reservation list")

    def reserveFlight(self):
        ic("reserve flight")

    def cancelReservation(self):
        ic("Anuluj rezerwacje")




if __name__ == "__main__":
    rootInterface = Tk()
    app = AirportInterface(rootInterface, AirportLogic(AirportClient(8080, [8085], "localhost", "SoapProject/AirportServerImplService")))
    rootInterface.mainloop()


