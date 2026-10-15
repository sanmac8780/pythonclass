
# Name: Your Name
# Date: October 15, 2026
# Description: This program asks the user to guess a number,
# checks the guess, counts attempts, and demonstrates while and for loops.

# Get the user's information
userName = input("Enter your name: ")
studentId = input("Enter your Student ID: ")

# Set the predetermined number and initialize variables
correctGuess = 5
numberOfTries = 0
userGuess = 0

# Greet the user
print("\n================================")
print("Number Guessing Game")
print("Student ID:", studentId)
print("Welcome,", userName + "!")
print("================================")

# Ask the user to guess until the correct number is entered
while userGuess != correctGuess:
    userGuess = int(input("Guess a number between 1 and 10: "))
    numberOfTries += 1

    # Determine whether the guess is too high, too low, or correct
    if userGuess > correctGuess:
        print("Your guess is too high. Try again!")
    elif userGuess < correctGuess:
        print("Your guess is too low. Try again!")
    else:
        print("Congratulations! You guessed correctly!")

# Display the number of tries
print("\nStudent ID:", studentId)
print("Number of tries:", numberOfTries)

# Demonstrate a while loop five times
print("\nOutput from the while loop:")
loopGuess = correctGuess
loopCount = 0

while loopCount < 5:
    loopGuess += 1
    print("x incremented by 1 is", loopGuess)
    loopCount += 1

# Demonstrate a for loop accomplishing the same task
print("\nOutput from the for loop:")
loopGuess = correctGuess

for loopCount in range(5):
    loopGuess += 1
    print("x incremented by 1 is", loopGuess)
