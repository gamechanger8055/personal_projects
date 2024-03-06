"""
Singleton pattern is a creational pattern that ensures that class has only one instance and provides a global
point of access to it.
This pattern is useful when exactly one object is needed to co-ordinate actions across systems such as
database configuration, configuration manager or logging service.
"""

class Singleton:
    _instance=None

    @classmethod
    def __new__(cls):
        if not cls._instance:
            cls._instance=super(Singleton, cls).__new__(cls)
        return cls._instance

    def showMessage(self):
        print("Hello I am singleton instance.")

if __name__ == "__main__":
    # Get the Singleton instance
    singleton_instance1 = Singleton()
    singleton_instance2 = Singleton()

    # Both instances will be the same
    print("Are both instances the same?", singleton_instance1 is singleton_instance2)

    # Call a method on the Singleton instance
    singleton_instance1.showMessage()
