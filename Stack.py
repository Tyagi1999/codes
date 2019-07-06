class Stack():
    def __init__(self):
        self.stack=[]
        
    def isEmpty(self):
        return self.stack==[]
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizestack(self):
        return len(self.stack)
    
stack=Stack()

print("pushing items into stack.....")
stack.push(1)
stack.push(2)
stack.push(3)

print("size is: ",stack.sizestack())
print("Popped: ",stack.pop())
print("Popped: ",stack.pop())
print("size is: ",stack.sizestack())
print("Peek: ",stack.peek())
print("size is: ",stack.sizestack())
