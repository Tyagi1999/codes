# asked by FACEBOOK

# Ques.: Given any number you have to find the number of ways to decode that number like
# if you are given 12 then it can be decode as "ab" where a=1 and b=2 and "l" where l=12
# so total number of ways to decode 12 is 2 as "ab" and "l"


n=input("enter number: ")

def num_ways(n):
    return helper(n,len(n))

def helper(n,k):
    if k==0:
        return 1
    s=len(n)-k
    if n[s]=='0':
        return 0
    result=helper(n,k-1)
    if k>=2 and int(n[s:s+2])<=26:
        result+=helper(n,k-2)
    return result

print('no. of ways to decode this msg is {0}'.format(num_ways(n)))
