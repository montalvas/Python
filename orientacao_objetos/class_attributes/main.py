class A:
    test = 123


a1 = A()
a2 = A()

print(a1.test)
print(a2.test)

A.test = 321

print(a1.test)
print(a2.test)
