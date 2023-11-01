package com.acs560.restaurants_api;

import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * The RestaurantsService class acts as an intermediate class that interacts with the RestaurantsRepository and 
 * provides various methods to perform CRUD operations on the Restaurants entity.
 */
@Service
public class RestaurantsService {
	@Autowired
	private RestaurantsRepository repository;
	
	/**
	 * Retrieves a list of all restaurants.
	 * @return a list of all restaurants
	 */
	public List<Restaurants> getRestaurantsList(){
		return (List<Restaurants>) repository.findAll();
	}
	
	/**
	 * Retrieves a specific restaurant based on the provided ID.
	 * @param id the ID of the restaurant
	 * @return the requested restaurant, or null if not found
	 */
	public Restaurants getRestaurants(int id) {
		Optional<Restaurants> restaurants = repository.findById(id);
		return restaurants.orElse(null);
	}
	
	/**
	 * Stores a new or updated restaurant.
	 * @param restaurants the restaurant to be stored or updated
	 * @return the stored or updated restaurant
	 */
	public Restaurants storeRestaurants(Restaurants restaurants) {
		return repository.save(restaurants);
	}
	
	/**
	 * Deletes a restaurant based on the provided ID.
	 * @param id the ID of the restaurant to be deleted
	 * @return true if the restaurant was deleted successfully, false otherwise
	 */
	public boolean deleteRestaurants(int id) {
		boolean deleted = false;
		Optional<Restaurants> restaurants = repository.findById(id);
		
		if(restaurants.isPresent()) {
			repository.delete(restaurants.get());
			deleted = true;
		}
		return deleted;
	}
}
