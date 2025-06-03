import random
print("Welcome to the number guessing hame\n-----------------------------")

low = int(input("Enter the lowest number \n-----------------------------\n"))
high = int(input("Enter the highest number \n-----------------------------\n"))
differential = high - low
number = random.randint(low, high)
number_of_guesses = 0
game_variation = input("Do you want one guess or until you get it right?(one/mulitple)")

if game_variation.lower() == "one":
    if differential >= 1:
        number = random.randint(low, high)
        user_guess = int(input("Enter your guess \n-----------------------------\n"))
        if user_guess == number:
            print(f'Congratulations you guessed the number! The number was {number}\n-----------------------------')
        else:
            print(f'Better luck next time. The number was {number} and your guess was {user_guess}\n-----------------------------')
    else:
        print("Invalid Data. The subtraction of lower number from higher number needs to equal atleast one\n-----------------------------")
elif game_variation.lower() == "multiple":
    while differential >= 1:
        user_guess = int(input("Enter your guess \n-----------------------------\n"))
        if user_guess == number:
            number_of_guesses += 1
            print(f'Congratulations you guessed the number! The number was {number}. You guessed {number_of_guesses} time/s.\n-----------------------------')
            break
        else:
            if user_guess < number:
                print(f'Wrong! Its a higher number, try again \n-----------------------------')
            elif user_guess > number:
                print(f'Wrong! Its a lower number, try again \n-----------------------------')
            
            number_of_guesses += 1
else:
    print("Invalid Data. Please choose beetween one guess or multiple guesses")
