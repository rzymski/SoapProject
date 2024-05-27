# from client import *
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import inch
# from reportlab.platypus import Image as PDFImage, SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from datetime import datetime
#
#
# class PDF:
#     @staticmethod
#     def createSpacer(height):
#         return Spacer(1, height * inch)
#
#     @staticmethod
#     def createCenteredImage(imageData, width=3 * inch, height=3 * inch):
#         pdfImage = PDFImage(imageData, width=width, height=height)
#         pdfImage.hAlign = 'CENTER'
#         return pdfImage
#
#     @staticmethod
#     def createTwoColumnTable(left_text, right_text, col_widths=[3 * inch, 3 * inch]):
#         left_paragraph = Paragraph(left_text, getSampleStyleSheet()["BodyText"])
#         right_paragraph = Paragraph(right_text, getSampleStyleSheet()["BodyText"])
#         table = Table([[left_paragraph, right_paragraph]], colWidths=col_widths)
#         table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))
#         return table
#
#     @staticmethod
#     def createBulletList(items):
#         bullet_style = getSampleStyleSheet()["BodyText"]
#         elements = []
#         for item in items:
#             elements.append(Paragraph(f"- {item}", bullet_style))
#             elements.append(PDF.createSpacer(0.1))
#         return elements
#
#     def __init__(self, titlePDF, title, pdfImage, username, email, flightCode, numberOfReservedSeats, departureAirport, departureTime, destinationAirport, arrivalTime):
#         # Konfiguracja PDF
#         pdf_file = titlePDF
#         document = SimpleDocTemplate(pdf_file, pagesize=A4)
#         elements = []
#         # Dodanie tytułu
#         title_style = getSampleStyleSheet()["Title"]
#         titleParagraph = Paragraph(title, title_style)
#         elements.append(titleParagraph)
#         elements.append(PDF.createSpacer(0.5))
#         # Dodanie wycentrowanego obrazka
#         elements.append(PDF.createCenteredImage(pdfImage))
#         elements.append(PDF.createSpacer(0.5))
#         # Dodanie wypunktowanej listy
#         info = [
#             f"Username: {username}",
#             f"Email: {email}",
#             f"Flight code: {flightCode}",
#             f"Reserved seats: {numberOfReservedSeats}",
#         ]
#         elements.extend(PDF.createBulletList(info))
#         # Dodanie tekstu w dwóch kolumnach
#         elements.append(Paragraph("From: ", getSampleStyleSheet()["BodyText"]))
#         elements.append(PDF.createTwoColumnTable(departureAirport, departureTime))
#         elements.append(Paragraph("To: ", getSampleStyleSheet()["BodyText"]))
#         elements.append(PDF.createTwoColumnTable(destinationAirport, arrivalTime))
#         # Generowanie PDF-a
#         document.build(elements)
#         print(f"PDF został wygenerowany: {pdf_file}")
#
#
# if __name__ == "__main__":
#     soapService = AirportClient(8080, [], "localhost", "SoapProject/AirportServerImplService")
#     logo = BytesIO(soapService.service("downloadImage"))
#     flightReservationData = soapService.service("checkFlightReservation", "653")
#     print(flightReservationData)
#     login = flightReservationData['login']
#     email = flightReservationData['email']
#     flightCode = flightReservationData['flightCode']
#     departureAirport = flightReservationData['departureAirport']
#     departureTime = datetime.strptime(flightReservationData['departureTime'], "%Y-%m-%dT%H:%M:%S").__str__()
#     destinationAirport = flightReservationData['destinationAirport']
#     arrivalTime = datetime.strptime(flightReservationData['arrivalTime'], "%Y-%m-%dT%H:%M:%S").__str__()
#     numberOfReservedSeats = flightReservationData['numberOfReservedSeats']
#
#     pdf = PDF(titlePDF="../pdfs/ticketConfirmation.pdf",
#               title="Confirmation of Airline Ticket Purchase",
#               pdfImage=logo,
#               username=login,
#               email=email,
#               flightCode=flightCode,
#               numberOfReservedSeats=numberOfReservedSeats,
#               departureAirport=departureAirport,
#               departureTime=departureTime,
#               destinationAirport=destinationAirport,
#               arrivalTime=arrivalTime
#               )
