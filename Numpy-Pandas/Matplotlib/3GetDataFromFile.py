#  Write a Python program to draw a line using given axis values taken from a text file, with
# suitable label in the x axis, y axis and a title.
# Test Data:
# test.txt
# 1 2
# 2 4
# 3 1
import matplotlib.pyplot as plt
with open("C:\\Users\\91807\\Desktop\\Numpy-Pandas\\Matplotlib\\test1.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()
