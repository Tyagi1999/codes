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
        
    

    
