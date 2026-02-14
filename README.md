Password Generator – Python Project
Overview

This project is a command-line password generator written in Python.
It creates a random password based on the number of letters, numbers, and symbols specified by the user. The program demonstrates the use of lists, loops, and the random module to generate secure, randomized passwords.

Features

User-defined password length

Mix of letters, numbers, and symbols

Randomized character order (hard version)

Beginner-friendly implementation

Demonstrates list manipulation and shuffling

Technologies Used

Language: Python 3

Libraries:

random (for random selection and shuffling)

How It Works

The program asks the user:

How many letters to include

How many numbers to include

How many symbols to include

It selects random characters from predefined lists:

Alphabet (uppercase + lowercase)

Numbers

Symbols

Characters are stored in a list and shuffled to create a secure password.

The final password is printed.

Password Generation Logic

There are two versions in the code:

Easy Version (commented out)

Adds characters in order: letters → numbers → symbols

Password is predictable in structure

Hard Version (active)

Stores all characters in a list

Uses random.shuffle() to mix them

Produces a stronger, randomized password

How to Run

Install Python 3.

Save the file as:

password_generator.py

Open terminal/command prompt.

Run:

python password_generator.py

Enter the requested values.

Example Output
Welcome to the Password Generator!
How many letters would you like? 4
How many numbers would you like? 2
How many symbols would you like? 2

['a', 'K', 'm', 'Z', '5', '2', '@', '!']
['Z', '5', 'a', '@', 'm', '2', '!', 'K']
Z5a@m2!K
Learning Objectives

This project helps beginners understand:

Python lists

Loops (for)

Random selection using random.choice()

Shuffling using random.shuffle()

String concatenation

User input handling

Possible Improvements

Fix off-by-one error in range loops

Hide intermediate list prints

Validate user input

Add option to copy password to clipboard

Add GUI (Tkinter)

Enforce strong password rules

Author

Beginner Python practice project for learning randomness, loops, and password generation logic.
