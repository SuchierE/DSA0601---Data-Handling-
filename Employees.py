import matplotlib.pyplot as plt

departments = ["HR", "Marketing", "Finance", "IT", "Sales"]
percentages = [15, 25, 20, 30, 10]

plt.pie(percentages, labels=departments, autopct="%1.1f%%", startangle=90)
plt.title("Employee Distribution by Department")
plt.axis("equal")
plt.show()

total_employees = 200
marketing = total_employees * percentages[1] / 100

print("Employees in Marketing Department:", int(marketing))