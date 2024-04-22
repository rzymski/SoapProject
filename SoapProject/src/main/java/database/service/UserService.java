/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.service;

import database.model.User;

import java.util.List;

public interface UserService {
    User save(User t);
    void delete (Long id);
    User findById(Long id);
    List<User> findAll();
    public User findByLogin(String login);
    public boolean verify(String login, String password);
}
