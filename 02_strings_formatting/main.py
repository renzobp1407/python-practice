#Strings
my_string = "Hello, world! with double quotes"
my_string2 = 'hello world! on single quotes'

#You can use the printing without the variable
print("Hello, world!")

print(my_string)
print(my_string2)

#not recomended to use '\'
#this symbol '\' is called Escaping to remove the meaning of the char
string_without_quote_marks = "hello \"it's\" me"
print(string_without_quote_marks)

another_with_quotes = 'he said "you are amazing!" yesterday.'
print(another_with_quotes)

#Multiline Strings
multiline = """
hola como estas

my name is jose. Welcome to my program
"""
print(multiline)

hello = multiline + " , así?"
print(hello)

#how to Write a large comment
"""
this is a commentary section

this talks about strings
"""
name = "jose"
greetings1 = "hello, " + name
print(greetings1)

#Printing age with a string on a print
numero = 34

#incorrect: print("You are " + age)
#Correct:
num_to_string = str(numero)
print("tu edad es " + num_to_string)

#------------------------------------------

#Printf for python 3.6, is for print and format any variable
print(f"you are {numero}")

#curly braces to adapt any variable throught the print
name3 = "jose"
greetings = f"how are you, {name3}?"
print(greetings)

#You cannot rewrite a variable and print it, it will print the last value
name3 = "July"
print(greetings)

#it can be without a variable and pass throught the print
#With the function .format(variable)
#the curly brases is actually a template for a parameter throught the variable
jose_greetings = "how are you, {}"
final_greetings = jose_greetings.format(name)
print(final_greetings)

#you can rewrite the variable inside the curly braces with the previos variable
name2 = "bob"
alternative_greetings = jose_greetings.format(name2)
print(alternative_greetings)

#replacing the variable inside the curly braces with the new variable declared
jose_greetings2 = "how are you, {name2}"
alternative_greetings2 = jose_greetings2.format(name2="Maria")
print(alternative_greetings2)

#you can add a format variable inside the print
name4 = "mario"
final_greeting3 = "how are you, {}?"
print(final_greeting3.format(name4))

#Python knows about the paramter and variable when you pass it
#first name = parameter
#Second name = variable
# alternative_greetings2 = jose_greetings2.format(name=name)

#You can have 2 or more parametes on the print of a template string
description = "{} is {} years old."
print(description.format("gary", 50))

#Also you can declare a format o value inside the parameter
description = "{} is {age} years old."
print(description.format("Bob", age=30))
