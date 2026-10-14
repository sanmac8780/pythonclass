
from datetime import datetime

# Display the application name
student_id = "YOUR_STUDENT_ID"
print(f"{student_id} Spreadsheet Automation Menu")

# Display the menu options
print("\nPlease select an option:")
print("1. Create a spreadsheet")
print("2. View a spreadsheet")
print("3. Update a spreadsheet")
print("4. Exit")

# The next line retrieves the inputted option and stores into the variable called option.
option = input("Enter your option number: ")

# Display the selected option and current date and time
print("\nYou selected option number:", option)
print("The time and date is", str(datetime.now()))
