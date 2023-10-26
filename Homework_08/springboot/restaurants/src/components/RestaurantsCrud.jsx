import { useState } from "react";
import api from "../api/axiosConfig";
import PublisherList from "./RestaurantsList";

const RestaurantCrud = ({ load, restaurants }) => {
    /* state definition  */
    const [restaurantId, setRestaurantId] = useState("");
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [phone, setPhone] = useState("");
    const [type, setType] = useState("");
    const [foodCategory, setFoodCategory] = useState("");
    const [foodName, setFoodName] = useState("");
    const [foodQuantity, setFoodQuantity] = useState("");
    const [amount, setAmount] = useState("");
  
    /* begin handlers */
    async function save(event) {
      event.preventDefault();
      await api.post("/create", {
        name: name,
        address: address,
        phone: phone,
        type: type,
        foodCategory: foodCategory,
        foodName: foodName,
        foodQuantity: foodQuantity,
        amount: amount,
      });
      alert("Restaurant Record Saved");
      // reset state
      setRestaurantId("");
      setName("");
      setAddress("");
      setPhone("");
      setType("");
      setFoodCategory("");
      setFoodName("");
      setFoodQuantity("");
      setAmount("");
      load();
    }
  
    async function editRestaurant(restaurant) {
      setName(restaurant.name);
      setAddress(restaurant.address);
      setPhone(restaurant.phone);
      setType(restaurant.type);
      setFoodCategory(restaurant.foodCategory);
      setFoodName(restaurant.foodName);
      setFoodQuantity(restaurant.foodQuantity);
      setAmount(restaurant.amount);
      setRestaurantId(restaurant.restaurantId);
    }
  
    async function deleteRestaurant(restaurantId) {
      await api.delete("/delete/" + restaurantId);
      alert("Restaurant Details Deleted Successfully");
      load();
    }
  
    async function update(event) {
      event.preventDefault();
      if (!restaurantId) return alert("Restaurant Details Not Found");
      await api.put("/update", {
        restaurantId: restaurantId,
        name: name,
        address: address,
        phone: phone,
        type: type,
        foodCategory: foodCategory,
        foodName: foodName,
        foodQuantity: foodQuantity,
        amount: amount,
      });
      alert("Restaurant Details Updated");
      // reset state
      setRestaurantId("");
      setName("");
      setAddress("");
      setPhone("");
      setType("");
      setFoodCategory("");
      setFoodName("");
      setFoodQuantity("");
      setAmount("");
      load();
    }
    /* end handlers */
  
    /* jsx */
    return (
      <div className="container mt-4">
        <form>
          <div className="form-group my-2">
            <input
              type="text"
              className="form-control"
              hidden
              value={restaurantId}
              onChange={(e) => setRestaurantId(e.target.value)}
            />
            <label>Name</label>
            <input
              type="text"
              className="form-control"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Address</label>
            <input
              type="text"
              className="form-control"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Phone</label>
            <input
              type="text"
              className="form-control"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Type</label>
            <input
              type="text"
              className="form-control"
              value={type}
              onChange={(e) => setType(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Food Category</label>
            <input
              type="text"
              className="form-control"
              value={foodCategory}
              onChange={(e) => setFoodCategory(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Food Name</label>
            <input
              type="text"
              className="form-control"
              value={foodName}
              onChange={(e) => setFoodName(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Food Quantity</label>
            <input
              type="text"
              className="form-control"
              value={foodQuantity}
              onChange={(e) => setFoodQuantity(e.target.value)}
            />
          </div>
  
          <div className="form-group mb-2">
            <label>Amount</label>
            <input
              type="text"
              className="form-control"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
            />
          </div>
  
          <div>
            <button className="btn btn-primary m-4" onClick={save}>
              POST
            </button>
            <button className="btn btn-warning m-4" onClick={update}>
              PUT
            </button>
          </div>
        </form>
        <PublisherList
          restaurants={restaurants}
          editRestaurant={editRestaurant}
          deleteRestaurant={deleteRestaurant}
        />
      </div>
    );
  };
  
  export default RestaurantCrud;
  