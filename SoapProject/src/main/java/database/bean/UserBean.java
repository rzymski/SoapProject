package database.bean;


import database.model.User;
import database.service.UserService;

import javax.ejb.EJB;
import javax.enterprise.context.SessionScoped;
import javax.inject.Inject;
import javax.inject.Named;
import javax.security.enterprise.SecurityContext;
import java.io.Serializable;
import java.security.Principal;

@Named
@SessionScoped
public class UserBean implements Serializable {

    @EJB
    private UserService userService;

    @Inject
    private SecurityContext securityContext;

    private User user;

    public boolean isLogged() {
        return getLogin() != null;
    }

    public boolean isAdmin(){
        if(isLogged() && user.getUserGroup().getName() == "ROLE_ADMIN")
            return true;
        else
            return false;
    }

    public boolean isManager(){
        if(isLogged() && user.getUserGroup().getName() == "ROLE_MANAGER")
            return true;
        else
            return false;
    }

    public String getLogin() {
        if (user != null) {
            return user.getLogin();
        }

        Principal principal = securityContext.getCallerPrincipal();
        if (principal != null) {
            user = userService.findByLogin(principal.getName());
        }

        return user != null ? user.getLogin() : null;
    }
}
