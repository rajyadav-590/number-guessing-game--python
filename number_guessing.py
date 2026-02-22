#importing a module of pthon library name as random module
import random

#using random module for selecting a random number from 1 to 100 and storing in a variable named random_value
random_value = random.randint(1, 100)

#printing some statements
print("Welcome to Number Guessing Game")
print("Choose a number from 1 to 100. You have 10 attempts.")

attempts = 0
guessed = False
#using while loop for repeating statements 10 times
while attempts < 10:

    #error handling
    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    #conditional statements
    if user_input < 1 or user_input > 100:
        print("Please enter a number between 1 and 100")
        continue

    attempts += 1

    if user_input < random_value:
        if attempts == 10:
            print("Choice is less than the actual number")
        else:
            print("Choice is less than actual number, increase your number")

    elif user_input > random_value:
        if attempts == 10:
            print("Choice is greater than the actual number")
        else:
            print("Choice is greater than actual number, decrease your number")

    else:
        print(f"You guessed it correct in {attempts} attempts!")
        guessed = True
        break

if not guessed:
    print(f"You failed to guess the number in 10 attempts. The correct number was {random_value}")
