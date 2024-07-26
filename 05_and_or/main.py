#and & or
age = 25

result = age > 18 and age < 65 #True and True
result2 = age < 18 and age > 65 
print(result)
print(result2)

# if the first vaule is false, automatically return the second value

#using OR, the first value is true, return the first value
#The OR operator returns the first operand that is not a false value. If both operands are false, it returns the second operand.

result3 = age < 18 or age < 65 #True and True
print(result3)

result4 = age < 18 or age > 65 
print(result4)

# When we call bool, it evaluates if not false or not empty, thats ir why on a value, return True
#Otherwise will be false

bool(0) # False, Zero
bool(13) #true

bool("") # False, empty String
bool("Hello") # True

bool([]) # False, empty list
bool([1,3,5]) #True

#Default Falsy value
default_age = 30
age = 0

user_age = age or default_age
print(user_age)

#Empty value

default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting

print(f"Hello, {user_name}!"")

# if printed some name, it will print the name, if not, it will print the default_greeting
#False vs true is true

