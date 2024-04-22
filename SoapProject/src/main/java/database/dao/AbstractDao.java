package database.dao;

import database.model.AbstractModel;

import java.util.List;
import java.util.Optional;

public interface AbstractDao<T extends AbstractModel>  {
    T save(T t);
    void delete(Long id);
    Optional<T> findById(Long id);
    List<T> findAll();
}
