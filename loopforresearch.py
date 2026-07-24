#Catherine Hendrie
#Thursday July 23rd
#Goal of the program is to use built in python tools to find the LCM, as well as euclidians algorithm
#and use the built in time tool to compare the speed

#Imports
import time
import math
import random

start1 = time.time() #Start timer
for _ in range(100):
   
    #variables
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    remainder = 1
    temp = 0
    a = number1
    b = number2

    #Euclidian Algorithm - Finding GCD
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
for _ in range(100):
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    lcm2 = math.lcm(number1,number2)
end2 = time.time() #End timer

time2 = end2 - start2

comparison = time1 - time2
percentdiff = (time1 / time2) * 100


print("The difference in time between the two methods was", comparison, "seconds")
print("The percentage difference between the two methods was", percentdiff, "%")
print("The time it took to find the LCM 1000 times using the Euclidian Algorithm was (manually)", time1, "seconds")
print("The time it took to find the LCM 1000 times using the built in Python tools was", time2, "seconds")


