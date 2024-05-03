package pdfGenerator;
import com.itextpdf.io.image.ImageData;
import com.itextpdf.io.image.ImageDataFactory;
import com.itextpdf.kernel.colors.Color;
import com.itextpdf.kernel.colors.ColorConstants;
import com.itextpdf.kernel.colors.DeviceRgb;
import com.itextpdf.kernel.events.PdfDocumentEvent;
import com.itextpdf.kernel.geom.PageSize;
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.borders.Border;
import com.itextpdf.layout.element.*;
import com.itextpdf.layout.element.Image;
import com.itextpdf.layout.properties.TextAlignment;
import com.itextpdf.layout.properties.VerticalAlignment;
import database.dto.FlightDTO;
import database.dto.FlightReservationDTO;
import com.itextpdf.layout.Canvas;



import java.awt.*;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.file.Files;

public class PdfGenerator {

    private final PdfWriter _writer;
    private final FlightReservationDTO _reservation;

    private boolean isHeaderFooter;
    private boolean isImage;

    private String headerText;
    private String footerText;

    private String imagePath;

    public PdfGenerator(ByteArrayOutputStream outputStream, FlightReservationDTO reservation) throws FileNotFoundException {
        this._writer = new PdfWriter(outputStream);
        this._reservation = reservation;

        this.isHeaderFooter = false;
        this.isImage = false;

        System.out.println("[PdfGenerator] Generator created");
    }

    public void setHeaderFooter(String headerText, String footerText) {
        this.headerText = headerText;
        this.footerText = footerText;

        this.isHeaderFooter = true;

        System.out.println("[PdfGenerator] Set header footer text");

    }

    public void setImage(String imgPath) {
        this.imagePath = imgPath;
        this.isImage = true;

        System.out.println("[PdfGenerator] Set image path as " + imagePath);
    }

    public void generate() throws MalformedURLException {
        PdfDocument pdfDocument = new PdfDocument(_writer);
        System.out.println("[PdfGenerator] Create document");

        pdfDocument.setDefaultPageSize(PageSize.A4);

        float col = 280f;
        float[] columnWidth = {col, col};

        Table table = new Table(columnWidth);

        table.setBackgroundColor(new DeviceRgb(63, 169, 219))
                        .setFontColor(ColorConstants.WHITE);

        table.addCell(new Cell().add(new Paragraph("Reservation"))
                            .setTextAlignment(TextAlignment.CENTER)
                            .setVerticalAlignment(VerticalAlignment.MIDDLE)
                            .setMarginTop(30f)
                            .setMarginBottom(30f)
                            .setFontSize(30f)
                            .setBorder(Border.NO_BORDER));

        table.addCell(new Cell().add(
                new Paragraph("Reservation number: " + _reservation.getReservationId() + "\n" +
                        "Current reservations count: " + _reservation.getNumberOfReservedSeats())
        ).setTextAlignment(TextAlignment.RIGHT)
                .setMarginTop(30f)
                .setMarginBottom(30f)
                .setMarginRight(10f)
                .setBorder(Border.NO_BORDER));

        Text text = new Text("Your data\n").setFontSize(17).setBold();
        Paragraph userDataHeader = new Paragraph(text).setMarginTop(25f);
        Paragraph userData = new Paragraph("Login: " + _reservation.getLogin() + "\n"
                                                + "E-mail: " + _reservation.getEmail() + "\n");

        Text text2 = new Text("Flight " + _reservation.getFlightCode()).setFontSize(17).setBold();
        Paragraph flightDataHeader = new Paragraph(text2);
        Paragraph flightData = new Paragraph("Departure: " + _reservation.getDepartureAirport() + " at " + FlightDTO.getStringFromDate(_reservation.getDepartureTime()) + "  ----->  "
                                                + "Destination: " + _reservation.getDestinationAirport() + " at " + FlightDTO.getStringFromDate(_reservation.getArrivalTime()));

        //watermark

        ImageData imageData = ImageDataFactory.create(imagePath);
        Image image = new Image(imageData);

        image.setFixedPosition(pdfDocument.getDefaultPageSize().getWidth()/2-320, pdfDocument.getDefaultPageSize().getHeight()/2-160);
        image.setOpacity(0.3f);

        Document document = new Document(pdfDocument);

        document.add(table);

        document.add(userDataHeader);
        document.add(userData);

        document.add(flightDataHeader);
        document.add(flightData);

        document.add(image);

        document.close();

        /*
        pdfDocument.addNewPage();

        Document document = new Document(pdfDocument);

        if(isHeaderFooter) {
            pdfDocument.addEventHandler(PdfDocumentEvent.END_PAGE, new HeaderFooterEventHandler(headerText, footerText));
            System.out.println("[PdfGenerator] Add header and footer event handler");
        }

        Paragraph paragraph = new Paragraph("Pdf Generator");
        document.add(paragraph);
        System.out.println("[PdfGenerator] Add paragraph");

        Paragraph paragraph1 = new Paragraph(_reservation.getLogin() + " " + _reservation.getEmail() + "\n" +
                                                _reservation.getFlightCode() + " " + _reservation.getNumberOfReservedSeats());
        document.add(paragraph1);

        if(isImage) {
            ImageData id = ImageDataFactory.create(imagePath);
            Image img = new Image(id);

            img.scaleAbsolute(100, 100);

            document.add(img);
            System.out.println("[PdfGenerator] Add image");
        }


*/

        System.out.println("[PdfGenerator] Document closed");
    }
}