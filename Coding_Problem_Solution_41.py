# asked by Google

# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def isSubsetSum(set,n, sum): 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
   
    if (set[n - 1] > sum) : 
        return isSubsetSum(set, n - 1, sum)    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 
      
set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set) 
if (isSubsetSum(set, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum") 
      
