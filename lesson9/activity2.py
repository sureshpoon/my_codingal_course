print ("Select your ride: ")
print ("1) bike")
print ("2) car")
choice = int (input("enter your choice of ride : "))
if choice == 1:
    print("What type of bike would you prefer?")
    print("1) motor bike ")
    print ("2) scooter")
    bike = int (input("Enter your choice: "))
    if bike == 1 :
        print("You have selected a motor bike")
    else :
        print ("You have selected a scooter")

elif choice == 2:
    print ("What type of car would you prefer? ")
    print ("1) SUV")
    print ("2) sports car")
    car = int (input("Enter your choice : "))
    if car ==1 :
        print ("You have selected a SUV")
    else :
        print ("You have selected a sports car")

else :
    print ("Wrong input")
  