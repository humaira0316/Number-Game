import random
top_range=input("Enter the limit : ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("Please type  a number greater than 0")
    else:
        random_number =random.randint(0,top_range)
else:
    print("please enter a digit")
guesses=0
while True:
    guesses+=1
    user_guess=input("Guess the number")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time")
        continue
    if user_guess == random_number:
        print("You got it!!")
        break
    else:
        if user_guess > random_number:
            print("Oops!you were above the number")
        else:
            print("Oops! you were below the number")

print("You've got it in",guesses,"guesses")






