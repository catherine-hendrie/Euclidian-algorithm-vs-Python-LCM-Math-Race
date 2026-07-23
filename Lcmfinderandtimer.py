#Catherine Hendrie
#Thursday July 23rd
#Goal of the program is to use built in python tools to find the LCM, as well as euclidians algorithm
#and use the built in time tool to compare the speed

#Imports
#from math import remainder
import time
import math

#variables
number1 = 0
number2 = 0
remainder = 1
temp = 0
a = 0
b = 0


#Getting integers to run calculations with
number1 = int(input("Please enter your first integer:"))
number2 = int(input("Please enter your 2nd integer:"))
a = number1
b = number2

#Euclidian Algorithm - Finding GCD
start1 = time.time() #Start timer
while number2 > 0:
    remainder = number1 % number2
    temp = number2
    number2 = remainder
    number1 = temp

#Euclidian Algorithm - Finding LCM
lcm1 = (a*b)/temp
end1 = time.time() #End timer

time1 = end1 - start1

#Using built in Python tools to find LCM
start2 = time.time() #Start timer
lcm2 = math.lcm(a,b)
end2 = time.time() #End timer

time2 = end2 - start2

print("The LCM of", a, "and", b, "is", lcm2)
print("The time it took to find the LCM using the Euclidian Algorithm was (manually)", time1, "seconds")
print("The time it took to find the LCM using the built in Python tools was", time2, "seconds")

comparison = time2 - time1
percentdiff = time1 / time2 * 100

print("The difference in time between the two methods was", comparison, "seconds")
print("The percentage difference between the two methods was", percentdiff, "%")

if lcm1 == lcm2:
    print("The two methods produced the same result of:", lcm2)
else:
    print("The two methods produced different results")