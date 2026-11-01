
# Function One
def functionOne():
    print("My Student ID is sanmac8780")


# Function Two
def functionTwo():
    numberOne = float(input("Enter your first number: "))
    numberTwo = float(input("Enter your second number: "))

    totalSum = numberOne + numberTwo

    print("The sum of", numberOne, "and", numberTwo, "is", totalSum)

    return totalSum


# Function Three
def functionThree(totalSum):
    if totalSum > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")

    return 8780


# Main Function
def main():
    functionOne()  # Calls functionOne to display my student ID.
    totalSum = functionTwo()  # Calls functionTwo and stores the returned sum.
    studentIdNumber = functionThree(totalSum)  # Passes the sum to functionThree and stores its returned value.
    print("functionThree returned the value of", studentIdNumber)  # Displays the numeric portion of my student ID.


# Calls main to execute the program.
main()
