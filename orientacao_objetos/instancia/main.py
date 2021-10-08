from person import Person

# instance
p1 = Person('Lucas', 27)

# methods
p1.eat('Tapioca recheada')
p1.eat('Batata doce')
p1.talk('Programacao')
p1.stop_eating()
p1.talk('Programacao')
p1.talk('Desenvolvimento web')
p1.eat('pao')
p1.stop_talking()

# attributes in the class
print(f"{p1.name} was born in {p1.get_year_birth}.")
