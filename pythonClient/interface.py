from tkinter import *
from tkinter import ttk
import tkcalendar as tkc
import tkinter.font as font
import customtkinter as ctk
from PIL import Image
from datetime import datetime, timedelta
from icecream import ic
import re

from logic import AirportLogic
from client import AirportClient


class AirportInterface:
    def __init__(self, root, logicClass):
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure("Treeview.Heading", font=(None, 18, "bold"))
        self.style.configure("Treeview", font=("Courier New", 16, "bold"), rowheight=int(16 * 2))
        self.root = root
        self.logic = logicClass
        self.root.title("Airport interface")
        self.root.iconbitmap('..\\images\\icons\\planeWorld.ico')
        boldFont18 = font.Font(size=18, weight="bold")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        root.state("zoomed")
        # Top frame, its weights and buttons login, register, logout
        self.topFrame = self.createLabelFrame(self.root, pad=[10, 10], pack=["top", False, "both"])
        self.topFrame.grid_columnconfigure(0, weight=1)  # Kolumna do rozciągania
        self.topFrame.grid_columnconfigure(1, weight=0)  # Kolumna dla przycisku login
        self.topFrame.grid_columnconfigure(2, weight=0)  # Kolumna dla przycisku register
        self.loggedUserLabel = self.createLabel(self.topFrame, text="NAZWA UZYTKOWNIKA", grid=[0, 0], labelFont=[32, "bold"])
        self.loginButton = self.createButton(self.topFrame, text="Zaloguj się", command=self.login, pad=[20, 20], grid=[0, 1], buttonFont=[24, "bold"])
        self.registerButton = self.createButton(self.topFrame, text="Zarejestruj się", command=self.register, pad=[20, 20], grid=[0, 2], buttonFont=[24, "bold"])
        self.logoutButton = self.createButton(self.topFrame, text="Wyloguj się", command=self.logout, pad=[20, 20], grid=[0, 3], buttonFont=[24, "bold"])
        # Left frame buttons checkFlights, findFlight, reserve flight, cancel reservation
        self.leftFrame = self.createLabelFrame(self.root, pad=[0, 0], pack=["left", False, "both"])
        self.checkFlightsButton = self.createButton(self.leftFrame, text="Wszystkie loty", command=self.checkFlightList, pad=[10, 10], grid=[0, 0], buttonFont=[28, "bold"])
        self.findFlightLabel = self.createLabelFrame(self.leftFrame, text='', grid=[1, 0], border=10)
        self.findFlightLabel.grid_columnconfigure(0, weight=1)
        self.findFlightButton = self.createButton(self.findFlightLabel, text="Wyszukaj lot", command=self.findFlight, grid=[0, 0], sticky="WE", span=(1, 2), pad=[10, 10], buttonFont=[28, "bold"])
        # dropdown departure city
        self.fromLabel = self.createLabel(self.findFlightLabel, "Lotnisko odlotu:", grid=[1, 0], labelFont=[16, "bold"])  # Lotnisko odlotu
        self.fromAirportVar = StringVar()
        self.options = [''] + self.logic.getAllAirports()
        self.fromDropdown = OptionMenu(self.findFlightLabel, self.fromAirportVar, *self.options)
        self.fromDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.fromDropdown['font'] = boldFont18
        self.fromDropdown.grid(row=1, column=1)
        # dropdown destination city
        self.toLabel = self.createLabel(self.findFlightLabel, "Lotnisko przylotu:", grid=[2, 0], labelFont=[16, "bold"])
        self.toAirportVar = StringVar()
        self.toDropdown = OptionMenu(self.findFlightLabel, self.toAirportVar, *self.options)
        self.toDropdown.config(width=12)  # Ustawienie stałej szerokości
        self.toDropdown['font'] = boldFont18
        self.toDropdown.grid(row=2, column=1)
        # start date entry
        self.startDateLabel = self.createLabel(self.findFlightLabel, "Od daty:", grid=[3, 0], labelFont=[18, "bold"])
        self.startDateEntry = tkc.DateEntry(self.findFlightLabel, date_pattern='d/m/yyyy')
        self.startDateEntry['font'] = boldFont18
        self.startDateEntry.grid(row=3, column=1)
        # end date entry
        self.endDateLabel = self.createLabel(self.findFlightLabel, "Do daty:", grid=[4, 0], labelFont=[18, "bold"])
        defaultEndDate = datetime.today() + timedelta(days=7)
        self.endDateEntry = tkc.DateEntry(self.findFlightLabel, date_pattern='d/m/yyyy', year=defaultEndDate.year, month=defaultEndDate.month, day=defaultEndDate.day)
        self.endDateEntry['font'] = boldFont18
        self.endDateEntry.grid(row=4, column=1)
        # show reservations
        self.checkReservationsButton = self.createButton(self.leftFrame, text="Moje rezerwacje", command=self.checkReservationList, pad=[10, 10], grid=[2, 0], buttonFont=[28, "bold"])
        # reserve button
        self.reserveFlightButton = self.createButton(self.leftFrame, text="Zarezerwuj lot", command=self.reserveFlight, pad=[10, 10], grid=[3, 0], buttonFont=[28, "bold"])
        # cancel reservation
        self.cancelReservationButton = self.createButton(self.leftFrame, text="Anuluj rezerwacje", command=self.cancelReservation, pad=[10, 10], grid=[4, 0], buttonFont=[28, "bold"])
        # generate pdf
        self.generatePDFButton = self.createButton(self.leftFrame, text="Odbierz potwierdzenie", command=self.generatePDF, pad=[5, 15], grid=[5, 0], buttonFont=[25, "bold"])
        # check reservation
        self.checkReservationButton = self.createButton(self.leftFrame, text="Sprawdź rezerwacje", command=self.checkReservation, pad=[10, 10], grid=[6, 0], buttonFont=[28, "bold"])
        # hide buttons which shouldn't be displayed to not logged user
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.checkReservationsButton, self.reserveFlightButton, self.cancelReservationButton, self.generatePDFButton, self.checkReservationButton])  # ukrycie przyciskow rezerwowania i usuwania rezerwacji
        # flights list
        self.mainFlightLabel, self.mainFlightList, self.mainReservationLabel, self.mainReservationList = [None] * 4
        # login panel variables
        self.loginWindow, self.loginPanel, self.usernameLabel, self.usernameEntry, self.passwordLabel, self.passwordEntry, self.loginConfirmButton, self.otherAuthenticationOptionLabel = [None] * 8
        # registration panel variables
        self.registerWindow, self.registerPanel, self.emailLabel, self.emailEntry, self.registerConfirmButton, self.loginOptionLabel = [None] * 6
        # errors in login or registration
        self.noUsernameError, self.emailError, self.noPasswordError, self.noAuthorizationError = [None] * 4
        # reservation operations window
        self.operationWindow = None
        # variable to store if user is logged in
        self.loggedIn = False

        # automatyczne zalogowanie na czes testow
        # self.logic.validateUser("rzymski", "Szumek19")
        # self.userAuthorizedInterface("rzymski")

    def validateUserProcessing(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        ic("Validate user", username, password)
        self.noUsernameError['text'] = "Pole 'nazwa użytkownika' jest wymagane." if not username else ""
        self.noPasswordError['text'] = "Pole 'hasło' jest wymagane." if not password else ""
        if self.logic.validateUser(username, password):
            self.userAuthorizedInterface(username)
        elif username and password:
            self.noAuthorizationError['text'] = "Nie udało się zalogować. Błędny login lub hasło"
        else:
            self.noAuthorizationError['text'] = ""

    def createUserProcessing(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        ic("Create user", username, password, email)
        self.noUsernameError['text'] = "Pole 'nazwa użytkownika' jest wymagane." if not username else ""
        self.noPasswordError['text'] = "Pole 'hasło' jest wymagane." if not password else ""
        correctEmail = True if re.match(r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) or not email else False
        self.emailError['text'] = "Niepoprawny format mail-a" if not correctEmail else ""
        if username and password and correctEmail:
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
        self.showButtonsAndLabels([[self.loggedUserLabel, (0, 0, "WE")], [self.logoutButton, (0, 3, "E")], [self.checkReservationsButton, (2, 0, "WE")], [self.reserveFlightButton, (3, 0, "WE")]])
        self.loggedIn = True

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
        self.loginConfirmButton = self.createButton(self.registerPanel, text="Zarejestruj się", command=self.createUserProcessing, grid=[9, 0], margin=[0, 5], buttonFont=[40, 'bold'])
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
        self.loginConfirmButton = self.createButton(self.loginPanel, text="Zaloguj się", command=self.validateUserProcessing, grid=[6, 0], margin=[0, 10], buttonFont=[40, 'bold'])
        self.noAuthorizationError = self.createLabel(self.loginPanel, "", grid=[7, 0], sticky="WE", pad=[0, 0], fg='red', labelFont=[12, 'normal'])
        self.otherAuthenticationOptionLabel = self.createLabel(self.loginPanel, "Nie masz konta? Zarejestruj się.", grid=[8, 0], pad=[0, 10], fg="blue", cursor="hand2", bind=["<Button-1>", self.register], labelFont=[16, 'normal'])

    def logout(self):
        ic("Logout")
        self.hideButtonsAndLabels([self.loggedUserLabel, self.logoutButton, self.checkReservationsButton, self.reserveFlightButton, self.cancelReservationButton, self.generatePDFButton, self.checkReservationButton])
        self.showButtonsAndLabels([[self.loginButton, (0, 1, "E")], [self.registerButton, (0, 2, "E")], [self.findFlightLabel, (1, 0, "WE")]])
        self.logic.logoutUser()
        self.manageMainFieldSpace()
        self.loggedIn = True

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
        windowMainLabel = AirportInterface.createLabel(window, "", grid=[1, 1])
        return window, windowMainLabel

    @staticmethod
    def createList(frame, headers, anchor=CENTER):
        mainLabel = AirportInterface.createLabel(frame, pack=[None, True, "both"], border=0)
        mainLabel.update()
        totalWidth = mainLabel.winfo_width()
        headerLengths = [len(header) for header in headers]
        totalHeaderLength = sum(headerLengths)
        scrollbarFlights = Scrollbar(mainLabel, orient=VERTICAL)
        columns = [f"c{i}" for i in range(1, len(headers) + 1)]
        mainList = ttk.Treeview(mainLabel, column=columns, show='headings', yscrollcommand=scrollbarFlights)
        for index, header in enumerate(headers, start=1):
            percentageOfWidth = headerLengths[index - 1] / totalHeaderLength
            mainList.column(f"#{index}", anchor=anchor, width=int(totalWidth * percentageOfWidth))
            mainList.heading(f"#{index}", text=header, anchor=anchor)
        mainList.column("c1", width=0, stretch=False)
        scrollbarFlights.config(command=mainList.yview)
        scrollbarFlights.pack(side=RIGHT, fill=Y)
        mainList.pack(fill="both", expand=True)
        return mainLabel, mainList

    @staticmethod
    def createEntry(frame, textVariable=None, validationCommand=None, width=20, grid=(0, 0), span=(1, 1), pad=(0, 0), sticky="WE", justify=CENTER, entryFont=(18, "bold"), show=None):
        entry = Entry(frame, width=width, textvariable=textVariable, validate='all', validatecommand=validationCommand, justify=justify, show=show)
        entry.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky, padx=pad[0], pady=pad[1])
        entry['font'] = font.Font(size=entryFont[0], weight=entryFont[1])
        return entry

    @staticmethod
    def createLabelFrame(frame, text='', grid=None, pack=None, sticky="WE", span=(1, 1), pad=(0, 0), border=1, labelFont=(18, "bold")):
        labelFrame = LabelFrame(frame, padx=pad[0], pady=pad[1], text=text, bd=border)
        if grid:
            labelFrame.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        if pack:
            labelFrame.pack(side=pack[0], expand=pack[1], fill=pack[2])
        labelFrame['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        return labelFrame

    @staticmethod
    def createLabel(frame, text='', grid=None, pack=None, sticky="WE", span=(1, 1), pad=(0, 0), labelFont=(18, "bold"), border=1, fg=None, bg=None, cursor=None, bind=None):
        label = Label(frame, text=text, padx=pad[0], pady=pad[1], bd=border, fg=fg, bg=bg, cursor=cursor)
        if grid:
            label.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky)
        if pack:
            label.pack(side=pack[0], expand=pack[1], fill=pack[2])
        label['font'] = font.Font(size=labelFont[0], weight=labelFont[1])
        if bind:
            label.bind(bind[0], bind[1])
        return label

    @staticmethod
    def createButton(frame, text, command, grid, sticky="WE", span=(1, 1), pad=(0, 0), margin=(0, 0), buttonFont=(18, "bold")):
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
        if self.mainFlightLabel:
            self.mainFlightLabel.destroy()
            self.mainFlightLabel = None
        if self.mainFlightList:
            self.mainFlightList.destroy()
            self.mainFlightList = None
        if self.mainReservationLabel:
            self.mainReservationLabel.destroy()
            self.mainReservationLabel = None
        if self.mainReservationList:
            self.mainReservationList.destroy()
            self.mainReservationList = None

    def manageMainList(self, flightsData=None, reservationsData=None):
        self.manageMainFieldSpace()
        if flightsData:
            self.hideButtonsAndLabels([self.cancelReservationButton, self.generatePDFButton, self.checkReservationButton])
            self.showButtonsAndLabels([[self.findFlightLabel, (1, 0, "WE")]])
            self.reserveFlightButton['text'] = "Zarezerwuj lot"
            # self.mainFlightLabel, self.mainFlightList = self.createList(self.root, headers=["ID", "KOD", "Z", "ODLOT O", "DO", "PRZYLOT O"])
            self.mainFlightLabel, self.mainFlightList = self.createList(self.root, headers=["ID", "KOD LOTU", "ODLOT Z", "CZAS ODLOTU", "PRZYLOT DO", "CZAS PRZYLOTU"])
            self.mainFlightList.bind("<Double-1>", self.reserveFlight)
            for flight in flightsData:
                self.mainFlightList.insert('', END, values=(flight["id"], flight['flightCode'], flight['departureAirport'], flight['departureTime'], flight['destinationAirport'], flight['arrivalTime']))
        if reservationsData:
            self.hideButtonsAndLabels([self.findFlightLabel])
            self.showButtonsAndLabels([[self.cancelReservationButton, (4, 0, "WE")], [self.generatePDFButton, (5, 0, "WE")], [self.checkReservationButton, (6, 0, "WE")]])
            self.reserveFlightButton['text'] = "Zmien rezerwacje"
            self.mainReservationLabel, self.mainReservationList = self.createList(self.root, headers=["ID", "ID ", "KOD LOTU", "KIERUNEK LOTU", "CZAS ODLOTU", "MIEJSCA"], anchor="w")
            self.mainReservationList.bind("<Double-1>", self.reservationOperations)
            for reservation in reservationsData:
                self.mainReservationList.insert('', END, values=(reservation["id"], reservation['reservationId'], reservation['flightCode'], reservation['airports'], reservation['dates'], reservation['seats']))

    def checkFlightList(self):
        ic("Check flight list")
        flights = self.logic.getAllFlights()
        self.manageMainList(flightsData=flights)

    def findFlight(self):
        departureAirport = self.fromAirportVar.get()
        destinationAirport = self.toAirportVar.get()
        departureTime = self.startDateEntry.get_date().strftime(AirportLogic.javaDateFormat)
        arrivalTime = self.endDateEntry.get_date().strftime(AirportLogic.javaDateFormat)
        ic("find flight", departureAirport, destinationAirport, departureTime, arrivalTime)
        flights = self.logic.getFlightsWithParameters(departureAirport=departureAirport, destinationAirport=destinationAirport, departureTime=departureTime, arrivalTime=arrivalTime)
        self.manageMainList(flightsData=flights)

    def reserveFlight(self, event=None):
        ic("reserve flight")
        if not self.loggedIn:
            return None
        if self.mainFlightList:
            ic("Wybierz z listy lotow")
            selectedFlight = self.mainFlightList.selection()
            if selectedFlight:
                item = self.mainFlightList.item(selectedFlight[0])
                self.addEditReservation(item)
        elif self.mainReservationList:
            ic("Wybierz z listy rezerwacji")
            selectedReservation = self.mainReservationList.selection()
            if selectedReservation:
                item = self.mainReservationList.item(selectedReservation[0])
                self.addEditReservation(item, True)
        else:
            return None

    @staticmethod
    def validateEntryNumberRange(P, numberRange=[]):
        if P == "" or (str.isdigit(P) and (not numberRange or numberRange[0] <= int(P) <= numberRange[1])):
            return True
        else:
            return False

    def addEditReservation(self, item, reservationExist=False):
        flightId = item['values'][0]
        # alreadyReservedSeats = item['values'][5].split('/')[0] if reservationExist else ""
        alreadyReservedSeats = item['values'][5] if reservationExist else ""
        ic(alreadyReservedSeats)
        numberOfAvailableSeats = self.logic.numberOfAvailableSeatsInFlight(flightId)
        reserveFlightWindow, reserveFlightPanel = self.initNewWindow(self.root, [500, 250], "Dodaj rezerwacje")
        validateCommand = (reserveFlightPanel.register(lambda P: self.validateEntryNumberRange(P, [1, int(numberOfAvailableSeats)])), '%P')
        numberOfSeatsLabel = self.createLabel(reserveFlightPanel, "Ile chcesz zarezerwować miejsc?", grid=[0, 0], sticky="W", pad=[0, 0], span=(1, 2), labelFont=[18, "bold"])
        numberOfSeatsEntry = self.createEntry(reserveFlightPanel, width=3, grid=[1, 0], entryFont=[32, "bold"], sticky="E", validationCommand=validateCommand)
        numberOfSeatsEntry.insert(0, alreadyReservedSeats)
        availableSeats = self.createLabel(reserveFlightPanel, f"/ {numberOfAvailableSeats}", grid=[1, 1], sticky="W", pad=[0, 0], labelFont=[32, "bold"])
        loginConfirmButton = self.createButton(reserveFlightPanel, text="Zarezerwuj miejsca", command=lambda: self.reserveFlightProcessing(flightId, numberOfSeatsEntry.get(), reserveFlightWindow), grid=[2, 0], span=(1, 2), margin=[0, 10], buttonFont=[32, 'bold'])

    def reserveFlightProcessing(self, flightId, numberOfReservedSeats, window):
        ic("reserve flight processing")
        if self.logic.reserveFlight(flightId, int(numberOfReservedSeats)):
            window.destroy()
            self.checkReservationList()

    def checkReservationList(self):
        ic("Check reservation list")
        reservations = self.logic.getFlightReservations()
        self.manageMainList(reservationsData=reservations)

    def getSelectedReservation(self):
        if not self.mainReservationList:
            return None
        selectedReservation = self.mainReservationList.selection()
        if selectedReservation:
            return self.mainReservationList.item(selectedReservation[0])['values'][1]
        return 0

    def cancelReservation(self, event=None):
        ic("Anuluj rezerwacje")
        reservationId = self.getSelectedReservation()
        if reservationId:
            self.logic.cancelReservation(reservationId)
            self.checkReservationList()

    def generatePDF(self, event=None):
        ic("Generate pdf")
        reservationId = self.getSelectedReservation()
        if reservationId:
            self.logic.generatePDF(reservationId)

    def checkReservation(self, event=None):
        ic("Check reservation")
        reservationId = self.getSelectedReservation()
        if reservationId:
            reservationData = self.logic.checkReservation(reservationId)
            reservationWindow, reservationMainLabel = self.initNewWindow(self.root, [500, 500], f"Wszystkie dane rezerwacji {reservationId}")
            for i, (key, value) in enumerate(reservationData.items()):
                self.createLabel(reservationMainLabel, text=f"{key}: {value}", grid=[i, 0], sticky="W")

    @staticmethod
    def createCtkButton(frame, text, command, grid, sticky="WE", span=(1, 1), margin=(0, 0), imagePath=None, imageSize=(100, 100), imageSide="top", buttonSize=(150, 150), textColor="white", fg="red", hg=None):
        image = ctk.CTkImage(light_image=Image.open(imagePath), size=imageSize) if imagePath else None
        button = ctk.CTkButton(master=frame, text=text, command=command, image=image, compound=imageSide, width=buttonSize[0], height=buttonSize[1], text_color=textColor, fg_color=fg, hover_color=hg)
        button.grid(row=grid[0], column=grid[1], rowspan=span[0], columnspan=span[1], sticky=sticky, padx=margin[0], pady=margin[1])
        return button

    def reservationOperations(self, event=None):
        ic("Reservation operations")
        reservationId = self.getSelectedReservation()
        if reservationId:
            self.operationWindow, operationMainLabel = self.initNewWindow(self.root, [450, 450], f"Dostepne operacje na rezerwacji {reservationId}")
            infoButton = self.createCtkButton(operationMainLabel, "Szczegółowe dane", lambda func=self.checkReservation: self.doReservationOperation(func), grid=(0, 0), imagePath="..\\images\\info.png", margin=(25, 25), fg="#0000FF", hg="#0000A0")
            pdfButton = self.createCtkButton(operationMainLabel, "Generuj pdfa", lambda func=self.generatePDF: self.doReservationOperation(func), grid=(0, 1), imagePath="..\\images\\pdf.png", margin=(25, 25), fg="#FF0000", hg="#C00000")
            editButton = self.createCtkButton(operationMainLabel, "Edytuj rezerwacje", lambda func=self.reserveFlight: self.doReservationOperation(func), grid=(1, 0), imagePath="..\\images\\edit.png", margin=(25, 25), fg="#FFAC1C", hg="#E3963E")
            cancelButton = self.createCtkButton(operationMainLabel, "Usuń rezerwacje", lambda func=self.cancelReservation: self.doReservationOperation(func), grid=(1, 1), imagePath="..\\images\\trash.png", margin=(25, 25), fg="#000000", hg="#202020")

    def doReservationOperation(self, operationFunction, event=None):
        self.operationWindow.destroy()
        operationFunction()


if __name__ == "__main__":
    rootInterface = Tk()
    app = AirportInterface(rootInterface, AirportLogic(AirportClient(8080, [], "localhost", "SoapProject/AirportServerImplService")))
    rootInterface.mainloop()