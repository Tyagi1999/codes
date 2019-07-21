# asked by AMAZON
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

s=input("enter the string: ")
k=int(input("enter the number of atmost distinct character: "))
l1=[]
len_list=[]
for i in range(len(s)):
    n=k
    l2=[]
    sub_s=s[i]
    l2.append(s[i])
    for j in s[i+1:]:
        
        if j in l2:
            l2.append(j)
            sub_s=sub_s+j
        elif n==1:
            break    
        elif j not in l2:
            n=n-1
            l2.append(j)
            sub_s=sub_s+j        
            
    l1.append(sub_s)
   
for i in l1:
    len_list.append(len(i))
dictionary={}
for i in range(len(l1)):
    dictionary[len_list[i]]=l1[i]
    
print("Substring is: {0}".format(dictionary[max(len_list)]))    
            
        
