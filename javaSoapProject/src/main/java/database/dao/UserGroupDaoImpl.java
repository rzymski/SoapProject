package database.dao;

import database.model.UserGroup;

import javax.ejb.Stateless;
import javax.persistence.TypedQuery;
import java.util.List;
import java.util.logging.Logger;

@Stateless
public class UserGroupDaoImpl extends AbstractDaoJpaImpl<UserGroup> implements UserGroupDao {
    private static Logger logger = Logger.getLogger(UserGroupDaoImpl.class.getName());
    @Override
    public UserGroup findUserGroupByName(String userGroupName) {
        logger.severe("findUserGroupByName wywolal sie z userGroupName = " + userGroupName);
        TypedQuery<UserGroup> query = em.createNamedQuery( "UserGroup.findUserGroupByName", UserGroup.class);
        query.setParameter(1, userGroupName);
        List<UserGroup> result = query.getResultList();
        return result.isEmpty() ? null : result.get(0);
    }
}
