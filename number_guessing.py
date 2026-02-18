#importing random module
import random
#defining variable to count in how many attempts user guess the correct answer
attempt=0
#taking random value from random module (between 1 to 100) and storing in a variable
computer_value=random.randint(1,100)
#using while loop
while True:
    #taking input from user
    user_input=int(input("Enter your choice: "))
    #counting atempts of user take to guess the correct answer
    attempt+=1
    #checking conditions using if-elif-else conditional statements
    if(user_input<computer_value):
        print("your choice is smaller then actual number increase your number")
    elif(user_input>computer_value):
        print("your choice is greater then actual number decrease your number")
    else:
        print(f"you guessed it correct in {attempt} attempts ")
        break
