print("Welcome to the rollercoaster!")

#Confirm your height
height = int(input("What is your height in cm? "))
bill = 0

#Verify your age
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    else:
        bill = 12
        print("Adult pay $12.")

#Ask if you want a photo
photo = input("Do you like buy a photo? y for YES and n for NO ")
if photo == "y":
    bill += 3
    print("Your bill is:" , bill)
elif photo == "n":
   print("Your bill is: " , bill)
else:
    print("Sorry you have to grow before for you can ride.")
