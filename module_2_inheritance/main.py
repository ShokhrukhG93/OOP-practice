from models.demonstration import A, B, C, D
from models.animal import Animal, Cat, Dog, Shorthair

# Demonstration
a = A('Class A', 'SuperClass')
print(a.att1, a.att2)
a.act()

print('-----------------------------------')

b = B('Class B', 'SubClass', 'Bat')
print(b.att1, b.att2, b.att3)
b.act()

print('-----------------------------------')

c = C('Class C', 'SubClass', 'Cat')
print(c.att1, c.att2, c.att4)
c.act()

print('-----------------------------------')

try:
    print(b.att4)
except AttributeError:
    print("AttributeError: 'B' object has no attribute 'att4'")

print('-----------------------------------')

try:
    print(c.att3)
except AttributeError:
    print("AttributeError: 'C' object has no attribute 'att3'")

print('-----------------------------------')

d = D('Class D', 'SubSubClass', 'Camel', 'Desert')
print(d.att1, d.att2, d.att4, d.att5)
d.act()

print('-----------------------------------')

# Animal class
print('-----------------------------------')
animal1 = Animal('Abby', 'Animal')
animal1.make_sound()

print('-----------------------------------')

dog1 = Dog('Buddy', 'Golden Retriever')
dog1.make_sound()
print(dog1.breed, dog1.name, dog1.species)

print('-----------------------------------')

cat1 = Cat('Cathy', 'Shorthair')
cat1.make_sound()
print(cat1.breed, cat1.name, cat1.species)

print('-----------------------------------')

cat2 = Shorthair('Conner', '10')
cat2.make_sound()
print(cat2.breed, cat2.name, cat2.species, cat2.age)