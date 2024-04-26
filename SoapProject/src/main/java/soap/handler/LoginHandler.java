package soap.handler;

import database.service.UserService;
import soap.service.AirportServerImpl;

import javax.inject.Inject;
import javax.xml.namespace.QName;
import javax.xml.soap.*;
import javax.xml.ws.handler.MessageContext;
import javax.xml.ws.handler.soap.SOAPHandler;
import javax.xml.ws.handler.soap.SOAPMessageContext;
import javax.xml.ws.soap.SOAPFaultException;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.logging.Logger;

public class LoginHandler implements SOAPHandler<SOAPMessageContext>{
    private static Logger logger = Logger.getLogger(LoginHandler.class.getName());

    public static final String USER_CONTEXT_KEY = "authenticatedUser";

    @Inject
    UserService userService;

    @Override
    public boolean handleMessage(SOAPMessageContext context) {
        logger.warning("Server : handleMessage()......");
        Boolean isRequest = (Boolean) context.get(MessageContext.MESSAGE_OUTBOUND_PROPERTY);
        if(!isRequest){
            try{
                SOAPMessage soapMsg = context.getMessage();
                SOAPEnvelope soapEnv = soapMsg.getSOAPPart().getEnvelope();
                SOAPHeader soapHeader = soapEnv.getHeader();
                //if no header, add one
                if (soapHeader == null){
                    soapHeader = soapEnv.addHeader();
                    generateSOAPErrMessage(soapMsg, "No SOAP header.");
                } else {

                }

                String username = null;
                String password = null;
                Map<String, List<String>> httpHeaders = (Map<String, List<String>>) context.get(MessageContext.HTTP_REQUEST_HEADERS);
                if (httpHeaders != null) {
                    List<String> usernameList = httpHeaders.get("username");
                    if (usernameList != null && !usernameList.isEmpty()) {
                        username = usernameList.get(0);
                    }
                    List<String> passwordList = httpHeaders.get("password");
                    if (passwordList != null && !passwordList.isEmpty()) {
                        password = passwordList.get(0);
                    }
                }
                logger.warning("username: " + username);
                logger.warning("password: " + password);
                boolean verification = userService.verify(username, password);
                if (verification) {
                    context.put(USER_CONTEXT_KEY, username);
                    context.setScope(USER_CONTEXT_KEY, MessageContext.Scope.APPLICATION);
                }

                ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
                soapMsg.writeTo(outputStream);
                String soapMessageString = outputStream.toString(StandardCharsets.UTF_8.name());
                logger.warning("SOAP Message: " + soapMessageString);
            } catch(SOAPException e){
                logger.warning("Wystąpił błąd podczas logowania wiadomości SOAP: " + e.toString());
            } catch(IOException e){
                logger.warning(e.toString());
            }
        }
        return true;
    }

    @Override
    public boolean handleFault(SOAPMessageContext context) {
        logger.warning("Server : handleFault()......");
        return true;
    }

    @Override
    public void close(MessageContext context) {
        logger.warning("Server : close()......");
    }

    @Override
    public Set<QName> getHeaders() {
        logger.warning("Server : getHeaders()......");
        return null;
    }

    private void generateSOAPErrMessage(SOAPMessage msg, String reason) {
        logger.warning("Brak danych do przetworzenia przez Handlera, wyrzuca wyjatek");
        logger.warning("Wiadomosc = " + msg);
        logger.warning("Powod = " + reason);
        try {
            SOAPBody soapBody = msg.getSOAPPart().getEnvelope().getBody();
            SOAPFault soapFault = soapBody.addFault();
            soapFault.setFaultString(reason);
            throw new SOAPFaultException(soapFault);
        } catch (SOAPException e) { }
    }
}
