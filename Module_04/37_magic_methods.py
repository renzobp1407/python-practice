class Student:
  def __init__(self, name):
    self.name = name  

movies = ['Matrix', 'Finding Nemo'] 
print(movies.__class__)
# Almost everyhtin in python is a object
print(len(movies))

class Garage:
    def __init__(self):
        self,cars = []

    def __len__(self):
       return len(self.cars)

    def __getitem__(self):
       return self.cars[i]    

    def __repr__(self):
       return f'<Garage {self.cars}>'  
    
    def __str__(self):
       return f'Garage with {len(self)} cars. '      

ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')        
print(ford.cars)

print(len(ford)) # this will cause and error
# To prevent this error, we must create a dunder methor for len on the class Garage()

print(ford[0]) # this will cause and error
# To prevent this error, we must create a dunder methor for len on the class Garage()
# we can use Garage.__getitem__(ford, 0)

# yoy can use a for only when you have len and get item, because you converted that class to 

for car in ford:
    print(car)