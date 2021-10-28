#Program that takes two double command-line arguments t
#and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
#temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
#National Weather Service defines the effective temperature (the wind chill) to be:
import math
def windchill(t,v):
    w = 35.74 + (t * 0.615) + (0.4275 * t - 35.75) * (math.pow(v, 0.16))
    print("WindChill is :",w)

#Get input from user
t=int(input("Enter a value of t that within 50 :"))
v=int(input("Enter a value of v that between 3 and 120 :"))
#calling function
windchill(t,v)