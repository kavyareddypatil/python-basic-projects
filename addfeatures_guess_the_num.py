guessing_num=20

chances=5
for i in range(chances):
    try:
        user=int(input("enter a number:"))
    except ValueError:
        print("Invalid number!Please enter a valid number")
        continue
    if user==guessing_num:
        print("congratulations! You guess the correct num")
        print("You guess the correct num in  :",i+1,"chance")
        break
    elif user<guessing_num:
        print("It's too low")
    else:
        print("It's too high")
    print("Chances left :",chances-i-1)
else:
    print("better luck next time")
    print("your chances are completed...") 
    print("The guessing number is:",guessing_num)