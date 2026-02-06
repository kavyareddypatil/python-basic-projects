# ask user to roll the dice?
# if user enters y
#     generate two random numbers
#     print them
# if user enters n 
#     print thank you message
#     terminate
# else
#   print invalid choice

import random
playing=True
while playing:
    choice=input("Roll the Dice (Y/N): ").upper()
    if choice=="Y" :
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1} , {die2})")
    elif choice=="N":
        print("thanks for playing!")
        break
    else:
        print("Invalid choice!")





