package soap;

import database.model.Flight;
import database.service.FlightService;

import javax.faces.view.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

import javax.jws.WebService;
import javax.xml.ws.BindingType;
import javax.xml.ws.soap.MTOM;

import javax.xml.ws.soap.SOAPBinding;

import java.awt.Image;
import javax.imageio.ImageIO;
import java.awt.image.RenderedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;

@Named
@ViewScoped
@MTOM
@BindingType(value = SOAPBinding.SOAP11HTTP_MTOM_BINDING)
@WebService(endpointInterface = "soap.AirportServer")
public class AirportServerImpl implements AirportServer, Serializable {
    private static Logger logger = Logger.getLogger(AirportServerImpl.class.getName());
    @Inject
    private FlightService flightService;

    @Override
    public String echo(String text) {
        return "Serwer zwraca otrzymany text: " + text;
    }

    @Override
    public byte[] downloadImage() {
        try {
            File imageFile = new File("D:\\programowanie\\java\\rsi\\SoapProject\\screens\\plane.png");
            Image image = ImageIO.read(imageFile);
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            ImageIO.write((RenderedImage) image, "png", outputStream);
            return outputStream.toByteArray();
        } catch (IOException e) {
            logger.warning("Wystąpił wyjątek: "+ e.toString());
            return null;
        }
    }

    @Override
    public List<Flight> getFlightsData() {
        logger.warning("Metoda getFlightsData została wywołana");
        List<Flight> flights = flightService.findAll();
        logger.warning("Znalezione loty:");
        for (Flight flight : flights) {
            logger.warning(flight.toString());
        }
        logger.warning("Testowa wartosc: " + flights.get(1));
        return flights;
    }
}
