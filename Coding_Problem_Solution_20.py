# asked by Amazon
# Count the number of negative integers in the given matrix.
# the matrix is given in such a way that the number of negative integer in one
# row is always more than the next row.

""" one naive way to solve this problem is to iterate every row and column of
the matrix and increment the count if found the negative integerbut this
solution has more complexity than the given below method."""

Given_Matrix=[[-3,-2,-1,1],
              [-2,-2,-3,-4],
              [-4,5,7,8]]

def func(M,n,m):
    count=0
    i=0
    j=m-1
    while j>=0 and i<n:
        if M[i][j]<0:
            count+=(j+1)
            i+=1
        else:
            j-=1
    return count

print(func(Given_Matrix,3,4))
