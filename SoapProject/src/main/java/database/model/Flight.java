package database.model;

import database.adapter.LocalDateTimeAdapter;

import javax.persistence.*;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import java.time.LocalDateTime;

@Entity
@NamedQuery(name = "Flight.findFlightByFromCity", query ="select f from Flight f where f.departureAirport=?1")
@NamedQuery(name = "Flight.findFlightByToCity", query ="select f from Flight f where f.destinationAirport=?1")
public class Flight extends AbstractModel {
    private String flightCode;
    private String departureAirport;
    @Column(nullable = false)
    private LocalDateTime departureTime;
    private String destinationAirport;
    @Column(nullable = false)
    private LocalDateTime arrivalTime;
    private int capacity;
    private int occupiedSeats;

    public Flight(){}
    public Flight(String flightCode, String departureAirport, LocalDateTime departureTime,
                  String destinationAirport, LocalDateTime arrivalTime) {
        this(flightCode, departureAirport, departureTime, destinationAirport, arrivalTime, 100);
    }
    public Flight(String flightCode, String departureAirport, LocalDateTime departureTime,
                  String destinationAirport, LocalDateTime arrivalTime, int capacity)
    {
        this.flightCode = flightCode;
        this.departureAirport = departureAirport;
        this.departureTime = departureTime;
        this.destinationAirport = destinationAirport;
        this.arrivalTime = arrivalTime;
        this.capacity = capacity;
        this.occupiedSeats = 0;
    }

    public int getCapacity() { return capacity; }

    public void setCapacity(int capacity) { this.capacity = capacity; }

    public int getOccupiedSeats() { return occupiedSeats; }

    public void setOccupiedSeats(int occupiedSeats) { this.occupiedSeats = occupiedSeats; }

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
}
