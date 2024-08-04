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


for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished successfully