form flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurant_pizzas.restaurant')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(512))
    restaurant_pizzas = db.Relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.id},  {self.name}, {self.address}>'
    
class Pizza(db.Module, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurant_pizzas.pizza')
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String, nullable= False)
    restaurant_pizzas = db.Relationship('RestaurantPizza', backref='pizza')
    def __repr__ (self):
        return f'<Pizza {self.id}, {self.name}, {self.ingredients}>'
    

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    Restaurant_id =db.Column(db.Integer, db.ForeignKey("restaurants.id"))

    
    def __repr__ (self):
        return f'<Restaurant_pizza{self.id}, {self.price}, {self.Restaurant_id}>'
    
    
