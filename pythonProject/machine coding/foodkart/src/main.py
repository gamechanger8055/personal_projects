from service.food_kart import FoodKart
def main():
    system = FoodKart()

    system.register_user(("Pralove", "M", "phoneNumber-1", "HSR"))
    system.register_user(("Nitesh", "M", "phoneNumber-2", "BTM"))
    system.register_user(("Vatsal", "M", "phoneNumber-3", "BTM"))

    print(system.users)

    system.login("phoneNumber-1")
    system.register_restaurant("Food Court-1", "BTM/HSR", "NI Thali", 100, 5)
    system.register_restaurant("Food Court-2", "BTM", "Burger", 120, 3)

    system.login("phoneNumber-2")
    system.register_restaurant("Food Court-3", "HSR", "SI Thali", 150, 1)

    system.login("phoneNumber-3")
    system.show_restaurants("rating")

    system.place_order("phoneNumber-3","Food Court-1", 2)
    system.place_order("phoneNumber-3","Food Court-1", 1)


    system.place_order("phoneNumber-2","Food Court-2", 7)

    system.create_review("Food Court-2", 3, "Good Food")
    system.create_review("Food Court-1", 5, "Nice Food")

    system.show_restaurants("rating")

    system.login("phoneNumber-1")
    system.update_quantity("Food Court-2", 5)

    print("Updated location:")
    system.update_location("Food Court-2", "BTM/HSR")

    print("Order History for phoneNumber-1:")
    for order in system.users["phoneNumber-3"].orders:
        print(f"Restaurant: {order[0]}, Food: {order[1]}, Quantity: {order[2]}")
main()
