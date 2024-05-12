package soap.service;

import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;

import javax.jws.WebMethod;
import javax.jws.WebService;

//import javax.xml.ws.BindingType;
//import javax.xml.ws.soap.MTOM;
import java.io.IOException;
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
    List<FlightDTO> getFlightsData();

    @WebMethod
    List<FlightDTO> getAllFlightsWithParameters(String fromCity, String toCity, String startDateRange, String endDateRange);

    @WebMethod
    List<String> findAvailableAirports();

    @WebMethod
    FlightReservationDTO checkFlightReservation(Long flightReservationId);

    @WebMethod
    FlightDTO getFlightById(Long flightReservationId);

    @WebMethod
    boolean reserveFlight(Long flightId, Long numberOfReservedSeats);

    @WebMethod
    boolean cancelFlightReservation(Long flightReservationId);

    @WebMethod
    boolean cancelUserReservationInConcreteFlight(Long flightId);

    @WebMethod
    boolean createUser(String username, String password,String email);

    @WebMethod
    byte[] generatePdf(Long reservationId) throws IOException;

    @WebMethod
    List<FlightReservationDTO> getUserReservations(String username);

    @WebMethod
    Long getFlightAvailableSeats(Long flightId);
}
