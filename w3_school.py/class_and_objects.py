# Creating class
class MyClass:
  x = 5
#creating object
p1 = MyClass()
print(p1.x)

# The __init__() Function is automatically running constructor

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Berke", 20)

print(p1.name)
print(p1.age)

#The __str__() Function 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Berke", 20)

print(p1)
#__init__() Runs when the object is created, setting the initial data
#__str__() Returns a proper string representation of the object when called with functions like print()

#Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Berke", 20)
p1.myfunc()
