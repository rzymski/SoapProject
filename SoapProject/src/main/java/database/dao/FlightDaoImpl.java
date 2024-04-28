package database.dao;

import database.model.Flight;

import javax.ejb.Stateless;
import javax.persistence.TypedQuery;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import java.time.LocalDateTime;
import java.util.ArrayList;
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
    public List<Flight> getFlightsFromCityToCity(String fromCity, String toCity) {
        logger.severe("getFlightsFromCityToCity wywolal sie z fromCity = " + fromCity + " toCity = " + toCity);
        TypedQuery<Flight> query = em.createNamedQuery( "Flight.findFlightsFromCityToCity", Flight.class);
        query.setParameter(1, fromCity);
        query.setParameter(2, toCity);
        List<Flight> result = query.getResultList();
        return result;
    }

    @Override
    public List<Flight> getFlightsFromCityToCityWithinDateRange(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange) {
        logger.severe("getFlightsFromCityToCityWithinDateRange wywolal sie z fromCity = " + fromCity + " toCity = " + toCity + " dateRange = " + startDateRange + " : " + endDateRange);
        TypedQuery<Flight> query = em.createNamedQuery("Flight.findFlightsFromCityToCityWithinDateRange", Flight.class);
        query.setParameter(1, fromCity);
        query.setParameter(2, toCity);
        query.setParameter(3, startDateRange);
        query.setParameter(4, endDateRange);
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

    @Override
    public List<Flight> getAllFlightsWithParameters(String fromCity, String toCity, LocalDateTime startDateRange, LocalDateTime endDateRange) {
        logger.severe("getAllFlightsWithParameters wywolal sie z fromCity = " + fromCity + " toCity = " + toCity + " dateRange = " + startDateRange + " : " + endDateRange);
        CriteriaBuilder cb = em.getCriteriaBuilder();
        CriteriaQuery<Flight> cq = cb.createQuery(Flight.class);
        Root<Flight> flight = cq.from(Flight.class);

        List<Predicate> conditions = new ArrayList<>();
        if (fromCity != null) { conditions.add(cb.equal(cb.upper(flight.get("departureAirport")), fromCity.toUpperCase())); }
        if (toCity != null) { conditions.add(cb.equal(cb.upper(flight.get("destinationAirport")), toCity.toUpperCase())); }
        if (startDateRange != null && endDateRange != null) {
            conditions.add(cb.between(flight.get("departureTime"), startDateRange, endDateRange));
        } else if (startDateRange != null) {
            conditions.add(cb.greaterThanOrEqualTo(flight.get("departureTime"), startDateRange));
        } else if (endDateRange != null) {
            conditions.add(cb.lessThanOrEqualTo(flight.get("departureTime"), endDateRange));
        }

        cq.where(conditions.toArray(new Predicate[0]));
        TypedQuery<Flight> allQuery = em.createQuery(cq);
        return allQuery.getResultList();
    }

    @Override
    public List<String> getAvailableAirports() {
        logger.severe("getAvailableAirports");
        TypedQuery<String> query = em.createNamedQuery("Flight.getAvailableAirports", String.class);
        List<String> result = query.getResultList();
        return result;
    }
}
