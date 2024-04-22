package database.dao;

import database.model.User;

import javax.ejb.Stateless;
import java.util.Optional;
import java.util.logging.Logger;

@Stateless
public class UserDaoImpl extends AbstractDaoJpaImpl<User> implements UserDao {
    private static Logger logger = Logger.getLogger(UserDaoImpl.class.getName());
    @Override
    public void delete(Long id) {
        logger.severe("Nadpisana metoda delete w userDaoImpl");
        User u = em.getReference(User.class,id);
        logger.severe(u.toString());
        em.remove(u);
        logger.severe("Wykonalo sie prawidlowo");
    }
    @Override
    public Optional<User> findByLogin(String login) {
        return findSingle("User.findByLogin","login",login);
    }
}
