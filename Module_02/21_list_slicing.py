friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

#estos son los que se encuentran entre 2 y 4
print(friends[2:4])
# obtener los elementos de la lista excepto el prmero
print(friends[1:])

print(friends[2:])
# se salta la posicio 4
print(friends[:4])

#trayendo una nueva lista si está vacio
print(friends[:])

print(friends[-3:])

#si no se pone nada al principio, entiende que es desde el principio
print(friends[:-2])

#va desde Anna hasta el final Jen, pero como Jen no se incluye por
# ser exclusivo en el extremo final
print(friends[-3:-1])
