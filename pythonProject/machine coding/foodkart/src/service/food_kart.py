from src.model.user import User
from src.model.restaurant import Restaurant


class FoodKart:
    def __init__(self):
        self.users = {}
        self.restaurants = {}

    def register_user(self, user_details):
        name, gender, phone, pincode = user_details
        user = User(name, gender, phone, pincode)
        self.users[phone] = user

    def login(self, user_id):
        for phone, user in self.users.items():
            if phone == user_id:
                user.login()
            else:
                user.logout()

    def register_restaurant(self, resturant_name, pincodes, food_name, price, initial_quantity):
        restaurant = Restaurant(resturant_name, pincodes, food_name, price, initial_quantity)
        self.restaurants[resturant_name] = restaurant

    def update_quantity(self,name,quantity):
        self.restaurants[name].update_quantity(quantity)

    def create_review(self,name,rating, comment=None):
        self.restaurants[name].rate_restaurant(rating)
        self.restaurants[name].add_comment(comment)

    def show_restaurants(self, key):
        sorted_restaurants=sorted(self.restaurants.values(),key=lambda x:getattr(x,key), reverse=True)
        for restaurant in sorted_restaurants:
            print(f"{restaurant.name},{restaurant.food},{restaurant.rating}")

    def place_order(self,phone,name,quantity):
        if name in self.restaurants:
            rest=self.restaurants[name]
            if quantity<=rest.food.quantity:
                self.restaurants[name].food.quantity-=quantity
                order_details = (rest.name, rest.food.name, quantity)
                self.users[phone].orders.append(order_details)
                print("order placed successfully")
            else:
                print("We have lesser quantity")
        else:
            print("restaurant is not listed in our app.")

    def update_location(self,name, pincode):
        self.restaurants[name].update_locations(pincode)



