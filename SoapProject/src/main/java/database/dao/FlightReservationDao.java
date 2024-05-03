package database.dao;

import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

import java.util.List;

public interface FlightReservationDao extends AbstractDao<FlightReservation>{
    FlightReservation getFlightReservation(User user, Flight flight);
    List<FlightReservation> getUserReservations(User user);
}
