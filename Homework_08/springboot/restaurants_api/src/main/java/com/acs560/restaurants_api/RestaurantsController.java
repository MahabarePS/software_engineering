package com.acs560.restaurants_api;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * The RestaurantsController class is responsible for handling HTTP requests related to restaurant operations.
 */
@RequestMapping("restaurants")
@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class RestaurantsController {

	@Autowired
	private RestaurantsService service;
	
	/**
	 * Retrieves a list of all restaurants.
	 * @return a list of all restaurants
	 */
	@GetMapping()
	public List<Restaurants> getRestaurants(){
		return service.getRestaurantsList();
	}
	
	/**
	 * Retrieves a specific restaurant based on the provided restaurant ID.
	 * @param id the restaurant ID
	 * @return a ResponseEntity with the requested restaurant or a NOT_FOUND status if the restaurant is not found
	 */
	@GetMapping("/{restaurantId}")
	public ResponseEntity<Restaurants> getRestaurant(@PathVariable("restaurantId") int id){
		Restaurants restaurants = service.getRestaurants(id);
		return restaurants != null ? new ResponseEntity<>(restaurants, HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
	
	/**
	 * Adds a new restaurant.
	 * @param restaurants the restaurant to be added
	 * @return a ResponseEntity indicating the status of the operation
	 */
	@PostMapping()
	public ResponseEntity<String> addRestaurant(@RequestBody Restaurants restaurants){
		return service.storeRestaurants(restaurants) != null ? new ResponseEntity<>("Saved Successfully", HttpStatus.OK)
				: new ResponseEntity<>("Not Saved Successfully", HttpStatus.OK);
	}
	
	/**
	 * Updates an existing restaurant based on the provided restaurant ID.
	 * @param id the restaurant ID
	 * @param restaurants the updated restaurant information
	 * @return a ResponseEntity indicating the status of the operation
	 */
	@PutMapping("/{restaurantId}")
	public ResponseEntity<String> updateRestaurant(@PathVariable("restaurantId") int id, @RequestBody Restaurants restaurants){
		Restaurants exRestaurants = service.getRestaurants(id);
		exRestaurants.setId(id);
		return exRestaurants != null ? service.storeRestaurants(restaurants) != null
				? new ResponseEntity<>("Updated Successfully", HttpStatus.OK)
				: new ResponseEntity<>("Not Updated Successfully", HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
	
	/**
	 * Deletes a restaurant based on the provided restaurant ID.
	 * @param id the restaurant ID
	 * @return a ResponseEntity indicating the status of the operation
	 */
	@DeleteMapping("/{restaurantId}")
	public ResponseEntity<String> deleteRestaurant(@PathVariable("restaurantId") int id){
		Restaurants exRestaurant = service.getRestaurants(id);
		return exRestaurant != null ? service.deleteRestaurants(id)
				? new ResponseEntity<>("Deleted Successfully", HttpStatus.OK)
				: new ResponseEntity<>("Not Deleted Successfully", HttpStatus.OK)
				: new ResponseEntity<>(HttpStatus.NOT_FOUND);
	}
	
	/**
	 * Default mapping method for the root path.
	 * @return the string "index"
	 */
	@RequestMapping(value = "/")
	public String index() {
		return "index";
	}
}
