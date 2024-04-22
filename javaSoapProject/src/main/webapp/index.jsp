<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>Java Soap Project Server</title>
</head>
    <body>
        <h1>
            <%= "Można sprawdzić działanie serwera w: " %>
        </h1>
        <ul style="font-size: 20px">
            <li>
                <a href="http://localhost:8080/SoapProject/AirportServerImplService">Lista metod</a>
            </li>
            <li>
                <a href="http://localhost:8080/SoapProject/AirportServerImplService?WSDL">WSDL</a>
            </li>
            <li>
                <a href="http://localhost:8080/SoapProject/AirportServerImplService?Tester">Tester Glassfisha</a>
            </li>
            <br>
            <li>
                <a href="http://localhost:4848">Panel administracyjny glassfish-a</a>
            </li>
        </ul>
    </body>
</html>