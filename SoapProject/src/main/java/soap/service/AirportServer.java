package soap.service;

import database.adapter.LocalDateTimeAdapter;
import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;
import database.model.Flight;
import database.model.FlightReservation;

import javax.jws.WebMethod;
import javax.jws.WebService;

//import javax.xml.ws.BindingType;
//import javax.xml.ws.soap.MTOM;
import java.awt.*;
import java.time.LocalDateTime;
import java.util.List;

import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import javax.jws.soap.SOAPBinding.Use;

//@MTOM
@WebService
@SOAPBinding(style = Style.DOCUMENT, use = Use.LITERAL)
//@BindingType(value = SOAPBinding.SOAP11HTTP_MTOM_BINDING)
public interface AirportServer {
    @WebMethod
    String echo(String text);

    @WebMethod
    byte[] downloadImage();


    @WebMethod
    List<FlightDTO> getFlightsData();

    @WebMethod
    List<FlightDTO> getFlightsByFromCity(String city);

    @WebMethod
    List<FlightDTO> getFlightsByToCity(String city);

    @WebMethod
    List<FlightDTO> getFlightsFromCityToCity(String fromCity, String toCity);

    @WebMethod
    List<FlightDTO> getFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, String startDateRange, String endDateRange);

    @WebMethod
    List<FlightDTO> getAllFlightsWithParameters(String fromCity, String toCity, String startDateRange, String endDateRange);

    @WebMethod
    FlightReservationDTO checkFlightReservation(Long flightReservationId);

    @WebMethod
    FlightDTO getFlightById(Long flightReservationId);

    @WebMethod
    boolean reserveFlight(Long flightId, Long numberOfReservedSeats);

    @WebMethod
    void cancelFlightReservation(Long flightId);

    @WebMethod
    void createUser(String username, String password,String email);
}
