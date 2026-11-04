# Print student ID
print("sanmac8780")

# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Store a classroom roster of 10 students in an array
students = ["John", "Mary", "Richard", "Jane", "Michael",
            "Sarah", "David", "Emily", "James", "Jessica"]

# Store the subjects
subjects = ["Math", "Science"]

# Create a list of grades for each student
grades = [
    [85, 90],
    [92, 88],
    [78, 95],
    [90, 92],
    [88, 85],
    [95, 91],
    [80, 87],
    [89, 94],
    [76, 82],
    [93, 96]
]

# Step 3: Create a MultiIndex using student names and subjects
index = pd.MultiIndex.from_product(
    [students, subjects],
    names=["Student", "Subject"]
)

# Step 4: Create a DataFrame containing student grades
# Repeat each student's grades for the two subjects
grade_values = [grade for student_grades in grades
                for grade in student_grades]

df = pd.DataFrame(grade_values, index=index, columns=["Grade"])

# Step 5: Display the DataFrame
print("\nClassroom Grades:")
print(df)

# Step 6: Group the grades by subject and calculate the mean
subject_means = df.groupby(level="Subject")["Grade"].mean()

print("\nAverage Grades by Subject:")
print(subject_means)

# Step 7: Create and display a vertical bar graph
subject_means.plot(kind="bar")

plt.title("Average Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.xticks(rotation=0)

plt.show()
