# Write a program Distance.java that takes two integer command-line arguments x
# and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
# formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
import math
def findDistance():
    x = int(input("Enter the value for x :"))
    y = int(input("Enter the value for y  :"))
    #find the distance using formula
    distance =math.sqrt(math.pow(x,x)+math.pow(y,y))
    print("Euclidean Distance is :",distance)

#calling funtion 
findDistance()

