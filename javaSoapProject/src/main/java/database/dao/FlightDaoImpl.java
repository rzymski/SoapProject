package database.dao;

import database.model.Flight;

import javax.ejb.Stateless;

@Stateless
public class FlightDaoImpl extends AbstractDaoJpaImpl<Flight> implements FlightDao{
}
