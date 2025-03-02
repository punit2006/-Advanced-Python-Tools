import numpy as np
import matplotlib.pyplot as plt

#1
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]

#1A
plt.plot(x, y)

#1B
plt.title("Line Plot of x vs y")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()

#2
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

#2A
plt.bar(students, marks, color='skyblue')

#2B
plt.title("Marks Scored by Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

#3
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]

#3A
plt.pie(revenue, labels=regions, autopct='%1.1f%%')

#3B
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=[0.1, 0, 0, 0])
plt.title("Revenue Distribution by Region")
plt.show()

#4
random_integers = np.random.randint(1, 101, size=1000)

plt.hist(random_integers, bins=20, edgecolor='black')
plt.title("Histogram of Random Integers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
