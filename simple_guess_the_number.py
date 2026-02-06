guessing_num=15
for i in range(5):
    user=int(input("enter a number:"))
    if user==guessing_num:
        print("Congratulations! you guess the correct number")
        break
    elif user<guessing_num:
        print("It's too low")
    elif user>guessing_num:
        print("It's too high")
    
else:
    print("Better luck next time,your chances completed")