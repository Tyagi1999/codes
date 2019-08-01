# asked by Microsoft
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible reconstruction, return any of them.
# If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

string_list=[str(x) for x in input("enter the list of words: ").split()]
string=input("enter the string: ")
output_list=[]

for i in range(len(string)):
    for j in range(i,len(string)+1):
        s=string[i:j]
        if s in string_list:
            output_list.append(s)
            break
        else:
            continue

print(output_list)
