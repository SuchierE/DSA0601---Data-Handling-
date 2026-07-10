import matplotlib.pyplot as plt

# Data
categories = ["Housing", "Transportation", "Food", "Entertainment"]
spending = [40, 20, 30, 10]

# Create Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(spending, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title("Household Budget Distribution")
plt.axis('equal')  # Makes the pie chart circular
plt.show()

# Calculate weighted average percentage
weighted_average = sum([x * x for x in spending]) / sum(spending)

print(f"Weighted Average Category of Spending: {weighted_average:.2f}%")

# Identify highest spending category
highest_category = categories[spending.index(max(spending))]
print(f"Highest Spending Category: {highest_category} ({max(spending)}%)")