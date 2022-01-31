# Create Line Graph
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

Title = "Line Graph"
AxisX = "Axis X"
AxisY = "Axis Y"

# Subtitle
plt.title(Title)
plt.xlabel(AxisX)
plt.ylabel(AxisY)

plt.plot(x,y)
plt.show()