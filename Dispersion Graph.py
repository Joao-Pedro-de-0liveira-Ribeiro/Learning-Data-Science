# Create Dispersion Graph
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

Title = "Scatterplot: Dispersion Graph"
AxisX = "Axis X"
AxisY = "Axis Y"

# Subtitle
plt.title(Title)
plt.xlabel(AxisX)
plt.ylabel(AxisY)

plt.scatter(x,y)
plt.show()