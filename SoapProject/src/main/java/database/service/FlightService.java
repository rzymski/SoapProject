package database.service;

import database.model.Flight;

import java.util.List;

public interface FlightService {
    Flight save(Flight t);
    void delete (Long id);
    Flight findById(Long id);
    List<Flight> findAll();
}
