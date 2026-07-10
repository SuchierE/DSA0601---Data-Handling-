import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
votes = [25, 18, 30, 12, 15]

plt.bar(fruits, votes, color="lightgreen", edgecolor="black")
plt.title("Favourite Fruit Survey")
plt.xlabel("Fruit")
plt.ylabel("Number of Votes")
plt.show()

most = fruits[votes.index(max(votes))]
least = fruits[votes.index(min(votes))]

print("Most Preferred Fruit:", most)
print("Least Preferred Fruit:", least)