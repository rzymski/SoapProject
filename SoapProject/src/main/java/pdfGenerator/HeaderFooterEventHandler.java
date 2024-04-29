package pdfGenerator;


import com.itextpdf.kernel.events.Event;
import com.itextpdf.kernel.events.IEventHandler;
import com.itextpdf.kernel.events.PdfDocumentEvent;
import com.itextpdf.kernel.font.PdfFontFactory;
import com.itextpdf.kernel.geom.PageSize;
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfPage;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.kernel.pdf.canvas.PdfCanvas;

import java.io.IOException;

public class HeaderFooterEventHandler implements IEventHandler {

    private String headerText, footerTest;

    public HeaderFooterEventHandler(String headerText, String footerTest) {
        this.headerText = headerText;
        this.footerTest = footerTest;
    }

    @Override
    public void handleEvent(Event event) {
        PdfDocumentEvent docEvent = (PdfDocumentEvent) event;
        PdfDocument pdfDocument = docEvent.getDocument();
        PdfPage page = docEvent.getPage();

        PageSize pageSize = pdfDocument.getDefaultPageSize();
        float pageWidth = pageSize.getWidth();
        float pageHeight = pageSize.getHeight();

        System.out.println("[HeaderFooterEventHandler] Handle event");

        PdfCanvas pdfCanvas = new PdfCanvas(page.newContentStreamBefore(), page.getResources(), pdfDocument);

        System.out.println("[HeaderFooterEventHandler] Create pdfCanvas");

        try {
            pdfCanvas.beginText()
                    .setFontAndSize(PdfFontFactory.createFont(), 10)
                    .setLeading(10)
                    .moveText(pageWidth / 2, pageHeight - 20)
                    .showText(headerText)
                    .endText()
                    .beginText()
                    .setFontAndSize(PdfFontFactory.createFont(), 10)
                    .setLeading(10)
                    .moveText(pageWidth / 2, 20)
                    .showText(footerTest)
                    .endText();
            System.out.println("[HeaderFooterEventHandler] Create Header and Footer text");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        pdfCanvas.release();
        System.out.println("[HeaderFooterEventHandler] Release pdfCanvas");

    }
}
