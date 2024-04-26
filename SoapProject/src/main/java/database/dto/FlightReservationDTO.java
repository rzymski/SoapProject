package database.dto;

import database.model.Flight;
import database.model.FlightReservation;

import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import java.time.LocalDateTime;

public class FlightReservationDTO extends FlightDTO {
    private Long reservationId;

    private String login;
    private String email;

    private Long numberOfReservedSeats;

    public FlightReservationDTO() { super(); }

    public FlightReservationDTO(FlightReservation flightReservation) {
        super(flightReservation.getFlight());
        this.reservationId = flightReservation.getId();
        this.login = flightReservation.getUser().getLogin();
        this.email = flightReservation.getUser().getEmail();
        this.numberOfReservedSeats = flightReservation.getNumberOfReservedSeats();
    }

//    public FlightReservationDTO(Flight flight, String login, String email, Long numberOfReservedSeats) {
//        super(flight);
//        this.login = login;
//        this.email = email;
//        this.numberOfReservedSeats = numberOfReservedSeats;
//    }
//
//    public FlightReservationDTO(Long id, String flightCode, String departureAirport, LocalDateTime departureTime, String destinationAirport, LocalDateTime arrivalTime, Long capacity, String login, String email, Long numberOfReservedSeats) {
//        super(id, flightCode, departureAirport, departureTime, destinationAirport, arrivalTime, capacity);
//        this.login = login;
//        this.email = email;
//        this.numberOfReservedSeats = numberOfReservedSeats;
//    }

    @XmlAttribute
    public Long getReservationId() {
        return reservationId;
    }

    @XmlElement(name = "login")
    public String getLogin() {
        return login;
    }

    @XmlElement(name = "email")
    public String getEmail() {
        return email;
    }

    @XmlElement(name = "numberOfReservedSeats")
    public Long getNumberOfReservedSeats() {
        return numberOfReservedSeats;
    }

    public void setReservationId(Long reservationId) {
        this.reservationId = reservationId;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setNumberOfReservedSeats(Long numberOfReservedSeats) {
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    @Override
    public String toString() {
        String FlightData = "id=" + id +
                ", flightCode='" + flightCode + '\'' +
                ", departureAirport='" + departureAirport + '\'' +
                ", departureTime=" + departureTime +
                ", destinationAirport='" + destinationAirport + '\'' +
                ", arrivalTime=" + arrivalTime +
                ", capacity=" + capacity;
        String UserData = "id=" + getId() +
                ", login='" + login + '\'' +
                ", email='" + email + '\'' +
                ", numberOfReservedSeats=" + numberOfReservedSeats;
        StringBuilder sb = new StringBuilder();
        sb.append("FlightReservationDTO{")
                .append(UserData)
                .append("reservationId = " + reservationId + "}");
        return sb.toString();
    }
}
