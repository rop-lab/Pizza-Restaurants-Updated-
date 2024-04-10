from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask import jsonify

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurant_pizzas.restaurant',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100))
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            # Add more attributes as needed
        }

    def __repr__(self):
        return f'<Restaurant {self.id},  {self.name}, {self.address}>'

    # Define the relationship to associate pizzas with restaurants
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref='restaurants')

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            # Add more attributes as needed
        }

    def __repr__(self):
        return f'<Pizza {self.id}, {self.name}, {self.ingredients}>'


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f'<Restaurant_pizza {self.id}, {self.price}, {self.restaurant_id}>'
