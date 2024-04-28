package database.service;


import database.dao.FlightDao;
import database.model.Flight;

import javax.ejb.EJB;
import javax.ejb.Stateless;
import java.time.LocalDateTime;
import java.util.List;


@Stateless
public class FlightServiceImpl implements FlightService {
    @EJB
    private FlightDao flightDao;
    @Override
    public Flight save(Flight t) {
        return flightDao.save(t);
    }

    @Override
    public void delete(Long id) {
        flightDao.delete(id);
    }

    @Override
    public Flight findById(Long id) {
        return flightDao.findById(id).orElse(null);
    }
    @Override
    public List<Flight> findAll() {
        return flightDao.findAll();
    }

    @Override
    public List<Flight> findFlightsFromCity(String city) {
        return flightDao.getFlightsFromCity(city);
    }
    @Override
    public List<Flight> findFlightsToCity(String city) {
        return flightDao.getFlightsToCity(city);
    }
    @Override
    public List<Flight> findFlightsFromCityToCity(String fromCity, String toCity) { return flightDao.getFlightsFromCityToCity(fromCity, toCity); }

    @Override
    public List<Flight> findFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange) {
        return flightDao.getFlightsFromCityToCityWithinDateRange(fromCity, toCity, startDateRange, endDateRange);
    }

    @Override
    public List<Flight> findAllFlightsWithParameters(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange) {
        return flightDao.getAllFlightsWithParameters(fromCity, toCity, startDateRange, endDateRange);
    }
}
