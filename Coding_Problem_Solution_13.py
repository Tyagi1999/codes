# asked by Google
# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.


import random
import math

def est_pi(n):
    count=0
    total=0
    prev_pi,pi_approx=0,3
    
    while True:
        point=[]
        for i in range(n):
            point.append((random.random(),random.random()))
            if point[i][0]**2 + point[i][1]**2 <=1:
                count+=1
            total+=1
        prev_pi=pi_approx
        pi_approx=4*count/float(total)

        print("prev_pi={0},pi_approx={1}".format(prev_pi,pi_approx))
        if abs(prev_pi-pi_approx)<=1e-9:
            return pi_approx
        

print("estimated value of pi is: {0}".format(est_pi(1000)))        
