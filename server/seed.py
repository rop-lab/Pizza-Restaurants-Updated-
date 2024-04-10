from app import app, db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        # Create Restaurants
        dominion_pizza = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        pizza_hut = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

        db.session.add(dominion_pizza)
        db.session.add(pizza_hut)
        db.session.commit()

        # Create Pizzas
        cheese_pizza = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pepperoni_pizza = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

        db.session.add(cheese_pizza)
        db.session.add(pepperoni_pizza)
        db.session.commit()

        # Create Restaurant Pizzas
        rp_dominion_cheese = RestaurantPizza(price=5, pizza_id=cheese_pizza.id, restaurant_id=dominion_pizza.id)
        rp_dominion_pepperoni = RestaurantPizza(price=6, pizza_id=pepperoni_pizza.id, restaurant_id=dominion_pizza.id)
        rp_hut_cheese = RestaurantPizza(price=7, pizza_id=cheese_pizza.id, restaurant_id=pizza_hut.id)

        db.session.add(rp_dominion_cheese)
        db.session.add(rp_dominion_pepperoni)
        db.session.add(rp_hut_cheese)
        db.session.commit()

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    seed_data()
