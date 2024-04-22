package database.util;

import javax.faces.application.FacesMessage;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

public class JSF {
    public static void addErrorMessage(String message) {
        addMessage(FacesMessage.SEVERITY_ERROR, message);
    }

    public static void addInfoMessage(String message) {
        addMessage(FacesMessage.SEVERITY_INFO, message);
    }

    public static void redirect(String view) throws IOException {
        if (!view.startsWith("/")) {
            view = "/"+view;
        }
        FacesContext context = FacesContext.getCurrentInstance();
        ExternalContext externalContext = context.getExternalContext();
        HttpServletRequest request = (HttpServletRequest) externalContext.getRequest();
        externalContext.redirect(externalContext.getRequestContextPath()+view);
    }

    public static void invalidateSession() {
        ExternalContext externalContext = FacesContext.getCurrentInstance().getExternalContext();
        externalContext.invalidateSession();
    }

    private static void addMessage(FacesMessage.Severity severity, String message) {
        FacesContext.getCurrentInstance().addMessage(null, new FacesMessage(severity, message, message));
    }


}

