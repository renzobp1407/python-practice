#advance Operations

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_nor_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_nor_science)
print(science_but_not_art)

#Simetric Difference, wich member that are not in both sets

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

#Intersection, wich member that are in both sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friends = art_friends.union(science_friends)
print(all_friends)
