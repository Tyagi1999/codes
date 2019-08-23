# asked by Amazon

# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

inp=input("enter the input: ")
max_length=0
for i in range(0,len(inp)):
    for j in range(i,len(inp)):
        s=inp[i:j+1]
        length=len(s)
        if s==s[::-1]:
            if length>=max_length:
                sub=s
                max_length=length

print(sub)
