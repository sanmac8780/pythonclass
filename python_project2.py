import python_project


python_project

# Name: Saniya Mack
# Date: October 19, 2026

from datetime import datetime

# Store student ID
student_id = "sanmac8780"

# store menu options in a dictionary
menuOptions = {
    1: 'Input Data',
    2: 'View Current Data',
    3: 'Generate Report',
}

# Display the application menu as the firat output line
print(f"{student_id} Spreadsheet Application Menu")

# Display the menu using a for-loop
for optionNumber, optionDescription in menuOptions.items():
    print(f"{optionNumber}. {optionDescription}")

# Get the user's selection
selectedOption = input("Enter your option number: ")

# Validate the user's selection
if selectedOption in menuOptions:
   currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

   print(f"Selected Option: {selectedOption}")
   print(f"Date and Time: {currentDateTime}")
else:
    print("Invalid option selected. Please try again.")
