# asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map where
# each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
# and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

# https://www.geeksforgeeks.org/trapping-rain-water/

def findwater(inp,n):
    left=[0]*n
    right=[0]*n
    water=0
    left[0]=inp[0]
    for i in range(1,n):
        left[i]=max(left[i-1],inp[i])

    right[n-1]=inp[n-1]

    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],inp[i])

    for i in range(0,n):
        water=water+min(left[i],right[i])-inp[i]

    return water

inp=[int(i) for i in input("enter the input: ").split()]
print("total water accumulated is: {0} units".format(findwater(inp,len(inp))))
