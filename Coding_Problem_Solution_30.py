# asked by Facebook
# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


input_string="([])[]{()}"

def balanced(string):
    open_list=['(','[','{']
    closed_list=[')',']','}']
    dictionary={')':'(',']':'[','}':'{'}

    stack=[]
    for i in string:
        if i in open_list:
             stack.append(i)
        elif i in closed_list:
            if match(stack,i,dictionary):
                 stack.pop()
            else:
                return False
        else:
            raise ValueError("invalid string")

    if not stack:
        return True
    else:
        return False

def match(stack,i,dic):
    if not stack:
        return False
    else:
        if stack[-1]==dic[i]:
            return True
        else:
            return False

print(balanced(input_string))        
