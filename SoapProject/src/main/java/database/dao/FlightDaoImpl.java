package database.dao;

import database.model.Flight;

import javax.ejb.Stateless;
import javax.persistence.TypedQuery;
import java.util.List;
import java.util.logging.Logger;

@Stateless
public class FlightDaoImpl extends AbstractDaoJpaImpl<Flight> implements FlightDao{
    private static Logger logger = Logger.getLogger(FlightDaoImpl.class.getName());

    @Override
    public List<Flight> getFlightsFromCity(String city) {
        logger.severe("getFlightsFromCity wywolal sie z city = " + city);
        TypedQuery<Flight> query = em.createNamedQuery( "Flight.findFlightsFromCity", Flight.class);
        query.setParameter(1, city);
        List<Flight> result = query.getResultList();
        return result;
    }
    @Override
    public List<Flight> getFlightsToCity(String city) {
        logger.severe("getFlightsToCity wywolal sie z city = " + city);
        TypedQuery<Flight> query = em.createNamedQuery( "Flight.findFlightsToCity", Flight.class);
        query.setParameter(1, city);
        List<Flight> result = query.getResultList();
        return result;
    }

    @Override
    public Long getFlightTotalNumberOfOccupiedSeats(Flight flight, Long additionalNumberOfOccupiedSeats) {
        logger.severe("findFlightTotalNumberOfOccupiedSeats wywolal sie z liczba dodatkowych miejsc = " + additionalNumberOfOccupiedSeats);
        TypedQuery<Long> query = em.createNamedQuery("Flight.getFlightTotalNumberOfOccupiedSeats", Long.class);
        query.setParameter(1, flight);
        List<Long> result = query.getResultList();
        Long resultValue = result.get(0) == null ? 0L : result.get(0);
        logger.severe("findFlightTotalNumberOfOccupiedSeats " + (resultValue + additionalNumberOfOccupiedSeats));
        return resultValue + additionalNumberOfOccupiedSeats;
    }
}
