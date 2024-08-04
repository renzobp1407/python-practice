friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([n.lower() for n in friends])
guest_lower = set([n.lower() for n in guests])

present_friends = {name.title() for name in friends_lower.intersection(guest_lower)}

# lo bueno es que remueve duplicados de esta forma

print(friends_lower.intersection(guest_lower))


# -----------------------------------------
friends = ["Rolf", "ruth", "charlie", "Jen"]
time_sine_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_sine_seen[i]
    for i in range(len(friends))
    if time_sine_seen[i] > 5

}

print(long_timers)

# esto seria un diccionario que anida los valores de las listas

