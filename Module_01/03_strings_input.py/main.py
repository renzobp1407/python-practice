#----------------------------------------
#User Input in python
#The input() function pass a character to a String any alfanumeric character
name = "jose"
your_name = input("Enter your name: ")
print(f"Hello {your_name}. My name is {name}")

#this is an logic error on the code, because is going to print the age twelve times
#they get concatenated
#  242424242424242424242424
age = input("Enter your age: ") #this is equal to age = "3"
print(f"you have lived for {age * 12} months.")

#turn to a integer
age_num = int(age)
print(f"you have lived for {age_num * 12} months.")

#Python has a priority inside a parenthesis, it will start from the inside to the outside
#this is called Nesting

#Recommend to separate the operations inside curly braces to give a 
# meaining to the variable and keep it readable
age2 = int(input("enter you age: "))
months = age2 *12
print(f"you have lived for {months} months.")

