# JavaSoapProject
___
**Zalecane wersje Java 8, Payara 5.2022.5, SoapUi-4.6.4, baza danych H2 1.4.200**
___
1) System rezerwacji biletów lotniczych


 - Ustawienie/sprawdzenie połączenia z bazą danych przez Inteliji       
![Alt text](screens/ustawienaPolaczeniaBazyWInteliji.png?raw=true "Polaczenie z baza danych przez Inteliji")    
 - Tworzenie lotów:
   - INSERT INTO Flight (ID, FLIGHTCODE, DEPARTUREAIRPORT, DEPARTURETIME, DESTINATIONAIRPORT, ARRIVALTIME, CREATEDATE, UPDATEDATE)      
     SELECT *

     FROM CSVREAD('D:/programowanie/java/rsi/SoapProject/createDatabaseCSV/flights.csv', null);

