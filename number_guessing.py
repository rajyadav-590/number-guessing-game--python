import random

computer_guess = random.randint(1, 100)
attempts = 0

def number_guessing_game(user_guess, attempts):
    attempts += 1
    
    if user_guess == computer_guess:
        print(f"Guessed it correct in {attempts} attempts")
        return attempts, True
    elif user_guess < computer_guess:
        print(f"Your guess is lower. Attempts left: {10 - attempts}")
    else:
        print(f"Your guess is higher. Attempts left: {10 - attempts}")
        
    return attempts, False


print("Welcome to Number Guessing Game")
print("You have 10 attempts")

for i in range(10):
    try:
        user_guess = int(input("Enter your choice from 1 to 100: "))
        
        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100")
            continue
            
    except ValueError:
        print("Invalid input! Please enter a number only.")
        continue
    
    attempts, correct = number_guessing_game(user_guess, attempts)
    
    if correct:
        break
else:
    print(f"You lost! The number was {computer_guess}")
