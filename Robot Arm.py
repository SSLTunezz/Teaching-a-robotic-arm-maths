#setup
import math
import serial
import time

ARM = 5
#main code
print ("Enter X co-ordinate")
X = int(input())
print ("Enter Y co-ordinate")
Y = int(input())
if (X**2)+(Y**2) <= 100:
    print ("Great! Working on it")
    distance = math.sqrt((X**2)+(Y**2))
    angle = ((math.acos(((2 * (ARM ** 2)) - distance ** 2) / (2 * (ARM ** 2))))*(180/math.pi))
    a1 = angle
    a2 = 180-angle
    base = (math.atan((Y)/(X))*(180/math.pi))
    b1 = (base-((180-a1)/(2)))
    b2 = (base-((180-a2)/(2)))
    #print (abs(a1+b1)) ONLY ADD FOR SANITY CHECKS
    #print (abs(a2+b2)) ONLY ADD FOR SANITY CHECKS

#PRINTING THE RESULTS 
    if abs((a1+b1))<abs((a2+b2)):
        print ("solution 1")
        print (a1)
        print (b1-a1)
        shoulder = a1
        elbow = b1 - a1

    else:
       print ("solution 2")
       print (a2)
       print (b2-a2)
       shoulder = a2
       elbow = b2 - a2
else:
    print ("Not possible, try a lower value..")


