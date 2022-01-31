# Create Bar Graph
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

Title = "Bar Graph"
AxisX = "Axis X"
AxisY = "Axis Y"

# Subtitle
plt.title(Title)
plt.xlabel(AxisX)
plt.ylabel(AxisY)

plt.bar(x,y)
plt.show()