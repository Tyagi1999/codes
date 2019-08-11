# asked by Quora

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.
# If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome).
# There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".


inp=input("enter the string: ")
temp=""

if inp==inp[::-1]:
    print(inp)
else:
    for i in range(len(inp)-1,-1,-1):
        string=inp
        temp=temp+inp[i]
        string=temp+string
        if string==string[::-1]:
            print(string)
            break

    
    
