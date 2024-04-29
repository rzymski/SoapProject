package pdfGenerator;
import com.itextpdf.io.image.ImageData;
import com.itextpdf.io.image.ImageDataFactory;
import com.itextpdf.kernel.events.PdfDocumentEvent;
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Image;
import com.itextpdf.layout.element.Paragraph;

import java.io.FileNotFoundException;
import java.net.MalformedURLException;

public class PdfGenerator {

    private final PdfWriter _writer;
    private final String _outPath;

    private boolean isHeaderFooter;
    private boolean isImage;

    private String headerText;
    private String footerText;

    private String imagePath;

    public PdfGenerator(String outPath) throws FileNotFoundException {
        this._writer = new PdfWriter(outPath);
        this._outPath = outPath;

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

        pdfDocument.addNewPage();

        Document document = new Document(pdfDocument);

        if(isHeaderFooter) {
            pdfDocument.addEventHandler(PdfDocumentEvent.END_PAGE, new HeaderFooterEventHandler(headerText, footerText));
            System.out.println("[PdfGenerator] Add header and footer event handler");
        }

        Paragraph paragraph = new Paragraph("Pdf Generator");
        document.add(paragraph);
        System.out.println("[PdfGenerator] Add paragraph");

        if(isImage) {
            ImageData id = ImageDataFactory.create(imagePath);
            Image img = new Image(id);

            img.scaleAbsolute(100, 100);

            document.add(img);
            System.out.println("[PdfGenerator] Add image");
        }

        document.close();

        System.out.println("[PdfGenerator] Document closed");
        System.out.println("[PdfGenerator] Document created at " + _outPath);

    }
}