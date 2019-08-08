# asked by Google

# The edit distance between two strings refers to the minimum number of character insertions,
# deletions, and substitutions required to change one string to the other.
# For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


string1=input("enter the first string: ")
string2=input("enter the second string: ")

length1=len(string1)
length2=len(string2)

count=0
diff=abs(length1-length2)
count=count+diff

for i in range(0,min(length1,length2)):
    if string1[i]==string2[i]:
        continue
    else:
        count+=1

print(count)        
