# Guess the number game

# Number of guesses : 9

# Print no of guesses left

# If no guesses left, game over

# Or else if guess correctly, then print you won along with no of guesses used

secret_number = 18
total_guesses = 9
no_of_guesses_left = 9
current_guess = 0

while True:
    user_num = int(input("Enter a number:\n"))
    if user_num > secret_number:
        print("Too big, try again")
        current_guess = current_guess + 1
        no_of_guesses_left = total_guesses - current_guess
        print("No of guesses left: ", no_of_guesses_left)
        if no_of_guesses_left == 0:
            print("You Lost!")
            break
        else:
            continue
    elif user_num < secret_number:
        print("Too small, try again")
        current_guess = current_guess + 1
        no_of_guesses_left = total_guesses - current_guess
        print("No of guesses left: ", no_of_guesses_left)
        if no_of_guesses_left == 0:
            print("You Lost!")
            break
        else:
            continue

    else:
        print("You Won!")
        print("Total guesses used: ", current_guess)
        break
