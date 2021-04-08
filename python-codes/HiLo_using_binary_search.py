low = 1
high = 1000
print("please think of  a number between {} and {}".format(low,high))

guesses=1
while True:
    guess = low+(high-low)//2
    user_guess = input("My guess is {}. Should i guess higher or lower? enter h or l or c if my guess is correct ".format(guess)).casefold()
    
    if user_guess == 'h':
        low = guess+1
    elif user_guess == 'l':
        high = guess-1                
    elif user_guess == 'c':
        print("You got in {} guesses".format(guesses))
        break
    else:
        print("try again")

    guesses=guesses+1    
