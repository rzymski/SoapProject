package database.dao;

import database.model.UserGroup;

public interface UserGroupDao extends AbstractDao<UserGroup> {
    public UserGroup findUserGroupByName(String userGroupName);
}
