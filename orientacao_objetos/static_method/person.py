from random import randint


class Person():
    """Model of class of a person
    
    Methods:
        __init__: start class attributes
    """
    
    def __init__(self, name, age) -> None:
        """Start class attributes

        Args:
            name (str): person's name
            age (int): person's age
        """
        self.name = name
        self.age = age
    
    @staticmethod
    def generate_id():
        id = randint(10000, 99999)
        return id
    