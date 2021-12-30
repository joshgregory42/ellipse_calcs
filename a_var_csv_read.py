import csv

import matplotlib.pyplot as plot
import matplotlib.figure as figure

f = open('a_var.csv', 'r')

reader = csv.reader(f)

data = []

for row in reader:
    data.append(row)

x = []
y = []
length = len(data)
for i in range(0, length):
    x.append(data[i][0])
    y.append(data[i][1])

# Plotting
plot.plot(x, y)
plot.show()

