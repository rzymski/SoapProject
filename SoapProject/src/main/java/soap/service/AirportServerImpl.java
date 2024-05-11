package soap.service;

import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;
import database.exceptions.NotEnoughDataException;
import database.exceptions.RecordNotFoundException;
import database.exceptions.UserAlreadyExistException;
import database.exceptions.UserNotFoundException;
import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;
import database.service.FlightReservationService;
import database.service.FlightService;
import database.service.UserService;
import pdfGenerator.PdfGenerator;
import soap.handler.LoginHandler;

import javax.annotation.Resource;
import javax.faces.view.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import java.io.*;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.rmi.NoSuchObjectException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.logging.Logger;

import javax.jws.HandlerChain;
import javax.jws.WebService;
import javax.xml.ws.BindingType;
import javax.xml.ws.WebServiceContext;
import javax.xml.ws.handler.MessageContext;
import javax.xml.ws.soap.MTOM;

import javax.xml.ws.soap.SOAPBinding;

import java.awt.Image;
import javax.imageio.ImageIO;
import java.awt.image.RenderedImage;

@Named
@ViewScoped
@MTOM
@BindingType(value = SOAPBinding.SOAP11HTTP_MTOM_BINDING)
@WebService(endpointInterface = "soap.service.AirportServer")
@HandlerChain(file="loginHandler.xml")
public class AirportServerImpl implements AirportServer, Serializable {
    private static Logger logger = Logger.getLogger(AirportServerImpl.class.getName());
    @Inject
    private FlightService flightService;


    @Override
    public String echo(String text) {
        return "Serwer zwraca otrzymany text: " + text;
    }

//    @Override
//    public byte[] downloadImage() {
//        try {
//            File imageFile = new File("D:\\programowanie\\java\\rsi\\SoapProject\\screens\\plane.png");
//            Image image = ImageIO.read(imageFile);
//            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
//            ImageIO.write((RenderedImage) image, "png", outputStream);
//            return outputStream.toByteArray();
//        } catch (IOException e) {
//            logger.warning("Wystąpił wyjątek: "+ e.toString());
//            return null;
//        }
//    }

    @Override
    public List<FlightDTO> getFlightsData() {
        logger.warning("Metoda getFlightsData została wywołana");
        List<Flight> flights = flightService.findAll();
        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
        return flightDTOs;
    }

//    @Override
//    public List<FlightDTO> getFlightsByFromCity(String city) {
//        logger.warning("Metoda getFlightsByFromCity została wywołana");
//        List<Flight> flights = flightService.findFlightsFromCity(city);
//        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
//        return flightDTOs;
//    }
//
//    @Override
//    public List<FlightDTO> getFlightsByToCity(String city) {
//        logger.warning("Metoda getFlightsByToCity została wywołana");
//        List<Flight> flights = flightService.findFlightsToCity(city);
//        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
//        return flightDTOs;
//    }
//
//    @Override
//    public List<FlightDTO> getFlightsFromCityToCity(String fromCity, String toCity) {
//        logger.warning("Metoda getFlightsFromCityToCity została wywołana");
//        List<Flight> flights = flightService.findFlightsFromCityToCity(fromCity, toCity);
//        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
//        return flightDTOs;
//    }
//
//    @Override
//    public List<FlightDTO> getFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, String startDateRange, String endDateRange) {
//        logger.warning("Metoda getFlightsFromCityToCityWithinDateRange została wywołana z: " + fromCity + " do: " + toCity + " od: " + startDateRange + " do: "+ endDateRange);
//        LocalDateTime start = LocalDateTime.parse(startDateRange);
//        LocalDateTime end = LocalDateTime.parse(endDateRange);
//        logger.warning("Metoda getFlightsFromCityToCityWithinDateRange konwersja stringow na daty start: " + start + " end: " + end);
//        List<Flight> flights = flightService.findFlightsFromCityToCityWithinDateRange(fromCity, toCity, start, end);
//        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
//        return flightDTOs;
//    }

    @Override
    public List<FlightDTO> getAllFlightsWithParameters(String fromCity, String toCity, String startDateRange, String endDateRange) {
        logger.warning("Metoda getAllFlightsWithParameters została wywołana z: " + fromCity + " do: " + toCity + " od: " + startDateRange + " do: "+ endDateRange);
        LocalDateTime start = (startDateRange != null) ? LocalDateTime.parse(startDateRange) : null;
        LocalDateTime end = (endDateRange != null) ? LocalDateTime.parse(endDateRange) : null;
        logger.warning("Metoda getAllFlightsWithParameters konwersja stringow na daty start: " + start + " end: " + end);
        List<Flight> flights = flightService.findAllFlightsWithParameters(fromCity, toCity, start, end);
        List<FlightDTO> flightDTOs = FlightDTO.createFromFlightsFlightDTOs(flights);
        return flightDTOs;
    }

