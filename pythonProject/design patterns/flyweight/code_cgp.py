"""
Type: Structural Pattern
The Flyweight pattern optimizes memory usage by sharing common, intrinsic portions of objects across multiple objects.
It reduces memory consumption when a large number of similar objects are required.
"""

# Word processor

# Flyweight class
class Character:
    def __init__(self, char, font, size):
        self.char = char
        self.font = font
        self.size = size

    def render(self):
        print(f"Character: {self.char}, Font: {self.font}, Size: {self.size}")

#flyweight factory

class CharacterFactory:
    char_cache={}

    @classmethod
    def get_char(cls,char, font, size):
        if (char, font, size) not in cls.char_cache:
            cls.char_cache[(char, font, size)]=Character(char, font, size)
        return cls.char_cache[(char, font, size)]

#client code
characters = []
char_factory = CharacterFactory()

text = "Hello, World!"

for char in text:
    character = char_factory.get_char(char, "Arial", 12)
    characters.append(character)

for character in characters:
    character.render()
