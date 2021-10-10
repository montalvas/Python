from product import Product

p1 = Product('shirt', 50)
p2 = Product('shirt', 100)

print(f"The product {p1.name} costs $ {p1.price}.")
p1.discount(10)
print(f"with the discount, costs $ {p1.price}")

p1.name = 'Gamer Keyboard'
p1.price = 200

print(f"\nThe product {p1.name} costs $ {p1.price}.")
p1.discount(10)
print(f"with the discount, costs $ {p1.price}")