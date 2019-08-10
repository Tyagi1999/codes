# asked by Microsoft

# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
'''2
   1.5
   2
   3.5
   2
   2
   2
'''   


import math

inp=[int(x) for x in input("enter the input list: ").split()]

temp=[]
for i in inp:
    temp.append(i)
    temp.sort()
    if len(temp)%2==0:
        result=(temp[len(temp)//2]+temp[(len(temp)//2)-1])/2
        print(result)
    else:
        result=temp[math.floor(len(temp)/2)]
        print(result)
