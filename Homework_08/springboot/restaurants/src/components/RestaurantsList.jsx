import React from "react";

const RestaurantList = ({ restaurants, editRestaurant, deleteRestaurant }) => {
    return (
      <table className="table table-hover mt-3" align="center">
        <thead className="thead-light">
          <tr>
            <th scope="col">Nº</th>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">Phone</th>
            <th scope="col">Type</th>
            <th scope="col">Food Category</th>
            <th scope="col">Food Name</th>
            <th scope="col">Food Quantity</th>
            <th scope="col">Amount</th>
            <th scope="col">Option</th>
          </tr>
        </thead>
        {restaurants.map((restaurant, index) => {
          return (
            <tbody key={restaurant.restaurantId}>
              <tr>
                <th scope="row">{index + 1} </th>
                <td>{restaurant.name}</td>
                <td>{restaurant.address}</td>
                <td>{restaurant.phone}</td>
                <td>{restaurant.type}</td>
                <td>{restaurant.foodCategory}</td>
                <td>{restaurant.foodName}</td>
                <td>{restaurant.foodQuantity}</td>
                <td>{restaurant.amount}</td>
                <td>
                  <button
                    type="button"
                    className="btn btn-warning"
                    onClick={() => editRestaurant(restaurant)}
                  >
                    Edit
                  </button>
                  <button
                    type="button"
                    className="btn btn-danger mx-2"
                    onClick={() => deleteRestaurant(restaurant.restaurantId)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          );
        })}
      </table>
    );
  };
  
  export default RestaurantList;
  