#Dictionary

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25

print(friend_ages)

#Differences between sets and dictionaries is in dictionarie do keep the order
#you cannot have duplicates
friends = (
   {"name": "Rolf Smith", "age": 24},
   {"name": "Adam Wool", "age": 30},
   {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

#Dict turn data into a dictionary

friends2 = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages2 = dict(friends2)
print(friend_ages2)




