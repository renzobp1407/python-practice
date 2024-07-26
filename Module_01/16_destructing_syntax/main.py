currencies = 0.8, 1.2
usd, eur = currencies
#usd and eur has been asigned a variables in currencies
#so, this is called destructuring

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

#this is the original form
for  friend in friends:
    print(friend)

#you can add by this form
#name and age asumes the values of the tuple and can print it clean
for  name, age in friends:
    print(name, age)

#can be better
for  name, age in friends:
  name, age = friend
  print(f"{name} is {age} years old.")

