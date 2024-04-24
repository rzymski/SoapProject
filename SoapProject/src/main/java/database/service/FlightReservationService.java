package database.service;

import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

import java.util.List;

public interface FlightReservationService {
    FlightReservation save(FlightReservation t);
    void delete (Long id);
    FlightReservation findById(Long id);
    List<FlightReservation> findAll();

    FlightReservation findFlightReservation(User user, Flight flight);
    boolean addEditFlightReservation(User user, Flight flight, Long numberOfReservedSeats);
    boolean addEditFlightReservation(FlightReservation flightReservation, Long numberOfReservedSeats);
    void deleteFlightReservation(User user, Flight flight);
    void deleteFlightReservation(FlightReservation flightReservation);
    void clearUserFlightReservations(User user);
}
