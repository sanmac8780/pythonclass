
# Name: Saniya Mack
# Date: October 15, 2026
# Description: This program displays an application menu that allows
# users to input data, view current data, and generate a report.

from datetime import datetime

# Store the student ID and application data
studentId = "sanmac8780"
currentData = {}

# Display the application title
print(f"{studentId} Spreadsheet Automation Menu")

# Continue displaying the menu until the user exits
while True:
    print("\nPlease select an option:")
    print("1. Input Data")
    print("2. View Current Data")
    print("3. Generate Report")
    print("4. Exit")

    selectedOption = input("Enter your option number: ")

    # Record the current date and time
    currentDateTime = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

    print(f"\nSelected option: {selectedOption}")
    print(f"Date and Time: {currentDateTime}")

    # Option 1: Input data
    if selectedOption == "1":
        dataName = input("Enter the name of the data: ")
        dataValue = input("Enter the value of the data: ")

        currentData[dataName] = dataValue

        print("Data entered successfully.")

    # Option 2: View current data
    elif selectedOption == "2":
        print("\n--- Current Data ---")

        if currentData:
            for dataName, dataValue in currentData.items():
                print(f"{dataName}: {dataValue}")
        else:
            print("No data has been entered yet.")

    # Option 3: Generate a report
    elif selectedOption == "3":
        print("\n--- Data Report ---")
        print(f"Report generated: {currentDateTime}")

        if currentData:
            for dataName, dataValue in currentData.items():
                print(f"{dataName}: {dataValue}")
        else:
            print("No data is available to generate a report.")

        print(f"Total entries: {len(currentData)}")

    # Option 4: Exit the application
    elif selectedOption == "4":
        print("Exiting the Spreadsheet Automation Menu.")
        break

    # Handle invalid menu selections
    else:
        print("Invalid option. Please select 1, 2, 3, or 4.")

print("Program ended.")
