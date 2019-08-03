# asked by Google
# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

input_list=[int(x) for x in input("enter the list: ").split()]
k=int(input("enter the integer: "))

del input_list[len(input_list)-k]

print(input_list)

