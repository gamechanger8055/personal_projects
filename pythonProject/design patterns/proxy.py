"""
Proxy pattern is a structural pattern that provides a placeholder for another object to control access over it.
It acts as an mediator between server and client
Eg. logging, monitoring, caching
"""

#eg- caching images---------------

# Subject interface
class Image:
    def display(self):
        pass

# RealImage represents the actual image object
class RealImage(Image):
    def __init__(self,filename):
        self.file=filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from {self.file}")

    def display(self):
        print(f"Displaying image: {self.file}")

class ProxyImage(Image):
    def __init__(self,filename):
        self.file = filename
        self.real_image=None

    def display(self):
        if not self.real_image:
            self.real_image=RealImage(self.file)
        self.real_image.display()

image1 = ProxyImage("image1.jpg")
image2 = ProxyImage("image2.jpg")

image1.display()
image2.display()

image1.display()

