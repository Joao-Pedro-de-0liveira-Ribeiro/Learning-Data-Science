# Create Dispersion Graph
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [300, 500, 1000, 230, 10] # Control the size of Points

Title = "Scatterplot: Dispersion Graph"
AxisX = "Axis X"
AxisY = "Axis Y"

# Subtitle
plt.title(Title)
plt.xlabel(AxisX)
plt.ylabel(AxisY)

plt.scatter(x,y, label="Points", color='Black',s=z)
plt.plot(x,y, color='k', linestyle='--') #Create lines between the points
plt.legend()
plt.show()