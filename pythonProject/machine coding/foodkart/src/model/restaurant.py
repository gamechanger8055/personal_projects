from src.model.food_item import FoodItem
from src.model.comment import Comment
class Restaurant:
    def __init__(self, name, pincodes, food, quantity, price):
        self.name=name
        self.pincodes=pincodes.split('/')
        self.food=FoodItem(food,quantity,price)
        self.rating=0
        self.rating_count=0
        self.comment={}

    def update_quantity(self, quantity):
        self.food.quantity+=quantity

    def rate_restaurant(self,rating):
        self.rating=(self.rating*self.rating_count+rating)/(self.rating_count+1)
        self.rating_count+=1

    def add_comment(self,comments):
        comment=Comment()
        comment.id=1
        comment.comment=comments
        self.comment[comment.id]=comments

    def update_locations(self, pincodes):
        self.pincodes.extend(pincodes.split('/'))
