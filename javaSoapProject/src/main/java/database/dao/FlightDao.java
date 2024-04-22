package database.dao;

import database.model.Flight;

import java.util.List;

public interface FlightDao extends AbstractDao<Flight>{
    public List<Flight> findFlightByFromCity(String city);
    public List<Flight> findFlightByToCity(String city);
}
