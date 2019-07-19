# asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and
# a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

s1=input("enter the string: ")
set_of_string=['dog','deer','deal','damn','decease']
result=[]
        
for i in set_of_string:
    if s1==i[0:len(s1)]:
        result.append(i)

print("Possible autocomplete strings are: {0}".format(result))        
