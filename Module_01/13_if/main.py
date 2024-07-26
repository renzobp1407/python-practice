friend = "Rolf"
user_name = input("Enter your name: ")

if True:
    print("Hello, Friend!")

#If has 4 spaces to the next one space
if user_name == friend:
    print("Hello, Friend! 2")

#This is outside of the if
print("This runs anyway")

if user_name != friend:
  print("Hello, Stranger")

# Simplified version:
if user_name == friend:
    print("Hello, Friend! 2")
else:
    print("Hello, stranger! 2")

#True
print(bool(5)) 
#False
print(bool(0)) 

#background bool
if 5:
    print("Runs")

#when a Scenary is empty, it will return False
#When a Scenary is not empty, it will return True
name1 = input("enter your name: ")
if name1:
   print("We know your name")

#Run across a list or tuple using "in"
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

if user_name in friends:
    print("hello friend of mine")

if user_name in family:
    print("hello, family")
else:
    print("in don'tknow you")

#Using elif
if user_name in friends:
    print("hello friend of mine")
elif user_name in family:
    print("hello, family")
else:
    print("in don'tknow you")
