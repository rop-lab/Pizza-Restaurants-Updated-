from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzeria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/')
def index():
    return "Welcome to the Restaurants Application!"

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.serialize() for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Assuming there is a relationship defined between Restaurant and Pizza models
        pizzas = [pizza.serialize() for pizza in restaurant.pizzas]
        serialized_restaurant = restaurant.serialize()
        serialized_restaurant['pizzas'] = pizzas
        return jsonify(serialized_restaurant)
    else:
        return jsonify({"error": "Restaurant not found"}), 404


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        try:
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        except IntegrityError:
            return jsonify({"error": "IntegrityError: Cannot delete restaurant with associated pizzas"}), 400
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.serialize() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not all([price, pizza_id, restaurant_id]):
        return jsonify({"errors": ["Validation errors"]}), 400

    if not RestaurantPizza.validate_price(price):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({"errors": ["Pizza not found"]}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"errors": ["Restaurant not found"]}), 400

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify(pizza.serialize()), 201

if __name__ == '__main__':
    app.run(debug=True)
