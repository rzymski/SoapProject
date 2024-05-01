___
**Zalecane wersje Java 8, Payara 5.2022.5, SoapUi-4.6.4, baza danych H2 1.4.200, IDE Inteliji Ultimate**
___

## Zawartość REDME
1. :airplane: [Funkcjonalność](#funkcjonalność)
2. :computer: [Działanie serwera](#działanie-serwera)
3. 📦 [Instalacja](#instrukcja-instalacji)
4. :wrench: [Konfiguracja serwera](#instrukcja-konfiguracji-serwera)
5. :satellite: [Modyfikowanie bazy danych](#użycie-konsoli-inteliji-do-modyfikowania-bazy-danych)
6. :eyes: [Monitorowanie requestów](#instrukcja-monitorowania-requestów)
7. :dragon: [Konfiguracja klienta w pythonie](#instrukcja-konfiguracji-klienta)
8. :file_folder: [Struktura projektu](#struktura-projektu)
9. :white_check_mark: [Wskazówki](#wskazówki-użycia)

# Funkcjonalność
**System rezerwacji biletów lotniczych**
1) [x] Baza lotów (Miasto od , Miasto do, dzień, godzina)
2) [x] Wyszukiwanie lotów
3) [x] Kupno biletu
4) [x] Odbiór potwierdzenia kupna w formacie PDF
5) [x] Sprawdzenie rezerwacji na podstawie podanego numeru

# Działanie Serwera
Można sprawdzić działanie serwera w:  
- http://localhost:8080/SoapProject/AirportServerImplService

WSDL:  
- http://localhost:8080/SoapProject/AirportServerImplService?WSDL

Tester Glassfisha:  
- http://localhost:8080/SoapProject/AirportServerImplService?Tester

# Instrukcja instalacji
Linki do pobrania Payary 5.2022.5 i H2 1.4.200
- Serwer Payara 5.2022.5: [Payara 5.2022.5](https://nexus.payara.fish/#browse/browse:payara-community:fish%2Fpayara%2Fdistributions%2Fpayara%2F5.2022.5%2Fpayara-5.2022.5.zip)
- Baza danych H2 1.4.200: [H2 1.4.200](https://www.h2database.com/html/download-archive.html)

Dodanie Payary do Inteliji:        
Edit configurations... -> + -> Glassfish server Local -> Configure          
![Alt text](screens/ustawienieServeraPayarawInteliji.png?raw=true "ustawienie Servera Payara w Inteliji.png")

Wymagane pluginy w Inteliji **GlassFish**, **Maven** i **Maven Extension**:       
File -> Settings -> Plugins          
![Alt text](screens/plugins.jpg?raw=true "Pluginy")

# Instrukcja konfiguracji serwera
> [!Important]
> ### Ustawiamy ścieżke do naszej bazy danych w:
> [SoapProject/src/main/java/database/Configuration.java](https://github.com/rzymski/SoapProject/blob/master/SoapProject/src/main/java/database/Configuration.java) ${\textsf{\color{gold}@DataSourceDefinition}}$ **`url`**

> [!Note]
> ### Ustawiamy ścieżke do obrazka, który ma być w pdf-ie w:
> [SoapProject/src/main/java/soap/service/AirportServerImpl.java](https://github.com/rzymski/SoapProject/blob/master/SoapProject/src/main/java/soap/service/AirportServerImpl.java) ${\textsf{\color{red}generatePdf(Long reservationId)}}$ **`imagePath`** 

W projekcie trzeba ustawić Jave 8:       
File -> Project Structure...:       
![Alt text](screens/projectStructure.png?raw=true "Project Structure")

Maven Lifecycle wyczyszczenie i zbudowanie projektu:         
View -> Tool Windows -> Maven -> SoapProject -> Lifecycle i klikamy **clean**, a następnie **package**          
![Alt text](screens/maven.jpg?raw=true "Pluginy")

Konfiguracja Payary:          
![Alt text](screens/payaraConfigurationCz1.png?raw=true "Payara cz.1")
![Alt text](screens/payaraConfigurationCz2.png?raw=true "Payara cz.2")
![Alt text](screens/payaraConfigurationCz3.png?raw=true "Payara cz.3")

Ustawienie/sprawdzenie połączenia z bazą danych przez Inteliji:       
View -> Tool Windows -> Database -> + -> Data Source -> H2       
![Alt text](screens/ustawienaPolaczeniaBazyWInteliji.png?raw=true "Polaczenie z baza danych przez Inteliji")

# Użycie konsoli Inteliji do modyfikowania bazy danych
#### Uruchomienie konsoli Inteliji
View -> Tool Windows -> Database -> wybieramy naszą baze danych np. airport -> QL -> Open Default Console

#### Tworzenie lotów w bazie za pomocą CSV:
```sh
INSERT INTO Flight (ID, FLIGHTCODE, DEPARTUREAIRPORT, DEPARTURETIME, DESTINATIONAIRPORT, ARRIVALTIME, CREATEDATE, UPDATEDATE, CAPACITY, OCCUPIEDSEATS)          
SELECT *
FROM CSVREAD('D:/programowanie/java/rsi/SoapProject/createDatabaseCSV/flights.csv', null);
```

# Instrukcja monitorowania requestów
Ustawienie **`SoapUi HTTP Proxy`** na porcie **8085**:      

![Alt text](screens/soapUiUstawieniePort8085.png?raw=true "Ustawienie SoapUi HTTP Proxy na porcie 8085")  

Przykładowe działanie **`SoapUi HTTP Proxy`** na porcie **8085**:

![Alt text](screens/soapUiDzialaPort8085.png?raw=true "Przykładowe działanie SoapUi HTTP Proxy na porcie 8085")

<br>

Ustawienie **`tcpMonitor`**-a na porcie **8084**:      

![Alt text](screens/tcpMonitorUstawieniePort8084.png?raw=true "Ustawienie tcpMonitor-a na porcie 8084")      

Przykładowe działanie **`tcpMonitor`**-a na porcie **8084**:

![Alt text](screens/tcpMonitorDzialaPort8084.png?raw=true "Przykładowe działanie tcpMonitor-a na porcie 8084")      

# Instrukcja konfiguracji klienta
Przechodzimy w konsoli do folderu **`pythonClient`**

Tworzymy wirtualne środowisko
```sh
python -m venv venv
```

Aktywujemy wirtualne środowisko
```sh
.\venv\Scripts\activate
```
Instalujemy wszystkie potrzebne biblioteki z pliku `requirements.txt`
```sh
pip install -r .\requirements.txt
```

# Struktura projektu
### Ogólna struktura całego projektu
```
.
├───createDatabaseCSV
│   └───pythonScriptToCreateCSV
├───pdfs
├───pythonClient
├───screens
├───SoapProject
│   └───src
│       └───main
│           ├───java
│           │   ├───database
│           │   │   ├───adapter
│           │   │   ├───dao
│           │   │   ├───dto
│           │   │   ├───exceptions
│           │   │   ├───model
│           │   │   └───service
│           │   ├───pdfGenerator
│           │   └───soap
│           │       ├───handler
│           │       └───service
│           ├───resources
│           │   └───META-INF
│           └───webapp
│               └───WEB-INF
└───tcpMonitor
```

### Struktura serwera javy w **`SoapProject`**
<!--- W cmd: tree /F  --->
```
SoapProject
│   airport.mv.db
│   pom.xml
└───src
    └───main
        ├───java
        │   ├───database
        │   │   │   Configuration.java
        │   │   ├───adapter
        │   │   │       LocalDateTimeAdapter.java
        │   │   ├───dao
        │   │   │       AbstractDao.java
        │   │   │       AbstractDaoJpaImpl.java
        │   │   │       FlightDao.java
        │   │   │       FlightDaoImpl.java
        │   │   │       FlightReservationDao.java
        │   │   │       FlightReservationDaoImpl.java
        │   │   │       UserDao.java
        │   │   │       UserDaoImpl.java
        │   │   │       UserGroupDao.java
        │   │   │       UserGroupDaoImpl.java
        │   │   ├───dto
        │   │   │       FlightDTO.java
        │   │   │       FlightReservationDTO.java
        │   │   ├───exceptions
        │   │   │       NotEnoughDataException.java
        │   │   │       RecordNotFoundException.java
        │   │   │       UserNotFoundException.java
        │   │   ├───model
        │   │   │       AbstractModel.java
        │   │   │       Flight.java
        │   │   │       FlightReservation.java
        │   │   │       User.java
        │   │   │       UserGroup.java
        │   │   └───service
        │   │           FlightReservationService.java
        │   │           FlightReservationServiceImpl.java
        │   │           FlightService.java
        │   │           FlightServiceImpl.java
        │   │           UserService.java
        │   │           UserServiceImpl.java
        │   ├───pdfGenerator
        │   │       HeaderFooterEventHandler.java
        │   │       PdfGenerator.java
        │   └───soap
        │       ├───handler
        │       │       LoginHandler.java
        │       └───service
        │               AirportServer.java
        │               AirportServerImpl.java
        ├───resources
        │   │   loginHandler.xml
        │   └───META-INF
        │           persistence.xml
        └───webapp
            │   index.xhtml
            └───WEB-INF
                    web.xml
```


```mermaid
graph TD;
   A[SoapProject]-->B[src];
   A[SoapProject]-->|baza danych| C[airport.mv.db];
   B-->M[main];
   M-->J[java];
   M-->R[resources];
   M-->W[webapp];
   J-->D[database];
   D-->model;
   D-->dao;
   D-->SD[service];
   D-->adapter;
   D-->dto;
   D-->exceptions;
   J-->pdfGenerator;
   J-->S[soap];
   S-->handler;
   S-->SS[service];
   R-->META-INF;
   W-->WEB-INF;
```

# Wskazówki użycia
> [!Tip]
> <details>
>  <summary>Wskazówki</summary>
>
>  ###
>  01. :white_check_mark: &nbsp; Baza danych nie może być otwarta w tym samym momencie przez aplikacje i konsole Inteliji 
