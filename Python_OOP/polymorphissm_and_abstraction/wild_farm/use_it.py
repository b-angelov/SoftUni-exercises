from project.animals.mammals import Dog, Mouse, Cat
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit, Seed

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
print(owl.feed(meat))
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
####################################################
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
seed = Seed(5)

dog = Cat("Harry", 10, 10)
print(dog.food)
print(dog)
print(dog.make_sound())
print(dog.feed(veg))
print(dog.feed(fruit))
print(dog.feed(meat))
print(dog.feed(seed))
print(dog)

