import matplotlib.pyplot as plt

activities = ["Video Games", "Reading", "Cooking", "Painting", "Music Listening"]
percentages = [20, 35, 20, 10, 25]

plt.pie(percentages, labels=activities, autopct="%1.1f%%", startangle=90)
plt.title("Weekend Activities of Employees")
plt.axis("equal")
plt.show()

most_common = activities[percentages.index(max(percentages))]

print("Most Common Weekend Activity:", most_common)