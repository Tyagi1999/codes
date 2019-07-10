# asked by Uber

# Given an array of integers, return a new array such that each element at index i of the new
# array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

n=[int(i) for i in input("enter list of numbers: ").split()]
output_list=[]

for i in n:
    product=1
    copy_list=[]
    copy_list=n.copy()
    copy_list.remove(i)
    for j in range(len(copy_list)):
        product=product*copy_list[j]
    output_list.append(product)
    
print("Output list is {0}".format(output_list))    
