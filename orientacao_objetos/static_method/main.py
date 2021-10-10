from person import Person


'''static é uma função comum que pode ser acessada pela classe ou instancia'''
p1 = Person('Jones', 150)
print(f"The {p1.name}'s id is {p1.generate_id()}")