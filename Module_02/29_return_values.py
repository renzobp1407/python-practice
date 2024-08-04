  cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
  ]

  def calculate_mpg(car):

    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg #Mpg variable only exist in this function context

  def car_name(car):
      name = f"{car['make']} {car['model']}"
      return name


  def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")

  # 3 functions in total with returning value

  # The retunr function ends the function, so the next line of code will not be executed

  # 2 lines after a function for better legibility

  for car in cars:
      print_car_info(car)

  #The function can return multiple values

  def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


  print(divide(10, 2))  # 5
  print(divide(6, 0))  # You tried to divide by zero!