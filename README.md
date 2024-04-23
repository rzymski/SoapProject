___
**Zalecane wersje Java 8, Payara 5.2022.5, SoapUi-4.6.4, baza danych H2 1.4.200, IDE Inteliji Ultimate**
___
# Funkcjonalność

**System rezerwacji biletów lotniczych**
1) [x] Baza lotów (Miasto od , Miasto do, dzień, godzina)
2) [x] Wyszukiwanie lotów
3) [ ] Kupno biletu
4) [ ] Odbiór potwierdzenia kupna w formacie PDF
5) [ ] Sprawdzenie rezerwacji na podstawie podanego numeru

# Działanie Serwera
Można sprawdzić działanie serwera w:  
- http://localhost:8080/SoapProject/AirportServerImplService

WSDL:  
- http://localhost:8080/SoapProject/AirportServerImplService?WSDL

Tester Glassfisha:  
- http://localhost:8080/SoapProject/AirportServerImplService?Tester

# Instrukcja instalacji
Linki do pobrania Payary 5.2022.5 i H2 1.4.200
- Payara 5.2022.5 https://nexus.payara.fish/#browse/browse:payara-community:fish%2Fpayara%2Fdistributions%2Fpayara%2F5.2022.5%2Fpayara-5.2022.5.zip
- H2 1.4.200 https://www.h2database.com/html/download-archive.html

Dodanie Payary do Inteliji:        
Edit configurations... -> + -> Glassfish server Local -> Configure          
![Alt text](screens/ustawienieServeraPayarawInteliji.png?raw=true "ustawienie Servera Payara w Inteliji.png")

Wymagane pluginy w Inteliji **GlassFish**, **Maven** i **Maven Extension**:       
File -> Settings -> Plugins          
![Alt text](screens/plugins.jpg?raw=true "Pluginy")

# Instrukcja konfiguracji
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

# Instrukcja dodawania rekordów do bazy przez konsole Inteliji
View -> Tool Windows -> Database -> wybieramy naszą baze danych np. airport -> Open Default Console
Tworzenie lotów w bazie za pomocą CSV:
   - INSERT INTO Flight (ID, FLIGHTCODE, DEPARTUREAIRPORT, DEPARTURETIME, DESTINATIONAIRPORT, ARRIVALTIME, CREATEDATE, UPDATEDATE, CAPACITY, OCCUPIEDSEATS)          
     SELECT *

     FROM CSVREAD('D:/programowanie/java/rsi/SoapProject/createDatabaseCSV/flights.csv', null);

