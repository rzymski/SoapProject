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
    public List<Flight> findFlightByFromCity(String city) {
        logger.severe("findFlightByCity wywolal sie z city = " + city);
        TypedQuery<Flight> query = em.createNamedQuery( "Flight.findFlightByFromCity", Flight.class);
        query.setParameter(1, city);
        List<Flight> result = query.getResultList();
        return result;
    }
    @Override
    public List<Flight> findFlightByToCity(String city) {
        logger.severe("findFlightByCity wywolal sie z city = " + city);
        TypedQuery<Flight> query = em.createNamedQuery( "Flight.findFlightByToCity", Flight.class);
        query.setParameter(1, city);
        List<Flight> result = query.getResultList();
        return result;
    }
}
