from itertools import*
count=0
count1=0
l=[str(x) for x in input("Enter your letters: ").split()]


#PERMUTATIONS
per=permutations(l)
for i in list(per):
    print(i)
    count=count+1
print("Total no. of permutations are: "+str(count))

#COMBINATI0NS

n=int(input("Enter the number upto which letters are combined: "))
com=combinations(l,n)
for i in list(com):
    print(i)
    count1=count1+1
print("Total no. of combinations are: "+str(count1))    
