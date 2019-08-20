# asked by Amazon

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

stack=[]
def push(element):
    stack.append(element)
    return stack

def pop():
    if len(stack)==0:
        return None
    else:
        return stack.pop()

def Max():
    if len(stack)==0:
        return None
    else:
        return max(stack)

print(push(2))
print(push(5))
print(push(3))
print(push(7))
print(pop())
print(pop())
print(Max())
        
    

    
