package database.dao;

import database.model.Flight;
import database.model.FlightReservation;
import database.model.User;

import java.util.Optional;

public interface UserDao extends AbstractDao<User> {
    @Override
    void delete(Long id);
    public Optional<User> findByLogin(String username);
}
