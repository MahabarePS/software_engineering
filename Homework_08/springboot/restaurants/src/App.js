import "bootstrap/dist/css/bootstrap.css";
import api from "./api/axiosConfig";
import { useEffect, useState } from "react";
import "./App.css";
import RestaurantCrud from "./components/RestaurantsCrud";

function App() {
  const [restaurants, setRestaurants] = useState([]);

  /* manage side effects */
  useEffect(() => {
    (async () => await load())();
  }, []);

  async function load() {
    const result = await api.get("/all");
    setRestaurants(result.data);
  }

  return (
    <div>
      <h1 className="text-center">List Of Restaurants</h1>
      <RestaurantCrud load={load} restaurants={restaurants} />
    </div>
  );
}

export default App;
