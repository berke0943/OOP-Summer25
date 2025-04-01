#Import Statements
import os  # correct
import sys  # correct

import os, sys #wrong 
#print
print("Hello World!") #correct example 
print  ( "hello world" ) #wrong example

# Whitespace Usage
x = 10 #correct
y = 5

# Wrong
x=10  
y =5  

#naming 
my_name="Berke" #correct 
print(my_name)

ssnnnfjvf= "Berke" #wrong
print(ssnnnfjvf)

my_age = 10  # correct 

MyAge=10 #wrong

print(my_age)
print(MyAge)

#indentation 
if True:
    print("Hello") #correct

"""
if True:
print("Hello")" #wrong
"""
# Dictionary Usage
person = {
    "name": "Alice",
    "age": 25,
}# Correct


person = {"name":"Alice","age":25}  #wrong

#function 
def my_function():  #correct
    print("Hello")

def MyFunction(): #wrong
    print("HEllo")
#Loop
for i in range(5):
    print(i)
    print("Loop continues")#correct


for i in range(5):
    print(i)
    
    print("Loop continues")#wrong