    @Override
    public List<String> findAvailableAirports() {
        logger.warning("Metoda findAvailableAirports");
        List<String> airports = flightService.findAvailableAirports();
        return airports;
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

    @Override
    public boolean reserveFlight(Long flightId, Long numberOfReservedSeats) {
        User user = getAuthenticatedUser();
        if (user == null) throw new UserNotFoundException("Nie ma użytkownika o takich danych logowania");
        Flight flight = flightService.findById(flightId);
        if(flight == null) throw new RecordNotFoundException("Nie znaleziono lotu o takim ID: " + flightId);
        return flightReservationService.addEditFlightReservation(user, flight, numberOfReservedSeats);
    }

    @Override
    public boolean cancelFlightReservation(Long flightReservationId) {
        FlightReservation flightReservation =  flightReservationService.findById(flightReservationId);
        if(flightReservation == null) throw new RecordNotFoundException("Nie ma rezerwacji lotu o ID: " + flightReservationId);
        flightReservationService.deleteFlightReservation(flightReservation);
        return true;
    }

    @Override
    public boolean cancelUserReservationInConcreteFlight(Long flightId) {
        User user = getAuthenticatedUser();
        if (user == null) throw new UserNotFoundException("Nie ma użytkownika o takich danych logowania");
        Flight flight = flightService.findById(flightId);
        if (flight == null) throw new RecordNotFoundException("Nie znaleziono lotu o takim ID: " + flightId);
        FlightReservation flightReservation =  flightReservationService.findFlightReservation(user, flight);
        if(flightReservation == null) throw new RecordNotFoundException("Użytkownik " + user.getLogin() + " nie ma rezerwacji lotu o ID: " + flightId);
        flightReservationService.deleteFlightReservation(flightReservation);
        return true;
    }

    @Resource
    private WebServiceContext webServiceContext;

    private User getAuthenticatedUser() {
        MessageContext context = webServiceContext.getMessageContext();
        String username = (String) context.get(LoginHandler.USER_CONTEXT_KEY);
        if (username != null) {
            return userService.findByLogin(username);
        }
        return null;
    }

    @Override
    public boolean createUser(String username, String password, String email) {
        if (username != null && email != null && password != null) {
            User user = new User(username, password, email, false);
            try {
                userService.save(user);
            } catch (Exception e){
                logger.warning("TRANSAKCJA ABORTED PEWNIE ISTNIEJE TAKI UZYTKOWNIK");
                throw new UserAlreadyExistException("Użytkownik " + username + " juz istnieje.");
            }
        } else {
            throw new NotEnoughDataException("Nie podano wszystkich danych. Użytkownik = " + username + ", password = " + password + ", email = " + email);
        }
        return true;
    }
    
    @Override
    public byte[] generatePdf(Long reservationId) throws IOException {
        FlightReservationDTO res = checkFlightReservation(reservationId);
        if (res == null) {
            throw new RecordNotFoundException("No reservation with ID: " + reservationId);
        }
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        PdfGenerator pdfGenerator = new PdfGenerator(byteArrayOutputStream, res);
        pdfGenerator.setHeaderFooter("Potwierdzenie rezerwacji biletu", "Super linie lotnicze sp. z o.o.");
        String imagePath = "D:\\programowanie\\java\\rsi\\soap\\SoapProject\\screens\\plane.png";
        pdfGenerator.setImage(imagePath);
        pdfGenerator.generate();
        return byteArrayOutputStream.toByteArray();
    }

    @Override
    public List<FlightReservationDTO> getUserReservations(String username) {
        logger.warning("Metoda getUserReservations została wywołana");
        User user = getAuthenticatedUser();
        if (user == null) throw new UserNotFoundException("Nie ma użytkownika o takich danych logowania");
        List<FlightReservation> flightReservations = flightReservationService.findUserReservations(user);
        return FlightReservationDTO.createFromFlightReservationsFlightReservationDTOs(flightReservations);
    }

    @Override
    public Long getFlightAvailableSeats(Long flightId) {
        User user = getAuthenticatedUser();
        Flight flight = flightService.findById(flightId);
        return flightReservationService.getFlightAvailableSeats(flight, user);
    }
}
