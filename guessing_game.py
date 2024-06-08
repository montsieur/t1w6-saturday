# Guessing game

guess_num = 5

user_guess = None

while user_guess != guess_num:
    user_guess = input(print("What is your guess between 1 and 10: "))

print("Correct.")

# Make it better

# Giving hints

while user_guess != guess_num:
    user_guess = int(input("What is your guess (between 1 and 10)?"))

    if user_guess < guess_num:
        print("Too low!")
    elif user_guess > guess_num:
        print("Too high!")
    else:
        print("Correct!")