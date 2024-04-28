package database.service;

import database.model.Flight;

import java.time.LocalDateTime;
import java.util.List;

public interface FlightService {
    Flight save(Flight t);
    void delete (Long id);
    Flight findById(Long id);
    List<Flight> findAll();
    List<Flight> findFlightsFromCity(String city);
    List<Flight> findFlightsToCity(String city);
    List<Flight> findFlightsFromCityToCity(String fromCity, String toCity);
    List<Flight> findFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange);
    List<Flight> findAllFlightsWithParameters(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange);
    List<String> findAvailableAirports();
}
