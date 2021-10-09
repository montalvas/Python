from datetime import datetime


class Person():
    """Model of class of a person
    
    Args:
        current_year (int): receive the current year
    
    Methods:
        __init__: start class attributes
        eat: The person will eat
        stop_eating: The person will stop eating
        talk: The person will talk
        stop_talking: The person will stop talking
        get_year_birth: Calculates the year of birth
    """
    
    current_year = datetime.today().year
    
    def __init__(self, name, age, eating=False, talking=False) -> None:
        """Start class attributes

        Args:
            name (str): person's name
            age (int): person's age
            eating (bool, optional): the person is eating. Defaults to False.
            talking (bool, optional): the person is talking. Defaults to False.
        """
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking
    
    def eat(self, food):
        """The person will eat"""
        if self.eating:
            print(f"{self.name} is already eating.")
            return

        if self.talking:
            print(f"{self.name} don't eat while talking.")
            return
            
        print(f"{self.name} is eating {food}.")
        self.eating = True
    
    def stop_eating(self):
        """The person will stop eating"""
        if not self.eating:
            print(f"{self.name} is not eating.")
            return
        
        print(f"{self.name} stopped eating.")
        self.eating = False
    
    def talk(self, subject):
        """The person will talk"""
        if self.eating:
            print(f"{self.name} don't talk while eating.")
            return
        
        if self.talking:
            print(f"{self.name} is already talking.")
            return

        print(f"{self.name} is talking about {subject}.")
        self.talking = True
    
    def stop_talking(self):
        """The person will stop talking"""
        if not self.talking:
            print(f"{self.name} is not talking.")
            return
        
        print(f"{self.name} stopped talking.")
        self.talking = False
    
    def get_year_birth(self):
        """Calculates the year of birth

        Returns:
            int: Year of birth
        """
        birth = self.current_year - self.age
        return birth