package database.dao;

import database.model.Flight;

import java.time.LocalDateTime;
import java.util.List;

public interface FlightDao extends AbstractDao<Flight>{
    public List<Flight> getFlightsFromCity(String city);
    public List<Flight> getFlightsToCity(String city);
    public List<Flight> getFlightsFromCityToCity(String fromCity, String toCity);
    public List<Flight> getFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange);
    public Long getFlightTotalNumberOfOccupiedSeats(Flight flight);
    public List<Flight> getAllFlightsWithParameters(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange);
    public List<String> getAvailableAirports();
}
