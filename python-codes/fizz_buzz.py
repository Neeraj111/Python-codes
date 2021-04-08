def fizz_buzz(number: int):
    if number%3 == 0 and number%5 == 0:
        return "fizzbuz" 
    elif number%3 == 0 and number%5 != 0:
        return "fizz"
    elif number%5 == 0 and number%3 != 0:  
        return "buzz"        
    else:
        return number    


input("Play FizzBuzz.   Press ENTER to start")
print()

next_entry = 0
while next_entry < 10:
    next_entry = next_entry + 1
    print(fizz_buzz(next_entry))
    next_entry = next_entry + 1
    correct_entry = str(fizz_buzz(next_entry))
    player_entry = str(input("Your GO :"))

    if player_entry != correct_entry:
        print("Wrong answer. {} is the correct answer".format(correct_entry))
        break
else:
    print("game over")






