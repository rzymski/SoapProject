package soap;

import database.dao.FlightDao;
import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;
import database.exceptions.RecordNotFoundException;
import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;
import database.service.FlightReservationService;
import database.service.FlightService;
import database.service.UserService;

import javax.ejb.EJB;
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
    public List<FlightDTO> getFlightsData() {
        logger.warning("Metoda getFlightsData została wywołana");
        List<Flight> flights = flightService.findAll();
        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
        return flightDTOs;
    }

    @Override
    public List<FlightDTO> getFlightsByFromCity(String city) {
        logger.warning("Metoda getFlightsByFromCity została wywołana");
        List<Flight> flights = flightService.findFlightsFromCity(city);
        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
        return flightDTOs;
    }

    @Override
    public List<FlightDTO> getFlightsByToCity(String city) {
        logger.warning("Metoda getFlightsByToCity została wywołana");
        List<Flight> flights = flightService.findFlightsToCity(city);
        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
        return flightDTOs;
    }

    @Inject
    private UserService userService;

    @Inject
    private FlightReservationService flightReservationService;

    @Override
    public FlightReservationDTO checkFlightReservation(Long flightReservationId) {
        FlightReservation flightReservation = flightReservationService.findById(flightReservationId);
        if(flightReservation == null){
            throw new RecordNotFoundException("Nie znaleziono rezerwacji o takim ID: " + flightReservationId);
        }
        FlightReservationDTO flightReservationDTO = new FlightReservationDTO(flightReservation);
        return flightReservationDTO;
    }

    @Override
    public FlightDTO getFlightById(Long flightId) {
        Flight flight = flightService.findById(flightId);
        if(flight == null){
            throw new RecordNotFoundException("Nie znaleziono lotu o takim ID: " + flightId);
        }
        FlightDTO flightDTO = new FlightDTO(flight);
        return flightDTO;
    }

    //pozniej powinno sie dodac przechwytywanie uzytkownika z handlera
    @Override
    public boolean reserveFlight(Long flightId, Long numberOfReservedSeats) {
        User user = userService.findByLogin("rzymski");
        Flight flight = flightService.findById(flightId);
        if(flight == null){
            throw new RecordNotFoundException("Nie znaleziono lotu o takim ID: " + flightId);
        }
        return flightReservationService.addEditFlightReservation(user, flight, numberOfReservedSeats);
    }

    //pozniej powinno sie dodac przechwytywanie uzytkownika z handlera
    @Override
    public void cancelFlightReservation(Long flightId) {
        User user = userService.findByLogin("rzymski");
        Flight flight = flightService.findById(flightId);
        if(flight == null){
            throw new RecordNotFoundException("Nie znaleziono lotu o takim ID: " + flightId);
        }
        FlightReservation flightReservation =  flightReservationService.findFlightReservation(user, flight);
        if(flightReservation == null){
            throw new RecordNotFoundException("Użytkownik " + user.getLogin() + " nie ma rezerwacji lotu o ID: " + flightId);
        }
        flightReservationService.deleteFlightReservation(flightReservation);
    }
}
