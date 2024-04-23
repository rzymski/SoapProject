package database.service;


import database.dao.FlightDao;
import database.model.Flight;

import javax.ejb.EJB;
import javax.ejb.Stateless;
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
}
