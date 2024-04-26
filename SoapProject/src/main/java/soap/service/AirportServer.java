package soap.service;

import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;
import database.model.Flight;
import database.model.FlightReservation;

import javax.jws.WebMethod;
import javax.jws.WebService;

//import javax.xml.ws.BindingType;
//import javax.xml.ws.soap.MTOM;
import java.awt.*;
import java.math.BigDecimal;
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
    FlightReservationDTO checkFlightReservation(Long flightReservationId);

    @WebMethod
    FlightDTO getFlightById(Long flightReservationId);

    @WebMethod
    boolean reserveFlight(Long flightId, Long numberOfReservedSeats);

    @WebMethod
    void cancelFlightReservation(Long flightId);
}
