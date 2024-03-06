"""
Type: Behavoural Pattern
The Null Object pattern provides a default, do-nothing implementation of an interface for handling the absence of a real object.
 It helps avoid null reference errors in client code.
"""

class Logger:
    def log(self,message):
        pass

class ConcreteLogger(Logger):
    def log(self, message):
        print(f"Console Logger: {message}")

# Null logger
class NullLogger(Logger):
    def log(self, message):
        pass

# Client code
def do_something_with_logging(logger):
    logger.log("Doing something...")

console_logger = ConcreteLogger()
do_something_with_logging(console_logger)

# Disable logging
null_logger = NullLogger()
do_something_with_logging(null_logger)