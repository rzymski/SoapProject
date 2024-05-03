package database.model;

import database.service.FlightReservationServiceImpl;

import javax.persistence.*;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.logging.Logger;

@NamedQuery(name="User.findByLogin",query = "select u from User u where u.login=:login")
@Entity
public class User extends AbstractModel {
    @Column(unique = true)
    private String login;
    private String password;
    private String email;
    private boolean isVip=false;
    @ManyToOne
    private UserGroup userGroup;

    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<FlightReservation> flightReservations = new ArrayList<>();

    public User() {
    }

    public User(String login, String password, String email, Boolean isVip) {
        this.login = login;
        this.password = password;
        this.email = email;
        this.isVip = isVip;
    }
    public User(String login, String password, String email, Boolean isVip, UserGroup userGroup) {
        this.login = login;
        this.password = password;
        this.email = email;
        this.isVip = isVip;
        userGroup.addUser(this);
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public UserGroup getUserGroup() {
        return userGroup;
    }

    public void setUserGroup(UserGroup userGroup) {
        this.userGroup = userGroup;
    }

    public boolean getIsVip() {
        return isVip;
    }

    public void setIsVip(boolean vip) {
        isVip = vip;
    }

    public List<FlightReservation> getFlightReservations() {
        return flightReservations;
    }

    public void setFlightReservations(List<FlightReservation> flightReservations) {
        this.flightReservations = flightReservations;
    }

    @Override
    public String toString() {
        String basicData = "User{" +
                "id=" + getId() +
                ", login='" + login + '\'' +
                ", email='" + email + '\'' +
                ", userGroup='" + userGroup.getName() + '\'' +
                '}';
        StringBuilder sb = new StringBuilder();
        sb.append(basicData);
//                .append(" lista rezerwacji: ");
//
//        for (FlightReservation flightReservation : flightReservations) {
//            sb.append(flightReservation.getFlight())
//                    .append(", ");
//        }
        return sb.toString();
    }

    public void addFlightReservation(Flight flight, Long numberOfReservedSeats) {
        FlightReservation flightReservation = new FlightReservation(flight, this, numberOfReservedSeats);
        flightReservations.add(flightReservation);
        flight.getFlightReservations().add(flightReservation);
    }

    public void removeFlightReservation(Flight flight) {
        for (Iterator<FlightReservation> iterator = flightReservations.iterator(); iterator.hasNext();) {
            FlightReservation flightReservation = iterator.next();
            if (flightReservation.getUser().equals(this) && flightReservation.getFlight().equals(flight)) {
                iterator.remove();
                flightReservation.getFlight().getFlightReservations().remove(flightReservation);
                flightReservation.setUser(null);
                flightReservation.setFlight(null);
            }
        }
    }

    public void clearUserFlightReservations(){
        for (Iterator<FlightReservation> iterator = flightReservations.iterator(); iterator.hasNext();) {
            FlightReservation flightReservation = iterator.next();
            iterator.remove();
            flightReservation.getFlight().getFlightReservations().remove(flightReservation);
            flightReservation.setUser(null);
            flightReservation.setFlight(null);
        }
    }

    private static Logger logger = Logger.getLogger(User.class.getName());
}
