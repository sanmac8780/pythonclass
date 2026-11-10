import os
import csv
import openpyxl
from openpyxl.chart import BarChart, LineChart
from datetime import datetime

# This function takes two arguments:
# filePath (string): Path to the CSV file.
# chartType (string): Type of chart (line or bar).
# Returns: Nothing. Creates an Excel file with a chart.

def createChart(filePath, chartType):

    choice = input("Choose data source: 1. Fahrenheit 2. Celsius: ")

    dates = []
    values = []

    with open(filePath, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dates.append(row["Date"])

            if choice == "1":
                values.append(float(row["Fahrenheit"]))
            elif choice == "2":
                values.append(float(row["Celsius"]))

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet.append(["Date", "Temperature"])

    for date, value in zip(dates, values):
        sheet.append([date, value])

    if chartType == "bar":
        chart = BarChart()
    elif chartType == "line":
        chart = LineChart()
    else:
        print("Invalid chart type.")
        return

    chart.title = "sanmac8780 " + datetime.now().strftime("%m/%d/%Y")
    chart.x_axis.title = "Date"

    if choice == "1":
        chart.y_axis.title = "Temperature (Fahrenheit)"
    else:
        chart.y_axis.title = "Temperature (Celsius)"

    data = openpyxl.chart.Reference(
        sheet, min_col=2, min_row=1, max_row=sheet.max_row
    )

    categories = openpyxl.chart.Reference(
        sheet, min_col=1, min_row=2, max_row=sheet.max_row
    )

    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)

    sheet.add_chart(chart, "D2")

    workbook.save("final.xlsx")

# This function takes one argument:
# filePath (string): Path to the CSV data file.
# Returns: Nothing. Calls createChart to generate a report.

def generateReport(filePath):

    chartChoice = input("Choose chart type (line or bar): ")

    if chartChoice == "line" or chartChoice == "bar":
        createChart(filePath, chartChoice)
    else:
        print("Invalid chart selection.")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

choice = input("Enter your choice: ")

if choice == "1":
    getInput()

elif choice == "2":
    viewData(filePath)

elif choice == "3":
    generateReport(filePath)

    print("Report successfully created!")
