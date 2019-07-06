print("                      *** TOWER OF HANOI ***")
print("                      _______solution_______")
n=int(input("\nEnter number of disks: "))
def toh(n,beg,end,aux):
    if n==1:
        print("MOVE FROM "+beg+" TO "+end+".")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        toh(n-1,beg,aux,end)
        print("MOVE FROM "+beg+" TO "+end+".")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        toh(n-1,aux,end,beg)
toh(n,"*A*","*C*","*B*")
print("A: Starting pole   B: Auxiliary pole   C: Destination pole")
print("Total number of steps are: "+str((2**n)-1))
