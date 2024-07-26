friend1 = "Rolf"
friend2 = "bob"
friend3 = "Anne"

#declaring list
friends = ["Rolf", "bob", "Anne"]

#Printing a list
print(friends[0])

#Not recomended to use this way
friends = ["Rolf", 2, "Anne"] #Wrong

#Lenght of a list
print(len(friends))

#List inside with 2 elements

friends = [["Rolf", 24], ["bob", 24], ["Anne", 27]]
print(friends[0][0])
print(friends[1][1])

#large List
friends_list = [
  ["Rolf",24],
  ["bob", 30],
  ["Anne", 27],
  ["Charlie", 37],
  ["Jen", 25],
  ["Adam", 29],
]

# Using Apped to add a new value on the list
friends.append("Jen")
print(friends)

friends.remove("Jen")
print(friends)

#Removing a elemetn from a list
friends.remove(["Anne", 27])

#this is not valid: 
friends.remove(["Anne"])
