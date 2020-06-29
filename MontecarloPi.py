import random
import math

PUNTI=12500000
punti=0 
for p in range(PUNTI):
    x=random.random()
    y=random.random()
    if(x**2+y**2 <= 1): 
        punti+=1
pigreco=4*punti/PUNTI
error = abs(math.pi-pigreco)
#----------------------------------------------------------
print("Points=%d, Point in circles=%d, PI=%.5f, Error=%.5f" %(PUNTI,punti,pigreco,error))