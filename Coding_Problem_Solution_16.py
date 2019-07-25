# asked by Google
# From a given string return the first recurring character of the string.
# for e.g. if string id "ABCDBA" then return "B"
# if string is "ABCD" return None because no character is recurring.

s=input("enter the string: ")

def First_Rec_Char(s):
    char_list=[]
    for i in s:
        if i in char_list:
            return i
        else:
            char_list.append(i)
    return None
print("first recurring character is {0}".format(First_Rec_Char(s)))
