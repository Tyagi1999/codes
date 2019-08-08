# Given an array of numbers and an integer ,return the total number of subsets whose items' sum gives the total number equal to given integer.
# for exmample: if given array is [2,4,6,10] and integer is 16 then the total number of substes will be 2 i.e. [2,4,10] and [6,10].

def count_set(arr,total):
    mem = {}
    return helper(arr,total,len(arr)-1,mem)

def helper(arr,total,i,mem):
    key = str(total)+':'+str(i)
    if key in mem:
        return mem[key]

    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = helper(arr,total,i-1,mem)
    else:
        to_return = ( helper(arr,total-arr[i],i-1,mem) + helper(arr,total,i-1,mem) )

    mem[key] = to_return
    return to_return

arr=[int(x) for x in input("enter the array: ").split()]
total=int(input("enter the integer: "))

print("number of subsets are: {0}".format(count_set(arr,total)))
