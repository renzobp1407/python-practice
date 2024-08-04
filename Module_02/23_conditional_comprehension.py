ages = [22, 35, 27, 21, 20]
odds1 = [age for age in ages]

odds = [age for age in ages if age % 2 == 1]

# en una lista hay que saber diferenciar lo que se está haciendo
# en este caso la primera variable "ages" va a asignarsele un valor de lo que salga a la derech
# y en este caso, se hace un for y luego un if

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guest_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guest_lower))

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
  
]
print(present_friends)
# Si los ponemos como sets, pirden el orden
# Dentro de un for evitar poner tantos .functions porque así no se entiende casi

#es mejor ponerlo de esta forma:

present_friends = [
    name.title()
    for name in guests 
    if name.lower() in friends_lower

]



