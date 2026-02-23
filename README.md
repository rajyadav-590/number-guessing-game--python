# Number Guessing Game (Python)

A simple Python-based Number Guessing Game where the computer selects a random number between 1 and 100, and the user has 10 attempts to guess it correctly.

---

## Project Description

This is a command-line game built using Python. The program generates a random number, and the player tries to guess it within a limited number of attempts.

The game provides hints after each guess:

* If the guess is too low → asks to increase the number
* If the guess is too high → asks to decrease the number
* If guessed correctly → shows the number of attempts taken

The program also handles invalid inputs (like text or numbers outside the range).

---

## Features

* Random number generation using Python's `random` module
* Maximum 10 attempts
* Hints after each guess (Higher / Lower)
* Input validation

  * Handles non-numeric input
  * Ensures number is between 1 and 100
* Displays the correct number if the player loses

---

## Technologies Used

* Python 3
* Random module
* Command-line interface

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/number-guessing-game.git
```

2. Navigate to the project folder

```
cd number-guessing-game
```

3. Run the Python file

```
python number_guessing.py
```

---

## Game Rules

* The computer selects a number between **1 and 100**
* You have **10 attempts** to guess the correct number
* After each guess:

  * If your guess is low → You will be asked to increase the number
  * If your guess is high → You will be asked to decrease the number
* If you fail after 10 attempts, the correct number will be displayed

---

## Example Output

```
Welcome to Number Guessing Game
You have 10 attempts

Enter your choice from 1 to 100: 50
Your guess is lower. Attempts left: 9

Enter your choice from 1 to 100: 75
Your guess is higher. Attempts left: 8
```

---

## Folder Structure

```
number-guessing-game/
│
├── number_guessing.py
└── README.md
```

---

## Author

Raj Yadav
B.Tech Student | Python Beginner

---

## Future Improvements

* Add difficulty levels (Easy/Medium/Hard)
* Add graphical interface (GUI)
* Add score tracking system
* Add replay option
