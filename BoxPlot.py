# Create a BoxPlot
import matplotlib.pyplot as plt
import random

List = []

for i in range(100):
    Number_Random = random.randint(0,50)
    List.append(Number_Random)

# Subtitle
plt.title("BoxPlot")

plt.boxplot(List)
plt.show()
