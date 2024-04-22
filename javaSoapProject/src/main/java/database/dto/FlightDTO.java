package database.dto;

import database.conventor.LocalDateTimeAdapter;

import java.time.LocalDateTime;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "FlightDTO")
public class FlightDTO {
    private String flightCode;
    private String departureAirport;

    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    private LocalDateTime departureTimeX;

    private String destinationAirport;

    @XmlJavaTypeAdapter(LocalDateTimeAdapter.class)
    private LocalDateTime arrivalTimeX;

    public FlightDTO(){}

    public FlightDTO(String flightCode, String departureAirport, LocalDateTime departureTime, String destinationAirport, LocalDateTime arrivalTime)
    {
        this.flightCode = flightCode;
        this.departureAirport = departureAirport;
        this.departureTimeX = departureTime;
        this.destinationAirport = destinationAirport;
        this.arrivalTimeX = arrivalTime;
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

    @Override
    public String toString() {
        return "FlightDTO{" +
                ", flight Code='" + getFlightCode() + '\'' +
                ", departure Airport='" + getDepartureAirport() + '\'' +
                ", departure Time='" + getDepartureTime() + '\'' +
                ", destination Airport='" + getDestinationAirport() + '\'' +
                ", arrival Time='" + getArrivalTime() + '\'' +
                '}';
    }
}
