package database.model;

import javax.persistence.*;
import javax.validation.constraints.Min;
import java.math.BigDecimal;
import java.util.Objects;

@NamedQuery(name="FlightReservation.findUserReservations",query = "select fr from FlightReservation fr where fr.user=?1")
@NamedQuery(name = "FlightReservation.findFlightReservation", query = "select fr from FlightReservation fr where fr.user=?1 and fr.flight=?2")
@Entity
public class FlightReservation extends AbstractModel {

    @ManyToOne
    private Flight flight;

    @ManyToOne
    private User user;

    @Min(1)
    private Long numberOfReservedSeats;

    public FlightReservation() {}

    public FlightReservation(Flight flight, User user, Long numberOfReservedSeats) {
        this.flight = flight;
        this.user = user;
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    public Flight getFlight() {
        return flight;
    }

    public void setFlight(Flight flight) {
        this.flight = flight;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Long getNumberOfReservedSeats() {
        return numberOfReservedSeats;
    }

    public void setNumberOfReservedSeats(Long numberOfReservedSeats) {
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    @Override
    public String toString() {
        return "FlightReservation{" +
                "flight=" + flight +
                ", user=" + user +
                ", numberOfReservedSeats=" + numberOfReservedSeats +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof FlightReservation)) return false;
        if (!super.equals(o)) return false;
        FlightReservation that = (FlightReservation) o;
        return Objects.equals(flight, that.flight) && Objects.equals(user, that.user);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), flight, user);
    }
}
