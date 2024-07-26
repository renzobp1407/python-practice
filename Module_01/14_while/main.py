is_learning = True

while is_learning:
    print("you are learning")
    is_learning = False


is_learning = True
while is_learning:
  print("you are learning!!!")
  is_learning = input("are you learning? ")

#Testing
while is_learning:
  print("you are learning!!!")
  user_input = input("are you learning? ")
  is_learning == user_input == "yes"


user_input2 = input("Do you wish to run the program? (yes/no): ")

while user_input2 == "yes":
    print("We're running!")
    user_input2 = input("Do you wish to run the program? (yes/no): ")

print("we stopped running.")