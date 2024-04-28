from client import *
from createPDF import PDF

logo = BytesIO(soapService.service("downloadImage"))
flightReservationData = soapService.service("checkFlightReservation", "653")
print(flightReservationData)
login = flightReservationData['login']
email = flightReservationData['email']
flightCode = flightReservationData['flightCode']
departureAirport = flightReservationData['departureAirport']
departureTime = datetime.strptime(flightReservationData['departureTime'], "%Y-%m-%dT%H:%M:%S").__str__()
destinationAirport = flightReservationData['destinationAirport']
arrivalTime = datetime.strptime(flightReservationData['arrivalTime'], "%Y-%m-%dT%H:%M:%S").__str__()
numberOfReservedSeats = flightReservationData['numberOfReservedSeats']

pdf = PDF(titlePDF="../pdfs/ticketConfirmation.pdf",
          title="Confirmation of Airline Ticket Purchase",
          image=logo,
          username=login,
          email=email,
          flightCode=flightCode,
          numberOfReservedSeats=numberOfReservedSeats,
          departureAirport=departureAirport,
          departureTime=departureTime,
          destinationAirport=destinationAirport,
          arrivalTime=arrivalTime
          )