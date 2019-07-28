# asked by Google

# Given two singly linked lists that intersect at some point, find the intersecting node.
# The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
# return the node with value 8.
# In this example,assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

def intersection(a,b):
    i=0
    while a[i]!=b[i]:
        if a[i]==None:
            a=b
        elif b[i]==None:
            b=a
        else:
            i=i+1
    return a[i]

a=[int(x) for x in input("enter first list: ").split()]
b=[int(x) for x in input("enter the second list: ").split()]
a.append(None)
b.append(None)
print("intersection is: {0}".format(intersection(a,b)))


