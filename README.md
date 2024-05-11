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
10. :godmode: [WSDL](#wsdl)

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

<h3><details>
    <summary>Dodanie Payary do Inteliji:</summary>
        Edit configurations... -> + -> Glassfish server Local -> Configure          
        <img src="screens/ustawienieServeraPayarawInteliji.png?raw=true" alt="ustawienie Servera Payara w Inteliji.png">
</details></h3>

<h3><details>
    <summary>Wymagane pluginy w Inteliji <b>GlassFish</b>, <b>Maven</b> i <b>Maven Extension</b>: </summary>      
        File -> Settings -> Plugins          
        <img src="screens/plugins.jpg?raw=true" alt="Pluginy">
</details></h3>

# Instrukcja konfiguracji serwera
> [!Important]
> ### Ustawiamy ścieżke do naszej bazy danych w:
> [SoapProject/src/main/java/database/Configuration.java](https://github.com/rzymski/SoapProject/blob/master/SoapProject/src/main/java/database/Configuration.java) ${\textsf{\color{gold}@DataSourceDefinition}}$ **`url`**

<details>
  <summary>Kod <b><code>@DataSourceDefinition</code></b> zawierający <b>url</b> do bazy danych</summary>

  ```java
  @DataSourceDefinition(
        name = "java:global/SoapProjectDataSource",
        className = "org.h2.jdbcx.JdbcDataSource",
        url = "jdbc:h2:file:yourPath/SoapProject/SoapProject/airport",
        minPoolSize = 1,
        initialPoolSize = 1,
        user = "sa",
        password = ""
    )
  @FacesConfig
  @Singleton
  @Startup
  public class Configuration {
  ```
</details>

> [!Note]
> ### Ustawiamy ścieżke do obrazka, który ma być w pdf-ie w:
> [SoapProject/src/main/java/soap/service/AirportServerImpl.java](https://github.com/rzymski/SoapProject/blob/master/SoapProject/src/main/java/soap/service/AirportServerImpl.java) ${\textsf{\color{red}generatePdf(Long reservationId)}}$ **`imagePath`** 

<details>
  <summary>Kod <b><code>generatePdf</code></b> zawierający <b>url</b> do pliku obrazka</summary>

  ```java
@Override
public byte[] generatePdf(Long reservationId) throws IOException {
    FlightReservationDTO res = checkFlightReservation(reservationId);
    if (res == null) {
        throw new RecordNotFoundException("No reservation with ID: " + reservationId);
    }
    ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
    PdfGenerator pdfGenerator = new PdfGenerator(byteArrayOutputStream, res);
    pdfGenerator.setHeaderFooter("Potwierdzenie rezerwacji biletu", "Super linie lotnicze sp. z o.o.");
    String imagePath = "youPath\\SoapProject\\screens\\plane.png";
    pdfGenerator.setImage(imagePath);
    pdfGenerator.generate();
    return byteArrayOutputStream.toByteArray();
}
  ```
</details>

<h3><details>
    <summary>Ustawienie Javy 8</summary>
        File -> Project Structure...:
        <img src="screens/projectStructure.png?raw=true" alt="Project Structure">
</details></h3>

<h3><details>
    <summary>Maven Lifecycle wyczyszczenie i zbudowanie projektu:</summary>
        View -> Tool Windows -> Maven -> SoapProject -> Lifecycle i klikamy <b>clean</b>, a następnie <b>package</b><br>
        <img src="screens/maven.jpg?raw=true" alt="Maven lifecycle clean and package">
</details></h3>

<h3><details>
    <summary>Konfiguracja Payary: </summary>
        <img src="screens/payaraConfigurationCz1.png?raw=true" alt="Payara cz.1">
        <img src="screens/payaraConfigurationCz2.png?raw=true" alt="Payara cz.2">
        <img src="screens/payaraConfigurationCz3.png?raw=true" alt="Payara cz.3">
</details></h3>

<h3><details>
    <summary>Ustawienie/sprawdzenie połączenia z bazą danych przez Inteliji: </summary>
        View -> Tool Windows -> Database -> + -> Data Source -> H2
        <img src="screens/ustawienaPolaczeniaBazyWInteliji.png?raw=true" alt="Polaczenie z baza danych przez Inteliji">
</details></h3>

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


<h3><details>
    <summary>Ustawienie <b><code>SoapUi HTTP Proxy</code></b> na porcie <b>8085</b>:</summary>
        <img src="screens/soapUiUstawieniePort8085.png?raw=true" alt="Ustawienie SoapUi HTTP Proxy na porcie 8085">
</details></h3>

<h3><details>
    <summary>Przykładowe działanie <b><code>SoapUi HTTP Proxy</code></b> na porcie <b>8085</b>:</summary>
        <img src="screens/soapUiDzialaPort8085.png?raw=true" alt="Przykładowe działanie SoapUi HTTP Proxy na porcie 8085">
</details></h3>

<h3><details>
    <summary>Ustawienie <b><code>tcpMonitor</code></b> na porcie <b>8084</b>:</summary>
        <img src="screens/tcpMonitorUstawieniePort8084.png?raw=true" alt="Ustawienie tcpMonitor-a na porcie 8084">
</details></h3>

<h3><details>
    <summary>Przykładowe działanie <b><code>tcpMonitor</code></b> na porcie <b>8084</b>:</summary>
        <img src="screens/tcpMonitorDzialaPort8084.png?raw=true" alt="Przykładowe działanie tcpMonitor-a na porcie 8084">
</details></h3>      

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
   A[SoapProject]-->C[(airport.mv.db)];
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

### Struktura klienta pythona w **`pythonCLient`**
```
pythonCLient
    client.py
    interface.py
    logic.py
    main.py
```

```mermaid
graph TD;
    A[pythonClient]-->M[main.py];
    A-->I[interface.py];
    A-->L[logic.py];
    A-->C[client.py];
```

# Wskazówki użycia
> [!Tip]
> <details>
>  <summary>Wskazówki</summary>
>
>  ###
>  01. :white_check_mark: &nbsp; Baza danych nie może być otwarta w tym samym momencie przez aplikacje i konsole Inteliji 

# WSDL
```xml
<definitions targetNamespace="http://service.soap/" name="AirportServerImplService">
	<wsp:Policy wsu:Id="AirportServerImplPortBinding_MTOM_Policy-AirportServerImplPortBinding_MTOM_Policy">
		<ns1:OptimizedMimeSerialization wsp:Optional="true"/>
	</wsp:Policy>
	<types>
		<xsd:schema>
			<xsd:import namespace="http://service.soap/" schemaLocation="http://localhost:8080/SoapProject/AirportServerImplService?xsd=1"/>
		</xsd:schema>
	</types>
	<message name="echo">
		<part name="parameters" element="tns:echo"/>
	</message>
	<message name="echoResponse">
		<part name="parameters" element="tns:echoResponse"/>
	</message>
	<message name="getFlightsData">
		<part name="parameters" element="tns:getFlightsData"/>
	</message>
	<message name="getFlightsDataResponse">
		<part name="parameters" element="tns:getFlightsDataResponse"/>
	</message>
	<message name="getFlightById">
		<part name="parameters" element="tns:getFlightById"/>
	</message>
	<message name="getFlightByIdResponse">
		<part name="parameters" element="tns:getFlightByIdResponse"/>
	</message>
	<message name="generatePdf">
		<part name="parameters" element="tns:generatePdf"/>
	</message>
	<message name="generatePdfResponse">
		<part name="parameters" element="tns:generatePdfResponse"/>
	</message>
	<message name="IOException">
		<part name="fault" element="tns:IOException"/>
	</message>
	<message name="reserveFlight">
		<part name="parameters" element="tns:reserveFlight"/>
	</message>
	<message name="reserveFlightResponse">
		<part name="parameters" element="tns:reserveFlightResponse"/>
	</message>
	<message name="createUser">
		<part name="parameters" element="tns:createUser"/>
	</message>
	<message name="createUserResponse">
		<part name="parameters" element="tns:createUserResponse"/>
	</message>
	<message name="getFlightAvailableSeats">
		<part name="parameters" element="tns:getFlightAvailableSeats"/>
	</message>
	<message name="getFlightAvailableSeatsResponse">
		<part name="parameters" element="tns:getFlightAvailableSeatsResponse"/>
	</message>
	<message name="findAvailableAirports">
		<part name="parameters" element="tns:findAvailableAirports"/>
	</message>
	<message name="findAvailableAirportsResponse">
		<part name="parameters" element="tns:findAvailableAirportsResponse"/>
	</message>
	<message name="checkFlightReservation">
		<part name="parameters" element="tns:checkFlightReservation"/>
	</message>
	<message name="checkFlightReservationResponse">
		<part name="parameters" element="tns:checkFlightReservationResponse"/>
	</message>
	<message name="cancelFlightReservation">
		<part name="parameters" element="tns:cancelFlightReservation"/>
	</message>
	<message name="cancelFlightReservationResponse">
		<part name="parameters" element="tns:cancelFlightReservationResponse"/>
	</message>
	<message name="getUserReservations">
		<part name="parameters" element="tns:getUserReservations"/>
	</message>
	<message name="getUserReservationsResponse">
		<part name="parameters" element="tns:getUserReservationsResponse"/>
	</message>
	<message name="getAllFlightsWithParameters">
		<part name="parameters" element="tns:getAllFlightsWithParameters"/>
	</message>
	<message name="getAllFlightsWithParametersResponse">
		<part name="parameters" element="tns:getAllFlightsWithParametersResponse"/>
	</message>
	<message name="cancelUserReservationInConcreteFlight">
		<part name="parameters" element="tns:cancelUserReservationInConcreteFlight"/>
	</message>
	<message name="cancelUserReservationInConcreteFlightResponse">
		<part name="parameters" element="tns:cancelUserReservationInConcreteFlightResponse"/>
	</message>
	<portType name="AirportServer">
		<operation name="echo">
			<input wsam:Action="http://service.soap/AirportServer/echoRequest" message="tns:echo"/>
			<output wsam:Action="http://service.soap/AirportServer/echoResponse" message="tns:echoResponse"/>
		</operation>
		<operation name="getFlightsData">
			<input wsam:Action="http://service.soap/AirportServer/getFlightsDataRequest" message="tns:getFlightsData"/>
			<output wsam:Action="http://service.soap/AirportServer/getFlightsDataResponse" message="tns:getFlightsDataResponse"/>
		</operation>
		<operation name="getFlightById">
			<input wsam:Action="http://service.soap/AirportServer/getFlightByIdRequest" message="tns:getFlightById"/>
			<output wsam:Action="http://service.soap/AirportServer/getFlightByIdResponse" message="tns:getFlightByIdResponse"/>
		</operation>
		<operation name="generatePdf">
			<input wsam:Action="http://service.soap/AirportServer/generatePdfRequest" message="tns:generatePdf"/>
			<output wsam:Action="http://service.soap/AirportServer/generatePdfResponse" message="tns:generatePdfResponse"/>
			<fault message="tns:IOException" name="IOException" wsam:Action="http://service.soap/AirportServer/generatePdf/Fault/IOException"/>
		</operation>
		<operation name="reserveFlight">
			<input wsam:Action="http://service.soap/AirportServer/reserveFlightRequest" message="tns:reserveFlight"/>
			<output wsam:Action="http://service.soap/AirportServer/reserveFlightResponse" message="tns:reserveFlightResponse"/>
		</operation>
		<operation name="createUser">
			<input wsam:Action="http://service.soap/AirportServer/createUserRequest" message="tns:createUser"/>
			<output wsam:Action="http://service.soap/AirportServer/createUserResponse" message="tns:createUserResponse"/>
		</operation>
		<operation name="getFlightAvailableSeats">
			<input wsam:Action="http://service.soap/AirportServer/getFlightAvailableSeatsRequest" message="tns:getFlightAvailableSeats"/>
			<output wsam:Action="http://service.soap/AirportServer/getFlightAvailableSeatsResponse" message="tns:getFlightAvailableSeatsResponse"/>
		</operation>
		<operation name="findAvailableAirports">
			<input wsam:Action="http://service.soap/AirportServer/findAvailableAirportsRequest" message="tns:findAvailableAirports"/>
			<output wsam:Action="http://service.soap/AirportServer/findAvailableAirportsResponse" message="tns:findAvailableAirportsResponse"/>
		</operation>
		<operation name="checkFlightReservation">
			<input wsam:Action="http://service.soap/AirportServer/checkFlightReservationRequest" message="tns:checkFlightReservation"/>
			<output wsam:Action="http://service.soap/AirportServer/checkFlightReservationResponse" message="tns:checkFlightReservationResponse"/>
		</operation>
		<operation name="cancelFlightReservation">
			<input wsam:Action="http://service.soap/AirportServer/cancelFlightReservationRequest" message="tns:cancelFlightReservation"/>
			<output wsam:Action="http://service.soap/AirportServer/cancelFlightReservationResponse" message="tns:cancelFlightReservationResponse"/>
		</operation>
		<operation name="getUserReservations">
			<input wsam:Action="http://service.soap/AirportServer/getUserReservationsRequest" message="tns:getUserReservations"/>
			<output wsam:Action="http://service.soap/AirportServer/getUserReservationsResponse" message="tns:getUserReservationsResponse"/>
		</operation>
		<operation name="getAllFlightsWithParameters">
			<input wsam:Action="http://service.soap/AirportServer/getAllFlightsWithParametersRequest" message="tns:getAllFlightsWithParameters"/>
			<output wsam:Action="http://service.soap/AirportServer/getAllFlightsWithParametersResponse" message="tns:getAllFlightsWithParametersResponse"/>
		</operation>
		<operation name="cancelUserReservationInConcreteFlight">
			<input wsam:Action="http://service.soap/AirportServer/cancelUserReservationInConcreteFlightRequest" message="tns:cancelUserReservationInConcreteFlight"/>
			<output wsam:Action="http://service.soap/AirportServer/cancelUserReservationInConcreteFlightResponse" message="tns:cancelUserReservationInConcreteFlightResponse"/>
		</operation>
	</portType>
	<binding name="AirportServerImplPortBinding" type="tns:AirportServer">
		<wsp:PolicyReference URI="#AirportServerImplPortBinding_MTOM_Policy-AirportServerImplPortBinding_MTOM_Policy"/>
		<soap:binding transport="http://schemas.xmlsoap.org/soap/http" style="document"/>
		<operation name="echo">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="getFlightsData">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="getFlightById">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="generatePdf">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
			<fault name="IOException">
				<soap:fault name="IOException" use="literal"/>
			</fault>
		</operation>
		<operation name="reserveFlight">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="createUser">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="getFlightAvailableSeats">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="findAvailableAirports">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="checkFlightReservation">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="cancelFlightReservation">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="getUserReservations">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="getAllFlightsWithParameters">
			<soap:operation soapAction=""/>
			<input>
				<soap:body use="literal"/>
			</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
		<operation name="cancelUserReservationInConcreteFlight">
			<soap:operation soapAction=""/>
			<input>
</input>
			<output>
				<soap:body use="literal"/>
			</output>
		</operation>
	</binding>
	<service name="AirportServerImplService">
		<port name="AirportServerImplPort" binding="tns:AirportServerImplPortBinding">
			<soap:address location="http://localhost:8080/SoapProject/AirportServerImplService"/>
		</port>
	</service>
</definitions>
```
