package database.dao;

import database.model.Flight;

import java.util.List;

public interface FlightDao extends AbstractDao<Flight>{
    public List<Flight> getFlightsFromCity(String city);
    public List<Flight> getFlightsToCity(String city);

    public Long getFlightTotalNumberOfOccupiedSeats(Flight flight, Long additionalNumberOfOccupiedSeats);
}
