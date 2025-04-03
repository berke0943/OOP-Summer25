#Python Format


#This format is wrong We need to use F-String Format
"""
age = 20
txt = "My name is Berke, I am " + age 
print(txt)
"""
#F-String Format
age = 20
txt = f"My name is Berke, I am {age} years old" 
print(txt)

#Also we can show int numbers with 2 decimals
price = 79
txt = f"The price is {price:.2f} dollars" #price:.2f we can change the number how many digits we want 
print(txt)

#We can do math in curly braces
txt = f"27 multiplied by 32 equals {27 * 32} "
print(txt)

#Also we can write like this
print(f"27 multiplied by 32 equals {27 * 32} ")
