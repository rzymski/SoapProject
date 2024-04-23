package database.dao;

import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

public interface FlightReservationDao extends AbstractDao<FlightReservation>{
    FlightReservation findFlightReservation(User user, Flight flight);
}
