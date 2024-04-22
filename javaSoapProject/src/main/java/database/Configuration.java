package database;

import database.dao.*;
import database.model.*;

import javax.annotation.PostConstruct;
import javax.annotation.sql.DataSourceDefinition;
import javax.ejb.EJB;
import javax.ejb.Singleton;
import javax.ejb.Startup;
import javax.faces.annotation.FacesConfig;
import javax.inject.Inject;
import javax.security.enterprise.authentication.mechanism.http.CustomFormAuthenticationMechanismDefinition;
import javax.security.enterprise.authentication.mechanism.http.LoginToContinue;
import javax.security.enterprise.identitystore.DatabaseIdentityStoreDefinition;
import javax.security.enterprise.identitystore.Pbkdf2PasswordHash;
import java.util.List;
import java.util.logging.Logger;

@DataSourceDefinition(
        name = "java:global/SoapProjectDataSource",
        className = "org.h2.jdbcx.JdbcDataSource",
        url = "jdbc:h2:file:D:/programowanie/java/rsi/SoapProject/javaSoapProject/airport",

        minPoolSize = 1,
        initialPoolSize = 1,
        user = "sa",
        password = ""
)
@CustomFormAuthenticationMechanismDefinition(
        loginToContinue = @LoginToContinue(
                loginPage = "/login.xhtml",
                errorPage = "",
                useForwardToLogin = false
        )
)
@DatabaseIdentityStoreDefinition(
        dataSourceLookup = "java:global/SoapProjectDataSource",
        callerQuery = "SELECT password FROM \"USER\" WHERE login = ?",
        groupsQuery = "SELECT ug.name FROM \"USER\" u JOIN USERGROUP ug ON u.usergroup_id=ug.id WHERE u.login = ?",
        hashAlgorithm = Pbkdf2PasswordHash.class,
        hashAlgorithmParameters = {
                "Pbkdf2PasswordHash.Algorithm=PBKDF2WithHmacSHA512",
                "Pbkdf2PasswordHash.Iterations=3072",
                "Pbkdf2PasswordHash.SaltSizeBytes=64",
        }
)
@FacesConfig
@Singleton
@Startup
public class Configuration {
    private static Logger logger = Logger.getLogger(Configuration.class.getName());
    @Inject
    private Pbkdf2PasswordHash pbkdf;

    @EJB
    private UserDao userDao;

    @EJB
    private UserGroupDao userGroupDao;
    @EJB
    private FlightDao flightDao;

    @PostConstruct
    private void init(){
        initDatabase();
    }

    private void initDatabase(){
        logger.severe("Wywolano inicjalizacje bazy danych");

        logger.severe("Znalezione loty: ");
        List<Flight> flights = flightDao.findAll();
        for (Flight flight: flights) {
            logger.severe(flight.toString());
        }

        List<UserGroup> userGroupList = userGroupDao.findAll();
        logger.severe("Znaleziono " + userGroupList.size()+ " grup: ");
        for (UserGroup ug: userGroupList) {
            logger.severe(ug.toString());
        }
        if(userGroupList.size() == 0)
        {
            logger.severe("Baza danych jest pusta / nie ma jej");
            UserGroup ugAdmin = new UserGroup("ROLE_ADMIN");
            UserGroup ugClient = new UserGroup("ROLE_CLIENT");
            userGroupDao.save(ugAdmin);
            userGroupDao.save(ugClient);
            logger.severe("Utworzono grupy");
        }
    }
}
