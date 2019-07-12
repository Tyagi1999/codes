"""asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place."""


input_list=[int(i) for i in input("enter the list: ").split()]
n=[]
for i in input_list:
    if i>=0:
        n.append(i)
for i in range(1,max(n)+1):
    if i not in n:
        ans=i
        break
    else:
        ans=max(n)+1

print("Lowest positive integer missing is {0}".format(ans))

