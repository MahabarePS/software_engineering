"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Homework_12
Goal: API to interact with mySQL DB
Submited by: Prasad Sadanand Mahabare
"""
# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Winacs%40560$$@127.0.0.1:3306/sys'
db = SQLAlchemy(app)

# Define a database model for restaurant menus
class RestaurantMenu(db.Model):
    __tablename__ = 'restaurant_menus'

    # Define fields for the restaurant menu
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    vegetarian = db.Column(db.Boolean, default=False)
    available = db.Column(db.Boolean, default=True)

# Define route to fetch all restaurant menus
@app.route('/Menus', methods=['GET'])
def get_menus():
    menus = RestaurantMenu.query.all()
    menus_data = [{
        "id": menu.id,
        "dish_name": menu.dish_name,
        "description": menu.description,
        "price": menu.price,
        "vegetarian": menu.vegetarian,
        "available": menu.available
    } for menu in menus]
    return jsonify(menus_data)

# Define route to fetch a specific menu by ID
@app.route('/Menus/<int:id>', methods=['GET'])
def get_menu(id):
    menu = RestaurantMenu.query.get(id)
    
    if menu is None:
        return jsonify({"message": "Menu item not found"}), 404
    
    menu_data = {
        "id": menu.id,
        "dish_name": menu.dish_name,
        "description": menu.description,
        "price": menu.price,
        "vegetarian": menu.vegetarian,
        "available": menu.available
    }
    
    return jsonify(menu_data)

# Define route to add a new menu item
@app.route('/Menus', methods=['POST'])
def add_menu():
    data = request.json
    menu = RestaurantMenu(
        dish_name=data['dish_name'],
        description=data.get('description', ''),
        price=data['price'],
        vegetarian=data['vegetarian'],
        available=data.get('available', True)
    )
    db.session.add(menu)
    db.session.commit()
    return "Menu item added successfully", 201

# Define route to update a menu item by ID
@app.route('/Menus/<int:id>', methods=['PUT'])
def update_menu(id):
    menu = RestaurantMenu.query.get(id)
    
    if menu is None:
        return jsonify({"message": "Menu item not found"}), 404

    try:
        data = request.json
        # Update fields based on the data received
        if 'description' in data:
            menu.description = data['description']
        if 'price' in data:
            menu.price = data['price']
        if 'vegetarian' in data:
            menu.vegetarian = data['vegetarian']
        if 'available' in data:
            menu.available = data['available']

        db.session.commit()
        return jsonify({"message": "Menu item updated successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Define route to delete a menu item by ID
@app.route('/Menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    menu = RestaurantMenu.query.get(id)
    if menu:
        db.session.delete(menu)
        db.session.commit()
        return jsonify({"message": "Menu item deleted successfully"}), 200
    else:
        return jsonify({"message": "Menu item not found"}), 404

# Entry point to run the Flask application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask app in debug mode
    app.run(debug=True)
