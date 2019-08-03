# From a given string return the character which is repeating the maximum time continuously.
# for example if string is "AABCDDBBBEA" , then the result should be {'B':3}

s=input("enter the string: ")
max_count=0
max_char=None
prev=None
for i in s:
    if prev==i:
        count+=1
    else:
        count=1
    if count>max_count:
        max_count=count
        max_char=i
    prev=i

print("Maximum repeating character is : {0}".format({max_char:max_count}))    


