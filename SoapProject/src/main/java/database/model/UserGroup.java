package database.model;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@NamedQuery(name = "UserGroup.findUserGroupByName", query ="select ug from UserGroup ug where ug.name=?1")
public class UserGroup extends AbstractModel {
    private String name;

    public UserGroup() {
    }

    public UserGroup(String name) {
        this.name = name;
    }
    @OneToMany(mappedBy = "userGroup", orphanRemoval = true, cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<User> users = new ArrayList<>();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<User> getUsers() {
        return users;
    }

    public void setUsers(List<User> users) {
        this.users = users;
    }

    public void addUser(User user) {
        for(User u: users){
            if(u.getLogin().equals(user.getLogin())){
                throw new IllegalArgumentException();
            }
        }
        users.add(user);
        user.setUserGroup(this);
    }

    @Override
    public String toString() {
        return name;
    }
}
