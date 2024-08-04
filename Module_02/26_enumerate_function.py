friends = ["Rolf", "Jen", "Anne"]

counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

for counter, friend in enumerate(friends):
  print(counter)
  print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

#enumera 1 por 1 lo que vaya encontrando

# el print seria así 

"""
0
Rolf
1
Jen
2
Anne
0
Rolf
1
Jen
2
Anne
[(0, 'Rolf'), (1, 'Jen'), (2, 'Anne')]
{0: 'Rolf', 1: 'Jen', 2: 'Anne'}



"""



 # 
#En Python, la función enumerate se utiliza para iterar sobre una #secuencia (como una lista o una tupla) y obtener tanto el índice #del #elemento como el propio elemento en cada iteración. Esto es útil #cuando necesitas acceder al índice y al valor simultáneamente #durante la iteración.
#