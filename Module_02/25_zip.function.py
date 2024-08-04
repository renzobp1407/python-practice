
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

dict(zip(friends, time_since_seen))

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)

#Zip combinas 1 o mas listas en una sola

# Si agregas elementos demas el zip no lo va a leer


# Remember how we can turn a list of lists or tuples into a dictionary?
# `zip(friends, time_since_seen)` returns something like [("Rolf", 3), ("Bob", 7)...]
# We then use `dict()` on that to get a dictionary.

friends_last_seen = dict(zip(friends, time_since_seen))
print(friends_last_seen)
