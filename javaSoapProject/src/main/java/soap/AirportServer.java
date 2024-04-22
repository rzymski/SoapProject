package soap;

import database.dto.FlightDTO;
import database.model.Flight;

import javax.jws.WebMethod;
import javax.jws.WebService;

//import javax.xml.ws.BindingType;
//import javax.xml.ws.soap.MTOM;
import java.awt.*;
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
    List<Flight> getFlightsData();

    @WebMethod
    List<FlightDTO> getFlightsDTOData();
}
