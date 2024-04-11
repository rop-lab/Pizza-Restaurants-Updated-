# Pizza-Restaurants-Updated-

# Pizza Restaurant API

This Flask API provides endpoints to manage restaurants and pizzas, allowing users to retrieve, create, update, and delete data related to restaurants and their associated pizzas.

## Setup

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask server using `python3 app.py`.
4. Use Postman or any other API testing tool to interact with the endpoints.

## Endpoints

### Get Restaurants
- **URL:** `/restaurants`
- **Method:** `GET`
- **Description:** Retrieves a list of all restaurants.
- **Response:** 
    ```
    [
      {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5th Avenue"
      },
      {
        "id": 2,
        "name": "Pizza Hut",
        "address": "Westgate Mall, Mwanzi Road, Nrb 100"
      }
    ]
    ```

### Get Restaurant by ID
- **URL:** `/restaurants/:id`
- **Method:** `GET`
- **Description:** Retrieves details of a specific restaurant by its ID.
- **Response:** 
    - If restaurant exists:
        ```
        {
          "id": 1,
          "name": "Dominion Pizza",
          "address": "Good Italian, Ngong Road, 5th Avenue",
          "pizzas": [
            {
              "id": 1,
              "name": "Cheese",
              "ingredients": "Dough, Tomato Sauce, Cheese"
            },
            {
              "id": 2,
              "name": "Pepperoni",
              "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
            }
          ]
        }
        ```
    - If restaurant does not exist: 
        ```
        {
          "error": "Restaurant not found"
        }
        ```

### Delete Restaurant by ID
- **URL:** `/restaurants/:id`
- **Method:** `DELETE`
- **Description:** Deletes a restaurant and its associated pizzas by ID.
- **Response:** 
    - If restaurant exists and is deleted successfully: Empty response body.
    - If restaurant does not exist:
        ```
        {
          "error": "Restaurant not found"
        }
        ```

### Get Pizzas
- **URL:** `/pizzas`
- **Method:** `GET`
- **Description:** Retrieves a list of all pizzas.
- **Response:** 
    ```
    [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
    ```

### Create Restaurant Pizza
- **URL:** `/restaurant_pizzas`
- **Method:** `POST`
- **Description:** Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.
- **Request Body:** 
    ```
    {
      "price": 5,
      "pizza_id": 1,
      "restaurant_id": 3
    }
    ```
- **Response:** 
    - If created successfully: Data related to the pizza.
        ```
        {
          "id": 1,
          "name": "Cheese",
          "ingredients": "Dough, Tomato Sauce, Cheese"
        }
        ```
    - If not created successfully:
        ```
        {
          "errors": ["validation errors"]
        }
        ```

## Models

### Restaurant
- Attributes:
    - id (Primary Key)
    - name
    - address
- Validations:
    - Name must be less than 50 characters.
    - Name must be unique.

### Pizza
- Attributes:
    - id (Primary Key)
    - name
    - ingredients

### RestaurantPizza
- Attributes:
    - id (Primary Key)
    - price
    - restaurant_id (Foreign Key)
    - pizza_id (Foreign Key)
- Validations:
    - Price must be between 1 and 30.
