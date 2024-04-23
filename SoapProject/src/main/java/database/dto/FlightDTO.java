package database.dto;

import database.adapter.LocalDateTimeAdapter;
import database.model.Flight;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "FlightDTO")
public class FlightDTO {

    protected Long id;
    protected String flightCode;
    protected String departureAirport;
    protected LocalDateTime departureTime;
    protected String destinationAirport;
    protected LocalDateTime arrivalTime;
    protected Long capacity;

    public FlightDTO(){}

    public FlightDTO(Flight flight){
        this.id = flight.getId();
        this.flightCode = flight.getFlightCode();
        this.departureAirport = flight.getDepartureAirport();
        this.departureTime = flight.getDepartureTime();
        this.destinationAirport = flight.getDestinationAirport();
        this.arrivalTime = flight.getArrivalTime();
        this.capacity = flight.getCapacity();
    }

    public FlightDTO(Long id, String flightCode, String departureAirport, LocalDateTime departureTime, String destinationAirport, LocalDateTime arrivalTime, Long capacity)
    {
        this.id = id;
        this.flightCode = flightCode;
        this.departureAirport = departureAirport;
        this.departureTime = departureTime;
        this.destinationAirport = destinationAirport;
        this.arrivalTime = arrivalTime;
        this.capacity = capacity;
    }

    @XmlAttribute
    public Long getId() { return id; }

    @XmlElement(name = "flightCode")
    public String getFlightCode() { return flightCode; }

    @XmlElement(name = "departureAirport")
    public String getDepartureAirport() { return departureAirport; }

    @XmlElement(name = "departureTime")
    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    public LocalDateTime getDepartureTime() { return departureTime; }

    @XmlElement(name = "destinationAirport")
    public String getDestinationAirport() { return destinationAirport; }

    @XmlElement(name = "arrivalTime")
    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    public LocalDateTime getArrivalTime() { return arrivalTime; }

    @XmlElement(name = "capacity")
    public Long getCapacity() { return capacity; }

    public void setId(Long id) {
        this.id = id;
    }

    public void setFlightCode(String flightCode) {
        this.flightCode = flightCode;
    }

    public void setDepartureAirport(String departureAirport) {
        this.departureAirport = departureAirport;
    }

    public void setDepartureTime(LocalDateTime departureTime) {
        this.departureTime = departureTime;
    }

    public void setDestinationAirport(String destinationAirport) {
        this.destinationAirport = destinationAirport;
    }

    public void setArrivalTime(LocalDateTime arrivalTime) {
        this.arrivalTime = arrivalTime;
    }

    public void setCapacity(Long capacity) {
        this.capacity = capacity;
    }

    @Override
    public String toString() {
        return "FlightDTO{" +
                "id=" + id +
                ", flightCode='" + flightCode + '\'' +
                ", departureAirport='" + departureAirport + '\'' +
                ", departureTime=" + departureTime +
                ", destinationAirport='" + destinationAirport + '\'' +
                ", arrivalTime=" + arrivalTime +
                ", capacity=" + capacity +
                '}';
    }

    public static List<FlightDTO> createFromFlightsFlightDTOs(List<Flight> flights) {
        List<FlightDTO> flightDTOs = new ArrayList<>();
        for (Flight flight : flights) {
            flightDTOs.add(new FlightDTO(flight));
        }
        return flightDTOs;
    }
}