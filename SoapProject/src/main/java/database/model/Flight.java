package database.model;

import database.adapter.LocalDateTimeAdapter;

import javax.persistence.*;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@NamedQuery(name = "Flight.findFlightsFromCity", query ="select f from Flight f where f.departureAirport=upper(?1)")
@NamedQuery(name = "Flight.findFlightsToCity", query ="select f from Flight f where f.destinationAirport=upper(?1)")
@NamedQuery(name = "Flight.findFlightsFromCityToCity", query = "select f from Flight f where f.departureAirport=upper(?1) and  f.destinationAirport=upper(?2)")
@NamedQuery(name = "Flight.findFlightsFromCityToCityWithinDateRange", query = "select f from Flight f where f.departureAirport = upper(?1) and f.destinationAirport = upper(?2) and f.departureTime between ?3 and ?4")
@NamedQuery(name = "Flight.getFlightTotalNumberOfOccupiedSeats", query = "select sum(fr.numberOfReservedSeats) from FlightReservation fr where fr.flight=?1")
public class Flight extends AbstractModel {
    @Column(unique = true)
    private String flightCode;
    private String departureAirport;
    @Column(nullable = false)
    private LocalDateTime departureTime;
    private String destinationAirport;
    @Column(nullable = false)
    private LocalDateTime arrivalTime;
    private Long capacity;

    @OneToMany(mappedBy = "flight", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<FlightReservation> flightReservations = new ArrayList<>();

    public Flight(){}
    public Flight(String flightCode, String departureAirport, LocalDateTime departureTime,
                  String destinationAirport, LocalDateTime arrivalTime) {
        this(flightCode, departureAirport, departureTime, destinationAirport, arrivalTime, 100L);
    }
    public Flight(String flightCode, String departureAirport, LocalDateTime departureTime,
                  String destinationAirport, LocalDateTime arrivalTime, Long capacity)
    {
        this.flightCode = flightCode;
        this.departureAirport = departureAirport;
        this.departureTime = departureTime;
        this.destinationAirport = destinationAirport;
        this.arrivalTime = arrivalTime;
        this.capacity = capacity;
    }

    public Long getCapacity() { return capacity; }

    public void setCapacity(Long capacity) { this.capacity = capacity; }

    public String getFlightCode() {
        return flightCode;
    }

    public void setFlightCode(String flightCodee) {
        this.flightCode = flightCode;
    }

    public String getDepartureAirport() {
        return departureAirport;
    }

    public void setDepartureAirport(String departureAirport) {
        this.departureAirport = departureAirport;
    }

    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    @XmlSchemaType(name="dateTime")
    public LocalDateTime getDepartureTime() {
        return departureTime;
    }

    public void setDepartureTime(LocalDateTime departureTime) {
        this.departureTime = departureTime;
    }

    public String getDestinationAirport() {
        return destinationAirport;
    }

    public void setDestinationAirport(String destinationAirport) {
        this.destinationAirport = destinationAirport;
    }

    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    @XmlSchemaType(name="dateTime")
    public LocalDateTime getArrivalTime() {
        return arrivalTime;
    }

    public void setArrivalTime(LocalDateTime arrivalTime) {
        this.arrivalTime = arrivalTime;
    }

    @Override
    public String toString() {
        return "Flight{" +
                "id=" + getId() +
                ", flight Code='" + getFlightCode() + '\'' +
                ", departure Airport='" + getDepartureAirport() + '\'' +
                ", departure Time='" + getDepartureTime() + '\'' +
                ", destination Airport='" + getDestinationAirport() + '\'' +
                ", arrival Time='" + getArrivalTime() + '\'' +
                '}';
    }


    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Flight other = (Flight) obj;
        return flightCode.equals(other.flightCode);
    }

    public List<FlightReservation> getFlightReservations() {
        return flightReservations;
    }

    public void setFlightReservations(List<FlightReservation> flightReservations) {
        this.flightReservations = flightReservations;
    }


}
