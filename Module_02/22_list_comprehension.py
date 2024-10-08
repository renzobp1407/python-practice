# This file is automatically @generated by Poetry 1.5.3 and should 
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

# simplificacion de lo de arriba 
doubled_numbers2 = [number * 2 for number in numbers]

#Usando rango
doubled_numbers3 = [number * 2 for number in range(5)]
print(doubled_numbers3)

#underscore para omitir la variable
doubled_numbers3 = [number * 2 for _ in range(5)]

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)


# aplicar nuvas reglas
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie, Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")

# Title casing = first letter on mayus like "Rolf"
# Lower case = lower case all the string

# can be used to a tuple o list




