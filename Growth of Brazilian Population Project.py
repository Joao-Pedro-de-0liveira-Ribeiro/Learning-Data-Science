# Growth of Brazilian Population 1980-2016
# Datas was taken from DataSus
import matplotlib.pyplot as plt

Datas = open("populacao_brasileira.csv").readlines()  # Import the datas

x = []  # Store the years
y = []  # Store the Population

for i in range(len(Datas)):
    if i != 0:
        line = Datas[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))

# Subtitle
plt.title("Growth of Brazilian Population 1980-2016")
plt.xlabel("Years")
plt.ylabel("Population x 100.000.000")

# Custom
Gray = "e4e4e4"
Black = "k"
Dashed = "--"

# Graph
plt.bar(x, y, color="Gray")  # Create the bar table
plt.plot(x, y, color="Black", linestyle="--")  # Create the line table

# Show the table
plt.show()

# Save the Table
plt.savefig("Graph of Growth of Brazilian Population 1980-2016.png", dpi=300)
