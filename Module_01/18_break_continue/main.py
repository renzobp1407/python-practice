cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

#printing all
for status in cars:
  print(f"This car is {status}")

#with break
# 4 lines to the for and 4 lines to the if
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
    print("Shipping new car to customer!")

#now with continue, it will restart to the beginnig of the loop
#Skipping everything else and going to the next iteration
for status in cars:
  if status == "faulty":
      print("Found faulty car, skipping...")
      continue

  print(f"This car is {status}.")
  print("Shipping new car to customer!")