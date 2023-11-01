package com.acs560.restaurants_api;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * The Restaurants class represents a restaurant entity with various properties including 
 * restaurantid, name, address, phone, type, food category, food name, food quantity, and amount.
 */
@Entity
@Table(name = "restaurants")
public class Restaurants {
	
	@Id
	@GeneratedValue
	private int restaurantId;
	private String restaurantName;
	private String restaurantAddress;
	private String restaurantPhone;
	private String restaurantType;
	private String foodCategory;
	private String foodName;
	private int foodQuantity;
	private float amount;
	
	/**
	 * Default constructor for the Restaurants class.
	 */
	public Restaurants() {
		
	}
	
	/**
	 * Retrieves the restaurant id.
	 * @return the restaurant id
	 */
	public int getRestaurantId() {
		return restaurantId;
	}
	
	/**
	 * Retrieves the restaurant name.
	 * @return the restaurant name
	 */
	public String getRestaurantName() {
		return restaurantName;
	}
	
	/**
	 * Retrieves the restaurant address.
	 * @return the restaurant address
	 */
	public String getRestaurantAddress() {
		return restaurantAddress;
	}
	
	/**
	 * Retrieves the restaurant phone number.
	 * @return the restaurant phone number
	 */
	public String getRestaurantPhone() {
		return restaurantPhone;
	}
	
	/**
	 * Retrieves the restaurant type.
	 * @return the restaurant type
	 */
	public String getRestaurantType() {
		return restaurantType;
	}
	
	/**
	 * Retrieves the food category.
	 * @return the food category
	 */
	public String getfoodCategory() {
		return foodCategory;
	}
	
	/**
	 * Retrieves the food name.
	 * @return the food name
	 */
	public String getfoodName() {
		return foodName;
	}
	
	/**
	 * Retrieves the food quantity.
	 * @return the food quantity
	 */
	public int getfoodQuantity() {
		return foodQuantity;
	}
	
	/**
	 * Retrieves the amount.
	 * @return the amount
	 */
	public float getfoodAmount() {
		return amount;
	}
	

	/**
	 * Sets the restaurant id.
	 * @param restaurantId the restaurant id to set
	 */
	public void setId(int restaurantId) {
		this.restaurantId = restaurantId;
	}
	
	/**
	 * Sets the restaurant name.
	 * @param restaurantName the restaurant name to set
	 */
	public void setRestaurantName(String restaurantName) {
		this.restaurantName = restaurantName;
	}
	
	/**
	 * Sets the restaurant address.
	 * @param restaurantAddress the restaurant address to set
	 */
	public void setAddress(String restaurantAddress) {
		this.restaurantAddress = restaurantAddress;
	}
	
	/**
	 * Sets the restaurant phone number.
	 * @param restaurantPhone the restaurant phone number to set
	 */
	public void setPhone(String restaurantPhone) {
		this.restaurantPhone = restaurantPhone;
	}
	
	/**
	 * Sets the restaurant type.
	 * @param restaurantType the restaurant type to set
	 */
	public void setType(String restaurantType) {
		this.restaurantType = restaurantType;
	}
	
	/**
	 * Sets the food category.
	 * @param foodCategory the food category to set
	 */
	public void setCategory(String foodCategory) {
		this.foodCategory = foodCategory;
	}
	
	/**
	 * Sets the food name.
	 * @param foodName the food name to set
	 */
	public void setFoodName(String foodName) {
		this.foodName = foodName;
	}
	
	/**
	 * Sets the food quantity.
	 * @param foodQuantity the food quantity to set
	 */
	public void setQuantity(int foodQuantity) {
		this.foodQuantity = foodQuantity;
	}
	
	/**
	 * Sets the amount.
	 * @param amount the amount to set
	 */
	public void setAmount(float amount) {
		this.amount = amount;
	}
}
