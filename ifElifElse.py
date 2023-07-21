#student wants to check his qualification status in a exam

num = int(input("Enter your marks "))

#qualify means he has scored above 90
#level 1 means you scored above 75 and level 2 means you scored above 90

if num > 90:
    print("You have qualified both levels!")
elif num > 75:
    print("you have qualified only level 1!")
else:
    print("You have not qualified any levels!")

