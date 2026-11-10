# Student ID: sanmac8780

import os
import csv
from datetime import datetime

import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference


# Find the folder that contains this Python file.
# Keep final.csv in the same folder as FinalExam.py.
folderPath = os.path.dirname(os.path.abspath(__file__))
csvFile = os.path.join(folderPath, "final.csv")
excelFile = os.path.join(folderPath, "final.xlsx")
studentID = "sanmac8780"


def askUser():
    """Ask for five numbers, add them, and display their total.

    Arguments: None.
    Returns: None.
    """
    total = 0.0

    # This loop asks for five numbers and adds each entered number
    # to total, keeping a running sum as the loop progresses.
    for number in range(1, 6):
        while True:
            try:
                userNumber = float(input(f"Enter number {number} of 5: "))
                total += userNumber
                break
            except ValueError:
                print("Please enter a valid number.")

    print("The total of the five numbers is:", total)
  def askIncome():
    """Ask for five names and incomes and append them to final.csv.

    Arguments: None.
    Returns: None.
    """
    if not os.path.isfile(csvFile):
        print("Error: final.csv was not found in:", folderPath)
        return

    # If the existing CSV file does not end with a newline, add one
    # so the first new record starts on its own line.
    if os.path.getsize(csvFile) > 0:
        with open(csvFile, "rb+") as checkFile:
            checkFile.seek(-1, os.SEEK_END)
            lastCharacter = checkFile.read(1)
            if lastCharacter not in (b"\n", b"\r"):
                checkFile.write(b"\n")

    with open(csvFile, "a", newline="", encoding="utf-8") as dataFile:
        writer = csv.writer(dataFile)

        # This loop requests five names and annual incomes, then writes
        # each name-income pair as a new row at the end of final.csv.
        for number in range(1, 6):
            name = input(f"Enter the name of person {number} of 5: ").strip()

            while True:
                try:
                    income = int(input(f"Enter {name}'s annual income: "))
                    break
                except ValueError:
                    print("Please enter the income as a whole number.")

            writer.writerow([name, income])

    print("Five new records have been appended to final.csv.")
def loadIncomeData():


    """Read valid names and integer incomes from final.csv.

    Arguments: None.
    Returns: A tuple containing a list of names and a list of incomes.
    """
    names = []
    incomes = []

    with open(csvFile, "r", newline="", encoding="utf-8-sig") as dataFile:
        reader = csv.reader(dataFile)

        # This loop reads each CSV row. Rows with headings or invalid
        # income values are skipped; valid incomes are converted to ints.
        for row in reader:
            if len(row) < 2:
                continue

            try:
                incomeText = row[1].replace("$", "").replace(",", "").strip()
                income = int(float(incomeText))
                names.append(row[0].strip())
                incomes.append(income)
            except ValueError:
                # Skip a header row or any row without a numeric income.
                continue

    return names, incomes


def excelPie():
    """Create final.xlsx containing the income data and an Excel pie chart.

    Arguments: None.
    Returns: None.
    """
    names, incomes = loadIncomeData()

def excelPie():
    """Create final.xlsx containing the income data and an Excel pie chart.

    Arguments: None.
    Returns: None.
    """
    names, incomes = loadIncomeData()

    if not names:
        print("No valid name and income records were found in final.csv.")
        return

    # Create a new Excel workbook.
    workbook = Workbook()

    # Select the active worksheet in the workbook.
    sheet = workbook.active

    # Give the worksheet a descriptive name.
    sheet.title = "Annual Income"

    # Write the column headings into the first row.
    sheet.append(["Name", "Annual Income"])

    # Write each name and its integer income into the worksheet.
    for name, income in zip(names, incomes):
        sheet.append([name, int(income)])

    # Create an Excel pie chart object.
    pie = PieChart()
  # Select the income values in column B, including the heading.
    data = Reference(sheet, min_col=2, min_row=1, max_row=sheet.max_row)

    # Add the selected income values to the pie chart.
    pie.add_data(data, titles_from_data=True)

    # Select the names in column A to use as pie chart labels.
    labels = Reference(sheet, min_col=1, min_row=2, max_row=sheet.max_row)

    # Set the names as the pie chart's category labels.
    pie.set_categories(labels)

    # Set the title to the student ID and today's date.
    today = datetime.now()
    pie.title = f"{studentID} {today:%B} {today.day}, {today:%Y}"

    # Place the pie chart on the worksheet starting at cell D2.
    sheet.add_chart(pie, "D2")

    # Save the workbook, including its data and pie chart, as final.xlsx.
    workbook.save(excelFile)

    print("Excel pie chart saved as final.xlsx.")


def verticalBar():
    """Create and display a matplotlib vertical bar chart of the incomes.

    Arguments: None.
    Returns: None.
    """
    names, incomes = loadIncomeData()

    if not names:
        print("No valid name and income records were found in final.csv.")
        return

    # Create a vertical bar graph using each person's income.
    plt.bar(names, incomes)

    # Set the title to the student ID and today's date.
    today = datetime.now()
    plt.title(f"{studentID} {today:%B} {today.day}, {today:%Y}")

    # Label the horizontal axis with the names.
    plt.xlabel("Name")

    # Label the vertical axis with annual income.
    plt.ylabel("Annual Income ($)")

    # Rotate the names so they are easier to read.
    plt.xticks(rotation=45, ha="right")

    # Adjust spacing so labels are not cut off.
    plt.tight_layout()
  # Display the vertical bar graph.
    plt.show()


# Run the assignment functions in order.
def main():
    print("FINAL EXAM PROGRAM")
    print("------------------")

    if not os.path.isfile(csvFile):
        print("Error: Put final.csv in the same folder as FinalExam.py.")
        print("Expected folder:", folderPath)
        return

    askUser()
    askIncome()
    excelPie()
    verticalBar()


if __name__ == "__main__":
    main()

