# Improved Number Guess Game with:
# 1> Adding int() function to convert input to int 
# 2> Adding comments to the code

target = 10  # The number to guess
attempts = 0  # Counting attempts

while attempts < 3:  # Allow up to 3 guesses
    user_input = input("Please input your guess: ")
    guess = int(user_input)  # Convert input to integer
    
    if guess > target:
        print("Your guess is too large.")
    elif guess < target:
        print("Your guess is too small.")
    else:
        print("Congratulations! You've guessed it right.")
        break  # Exit the loop if guessed correctly
    
    attempts += 1  # Increment the attempt counter

if attempts == 3:
    print("3 attempts finished, you have no more chances.")
