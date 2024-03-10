# Number Guess Game

target = 10  
attempts = 0  

while attempts < 3:  # Allow up to 3 guesses
    user_input = input("Please input your guess: ")
    
    if user_input > target:
        print("Your guess is too large.")
    elif user_input < target:
        print("Your guess is too small.")
    else:
        print("Congratulations! You've guessed it right.")
        break  
    attempts += 1  
if attempts == 3:
    print("3 attempts finished, you have no more chances.")
