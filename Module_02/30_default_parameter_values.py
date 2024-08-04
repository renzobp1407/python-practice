def add(x, y=3):  # x=2, y is not OK
  total = x + y
  print(total)


# if you pass a second value, it will use by default Y=3
add(5)
add(x=5, y=2) #Name argument is called

add(2, 6)
add(x=3) 


# add(y=2)  # ERROR! need the second argument beacuse X dosen't have a default value
# add(x=2, 5)  # ERROR! all subsequent arguments must be keyword arguments or will fail 

print(1, 2, 3, 4, 5, sep=" - ")  # default is " "

#Sep is a default build-in function for separating the values of a print function

default_y = 3


def add(x, y=default_y): #it takes the deafult value at the time, causing confusion
  sum = x + y
  print(sum)


add(2)  # 5

default_y = 4 #highly discourages to do this
print(default_y)  # 4

add(2)  # 5