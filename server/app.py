from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    response =(
        '<h1>Welcome to my pizza restaurant!</h1>',
        200
    )
    return jsonify(response)


@app.route('/restaurant/<int:id>')
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if restaurant:
        response_body = f'<p>{restaurant.name} {restaurant.address}</p>'
        response_status = 200
    else:
        response_body = f'<p>Restaurant {id} not found</p>'
        response_status = 404

    # response = make_response(response_body, response_status)
    return jsonify(response_body, response_status)


@app.route('/pizza/<int:id>')
def pizza_by_id(id):
    pizza = Pizza.query.filter(Pizza.id == id).first()

    if pizza:
        response_body = f'<p>{pizza.name} {pizza.ingredients}</p>'
        response_status = 200
    else:
        response_body = f'<p>Pizza {id} not found</p>'
        response_status = 404

    # response = make_response(response_body, response_status)
    return jsonify(response_body, response_status)


@app.route('/species/<string:species>')
def pet_by_species(species):
    pets = Pet.query.filter_by(species=species).all()

    size = len(pets)  # all() returns a list so we can get length
    response_body = f'<h2>There are {size} {species}s</h2>'
    for pet in pets:
        response_body += f'<p>{pet.name}</p>'
    response = make_response(response_body, 200)
    return response




if __name__ == '__main__':
    app.run(port=5555, debug=True)