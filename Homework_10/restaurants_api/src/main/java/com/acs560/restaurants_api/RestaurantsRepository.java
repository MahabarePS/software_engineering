package com.acs560.restaurants_api;

import org.springframework.data.repository.CrudRepository;

/**
 * The RestaurantsRepository interface provides CRUD (Create, Read, Update, Delete) operations for the Restaurants entity.
 * It extends the CrudRepository interface.
 * @param <Restaurants> the entity type for the repository
 * @param <Integer> the type of the primary key of the entity
 */
public interface RestaurantsRepository extends CrudRepository<Restaurants, Integer> {

}
