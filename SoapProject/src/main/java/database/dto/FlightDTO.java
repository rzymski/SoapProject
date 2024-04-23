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
////    @XmlAttribute
//    protected Long id;
//    protected String flightCode;
//    protected String departureAirport;
//
////    @XmlElement(name = "DepartureTime")
//    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
//    protected LocalDateTime departureTimeX;
//
//    protected String destinationAirport;
//
////    @XmlElement(name = "ArrivalTime")
//    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
//    protected LocalDateTime arrivalTimeX;
//
//    protected Long capacity;

    @XmlAttribute
    protected Long id;

    @XmlElement(name = "FlightCode")
    protected String flightCode;

    @XmlElement(name = "DepartureAirport")
    protected String departureAirport;

    @XmlElement(name = "DepartureTime")
    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    protected LocalDateTime departureTimeX;

    @XmlElement(name = "DestinationAirport")
    protected String destinationAirport;

    @XmlElement(name = "ArrivalTime")
    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    protected LocalDateTime arrivalTimeX;

    @XmlElement(name = "Capacity")
    protected Long capacity;



    public FlightDTO(){}

    public FlightDTO(Flight flight){
        this.id = flight.getId();
        this.flightCode = flight.getFlightCode();
        this.departureAirport = flight.getDepartureAirport();
        this.departureTimeX = flight.getDepartureTime();
        this.destinationAirport = flight.getDestinationAirport();
        this.arrivalTimeX = flight.getArrivalTime();
        this.capacity = flight.getCapacity();
    }

    public FlightDTO(Long id, String flightCode, String departureAirport, LocalDateTime departureTime, String destinationAirport, LocalDateTime arrivalTime, Long capacity)
    {
        this.id = id;
        this.flightCode = flightCode;
        this.departureAirport = departureAirport;
        this.departureTimeX = departureTime;
        this.destinationAirport = destinationAirport;
        this.arrivalTimeX = arrivalTime;
        this.capacity = capacity;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFlightCode() {
        return flightCode;
    }

    public void setFlightCode(String flightCode) {
        this.flightCode = flightCode;
    }

    public String getDepartureAirport() {
        return departureAirport;
    }

    public void setDepartureAirport(String departureAirport) {
        this.departureAirport = departureAirport;
    }

    public LocalDateTime getDepartureTime() {
        return departureTimeX;
    }

    public void setDepartureTime(LocalDateTime departureTime) {
        this.departureTimeX = departureTime;
    }

    public String getDestinationAirport() {
        return destinationAirport;
    }

    public void setDestinationAirport(String destinationAirport) {
        this.destinationAirport = destinationAirport;
    }

    public LocalDateTime getArrivalTime() {
        return arrivalTimeX;
    }

    public void setArrivalTime(LocalDateTime arrivalTime) {
        this.arrivalTimeX = arrivalTime;
    }

    public Long getCapacity() {
        return capacity;
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
                ", departureTimeX=" + departureTimeX +
                ", destinationAirport='" + destinationAirport + '\'' +
                ", arrivalTimeX=" + arrivalTimeX +
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