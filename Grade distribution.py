import matplotlib.pyplot as plt

# Number of students in each grade
grades = ["A", "B", "C", "D", "E"]
students = [6, 8, 7, 5, 4]  # Total = 30

# Midpoint score for each grade
mid_scores = [95, 85, 75, 65, 50]

# Bar Chart
plt.bar(grades, students, color="skyblue", edgecolor="black")
plt.title("Grade Distribution of 30 Students")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

# Average Score
average = sum(s * m for s, m in zip(students, mid_scores)) / sum(students)

print("Average Score of the Class:", round(average, 2))