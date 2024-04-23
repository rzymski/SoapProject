package database.service;

import database.dao.FlightDao;
import database.dao.FlightReservationDao;
import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

import javax.ejb.EJB;
import javax.ejb.Stateless;
import javax.inject.Inject;
import java.util.List;
import java.util.logging.Logger;

@Stateless
public class FlightReservationServiceImpl implements FlightReservationService {
    private static Logger logger = Logger.getLogger(FlightReservationServiceImpl.class.getName());
    @EJB
    private FlightDao flightDao;
    @EJB
    FlightReservationDao flightReservationDao;

    @Override
    public FlightReservation save(FlightReservation t) { return flightReservationDao.save(t); }

    @Override
    public void delete(Long id) { flightReservationDao.delete(id); }

    @Override
    public FlightReservation findById(Long id) { return flightReservationDao.findById(id).orElse(null); }
    @Override
    public List<FlightReservation> findAll() {
        return flightReservationDao.findAll();
    }

    @Override
    public FlightReservation findFlightReservation(User user, Flight flight) {
        return flightReservationDao.findFlightReservation(user, flight);
    }

    @Inject
    UserService userService;

    @Override
    public boolean addEditFlightReservation(User user, Flight flight, Long numberOfReservedSeats) {
        logger.severe("Wywolal sie serwis addEditFlightReservation");
        logger.severe("User = " + user + " Flight = " + flight);
        FlightReservation fr = flightReservationDao.findFlightReservation(user, flight);

        Long actuallyReservedSeats = 0L;
        if(fr != null){
            FlightReservation flightReservation = flightReservationDao.findFlightReservation(user, flight);
            actuallyReservedSeats = flightReservation.getNumberOfReservedSeats();
        }

        if(flight.getCapacity() - actuallyReservedSeats >= flightDao.getFlightTotalNumberOfOccupiedSeats(flight, numberOfReservedSeats)){
            if(fr != null){
                deleteFlightReservation(user, flight);
            }

            user.addFlightReservation(flight, numberOfReservedSeats);
            userService.save(user);
            logger.severe("AddEditFlightReservation zakonczony, udalo sie dodac/zmienic rezerwacje");
            return true;
        } else {
            logger.severe("AddEditFlightReservation zakonczony, nie udalo sie dodac/zmienic rezerwacji");
            return false;
        }
    }

    @Override
    public void deleteFlightReservation(User user, Flight flight) {
        logger.severe("Usuwanie rezerwacji uzytkownika " + user + " na lot " + flight);
        user.removeFlightReservation(flight);
        userService.save(user);
    }

    @Override
    public void clearUserFlightReservations(User user) {
        user.clearUserFlightReservations();
        userService.save(user);
    }
}
