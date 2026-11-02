
from datetime import datetime

# Function to convert the numerical data
def convertData(value, spreadsheet):
    if spreadsheet == "1":
        return (value - 32) * 5/9

    elif spreadsheet == "2":
        return value / 2.205

    elif spreadsheet == "3":
        return value * 2.54


# Function to collect and convert user input
def getInput(spreadsheet):
    entries = int(input("How many entries are being entered? "))

    for i in range(entries):
        date = input("Enter the date: ")
        value = float(input("Enter the numerical value: "))

        # convertData() requires the numerical value and spreadsheet type as arguments and returns the converted numerical value.
        convertedValue = convertData(value, spreadsheet)

        print("The following was saved at", datetime.now())
        print("Date:", date)
        print("Original value:", value)
        print("Converted value:", convertedValue)


# Main program
print("Select a spreadsheet:")
print("1. Temperature (F to C)")
print("2. Weight (lbs to Kg)")
print("3. Rainfall (inches to cm)")

choice = input("Enter your selection: ")

if choice == "1" or choice == "2" or choice == "3":
    getInput(choice)
else:
    print("Error: The chosen functionality is not implemented yet")
