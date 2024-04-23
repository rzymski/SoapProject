package database.dto;

import database.model.Flight;
import database.model.FlightReservation;
import java.time.LocalDateTime;

public class FlightReservationDTO extends FlightDTO {

    private String login;
    private String email;

    private Long numberOfReservedSeats;

    public FlightReservationDTO() { super(); }

    public FlightReservationDTO(FlightReservation flightReservation) {
        super(flightReservation.getFlight());
        this.login = flightReservation.getUser().getLogin();
        this.email = flightReservation.getUser().getEmail();
        this.numberOfReservedSeats = flightReservation.getNumberOfReservedSeats();
    }

    public FlightReservationDTO(Flight flight, String login, String email, Long numberOfReservedSeats) {
        super(flight);
        this.login = login;
        this.email = email;
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    public FlightReservationDTO(Long id, String flightCode, String departureAirport, LocalDateTime departureTime, String destinationAirport, LocalDateTime arrivalTime, Long capacity, String login, String email, Long numberOfReservedSeats) {
        super(id, flightCode, departureAirport, departureTime, destinationAirport, arrivalTime, capacity);
        this.login = login;
        this.email = email;
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Long getNumberOfReservedSeats() {
        return numberOfReservedSeats;
    }

    public void setNumberOfReservedSeats(Long numberOfReservedSeats) {
        this.numberOfReservedSeats = numberOfReservedSeats;
    }

    @Override
    public String toString() {
        String FlightData = "id=" + id +
                ", flightCode='" + flightCode + '\'' +
                ", departureAirport='" + departureAirport + '\'' +
                ", departureTimeX=" + departureTimeX +
                ", destinationAirport='" + destinationAirport + '\'' +
                ", arrivalTimeX=" + arrivalTimeX +
                ", capacity=" + capacity +
                '}';
        String UserData = "id=" + getId() +
                ", login='" + login + '\'' +
                ", email='" + email + '\'' +
                ", numberOfReservedSeats=" + numberOfReservedSeats +
                '}';
        StringBuilder sb = new StringBuilder();
        sb.append("FlightReservationDTO{")
                .append(UserData);
        return sb.toString();
    }
}
