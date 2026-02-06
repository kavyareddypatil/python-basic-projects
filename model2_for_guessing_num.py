import random
guessing_num=random.randint(1,50)
while True:
    try:
        guess=int(input("guess the number b/w 1 t0 50 : "))
        if guess < guessing_num:
            print("It's too low")
        elif guess > guessing_num:
            print("It's too high")
        else:
            print("congratulations! you guessed the number")
            break
    except ValueError:
        print("enter a valid number..")