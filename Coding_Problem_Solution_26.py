# asked by Facebook
# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element

# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


string=input("enter the string: ")
pattern=input("enter the pattern: ")

m=len(string)
n=len(pattern)

result=[[False]*(n+1) for i in range(m+1)]
result[0][0]=True

for i in range(m+1):
    for j in range(1,n+1):
        if pattern[j-1]=="*":
            result[i][j]=result[i][j-2] or (i>0 and j>1 and (pattern[j-2]=='.' or string[i-1]==pattern[j-2]) and result[i-1][j])

        elif i>0 and (pattern[j-1]=="." or pattern[j-1]==string[i-1]):
            result[i][j]=result[i-1][j-1]


print(result[m][n])            
