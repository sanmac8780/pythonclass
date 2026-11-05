class zoodata:
    ...

# Prints student ID
print("sanmac8780")

# Import required libraries
import csv
import os
from datetime import datetime


# This function saves comma-separated data to a CSV file
def insertData(filePath, data):
    try:
        with open(filePath, "a", newline="") as file:
            file.write(data + "\n")
    except Exception as error:
        print("Error writing to file:", error)


# This function displays the contents and path of a CSV file
def viewData(filePath):
    try:
        print("Reading file:", filePath)

        with open(filePath, "r") as file:
            print(file.read())

    except Exception as error:
        print("Error reading file:", error)


# This function gets information from the user
# and saves the information into ZooData.csv
def getInput():
    try:
        data = input("Enter zoo data separated by commas: ")

        filePath = "ZooData.csv"

        insertData(filePath, data)

        print("The following data was saved at",
              datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              ":", data)

    except Exception as error:
        print("Error saving data:", error)


# This function controls the main menu
def main():
    while True:
        print("\nZoo Management Menu")
        print("1. Enter Zoo Data")
        print("2. View Zoo Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            getInput()

        elif choice == "2":
            viewData("ZooData.csv")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Calls the main function to start the program
main()
