#Find the roots of the equation a*x*x + b*x + c.
#Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
#can be found using a formula
import math
def Quadratic(a,b,c):
    #Finding a delta using formula
    delta = b*b-4*a*c
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    #print the root1 and root2
    print("Root 1  :", root1)
    print("Root 2  :", root2)

#Get input from user
a=int(input("Enter value a : "))
b=int(input("Enter value b : "))
c=int(input("Enter value c : "))
#calling function
Quadratic(a,b,c)