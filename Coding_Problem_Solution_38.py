# asked by Google

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


inp=[x for x in input("enter the input array: ").split()]

# Simple python code using prebuilt functions.
inp.sort()
inp.reverse()
print(inp)


# Code using functions without using any predefined library.
def sort(rgbs):
    left_index,right_index=0,len(rgbs)-1
    while True:
        while rgbs[left_index]=='R' and left_index<right_index:
            left_index+=1

        while rgbs[right_index]!='R' and left_index<right_index:
            right_index-=1

        if left_index>=right_index:
            break
        rgbs[left_index],rgbs[right_index]=rgbs[right_index],rgbs[left_index]

    right_index=len(rgbs)-1
    while True:
        while rgbs[left_index]!='B' and left_index<right_index:
            left_index+=1

        while rgbs[right_index]=='B' and left_index<right_index:
            right_index-=1

        if left_index>=right_index:
            break

        rgbs[left_index],rgbs[right_index]=rgbs[right_index],rgbs[left_index]

    return rgbs

print(sort(inp))
