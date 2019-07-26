# asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
# we should get: [10, 7, 8, 8], since
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)


from collections import deque
def Max_No(arr,n,k):
    q=deque()
    for i in range(k):
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k,n):
        print(str(arr[q[0]])+" ",end="")

        while q and q[0]<=i-k:
            q.popleft()

        while q and arr[i]>=arr[q[-1]]:
            q.pop()

        q.append(i)

    print(str(arr[q[0]]))

arr=[int(i) for i in input("enter the array: ").split()]
k=int(input("enter the value of k: "))
Max_No(arr,len(arr),k)
