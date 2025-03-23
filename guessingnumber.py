#Guessing number game in python

import random
Cnum=random.randrange(1,1000)
Userinput =int(input("Enter Your Number:"))

if Userinput>Cnum:
    print("Computer Number, Cnum")
    print("Your guessing number is too high")

elif Cnum>Userinput:
    print("Computer Number,Cnum")
    print("Your guessing number is too low")

else:
    print("Computer Number,Cnum")
    print("your guessing number is equal")

