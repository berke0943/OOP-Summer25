# 1. Question Print your name on the screen.
print("Berke")

# 2. Question Assign 10 to a variable x, 3.5 to a variable y, and print their sum.
x = 10
y = 3.5
print(x + y)

# 3.Question Get the user's name and print "Hello, +name".
name = input("Enter your name: ")
print("Hello, " + name)

# 4.Question Create a dictionary and print the countries' capital:
country = {
    "name": "Turkey",
    "population": "85 million",
    "continent": "Asia-Europe",
    "capital": "Ankara"
}
print(country["capital"])  # Output: Ankara


# 5.Question Ask the user for their age and print whether they are a child, teenager, adult, or senior.
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")


#6. Question  Create a list with nafruits and print each item on a new line.
fruits = ["apple", "pear", "banana", "strawberry", "orange"]
print(fruits)
for fruit in fruits:
    print(fruit)



#7. Question Create a dictionary
student= {
  "name": "Berke",
  "index_numver": 35274,
  "faculty": "engineering"
}
print(student)

#8. Question Create a class "Car" with attributes name and model. 
# Create one object and print its information.
class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

print(car1.model)
print(car2.name)

#9. Write a while loop that prints numbers from 1 to 10.
for i in range(1, 11):
    print(i)

#10. Create a list aand add new item
fruits = ["apple", "banana", "orange"]
print(fruits[-1]) 

fruits.append("kiwi")  
print(fruits)  

