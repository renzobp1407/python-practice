car = {
  "make": "Ford",
  "model": "Fiesta", 
  "mileage": 23000, 
  "fuel_consumed": 460
}

mpg = car["mileage"] / car["fuel_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon.")

# This is with function:
def calculate_mpg():
    car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg()


#WIth parameters and 1 list

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}


def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg(car)

# now with a lot of values and a for

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)