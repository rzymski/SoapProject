package database.dao;

import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

import javax.ejb.Stateless;
import javax.persistence.TypedQuery;
import java.util.List;
import java.util.logging.Logger;

@Stateless
public class FlightReservationDaoImpl extends AbstractDaoJpaImpl<FlightReservation> implements FlightReservationDao{
    private static Logger logger = Logger.getLogger(FlightReservationDaoImpl.class.getName());
    @Override
    public FlightReservation getFlightReservation(User user, Flight flight) {
        logger.severe("findFlightReservation wywolal sie: user= " + user + " lot = " + flight);
        TypedQuery<FlightReservation> query = em.createNamedQuery( "FlightReservation.findFlightReservation", FlightReservation.class);
        query.setParameter(1, user);
        query.setParameter(2, flight);
        List<FlightReservation> result = query.getResultList();
        return result.isEmpty() ? null : result.get(0);
    }

    @Override
    public List<FlightReservation> getUserReservations(User user) {
        logger.severe("findFlightReservation wywolal sie: user= " + user);
        TypedQuery<FlightReservation> query = em.createNamedQuery( "FlightReservation.findUserReservations", FlightReservation.class);
        query.setParameter(1, user);
        List<FlightReservation> result = query.getResultList();
        return result;
    }
}
