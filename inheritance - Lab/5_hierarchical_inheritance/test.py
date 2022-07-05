# In a folder called project create three files: animal.py, dog.py, and cat.py.
# In each file, create its corresponding class - Animal, Dog, and Cat:
# •	Animal with a single method eat() that returns: "eating..."
# •	Dog with a single method bark() that returns: "barking..."
# •	Cat with a single method meow() that returns: "meowing..."
# Both Dog and Cat should inherit from Animal.


from project.cat import Cat
from project.dog import Dog

d = Dog()
c = Cat()

print(d.eat())
print(d.bark())
print(c.eat())
print(c.meow())
