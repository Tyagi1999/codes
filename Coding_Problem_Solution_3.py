# asked by Google.

# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


k=int(input("enter the number: "))
list_of_no=[int(i) for i in input("enter your list of numbers: ").split()]
flag=0

for i in list_of_no:
    copy_list=list_of_no.copy()
    copy_list.remove(i)
    for j in copy_list:
        if i+j == k:
            flag=1
            break
        else:
            flag=0

if flag == 1:
    print("yes numbers of given list can add up to k.")
else:
    print("No")
    
        
        
