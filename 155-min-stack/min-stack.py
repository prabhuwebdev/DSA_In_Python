class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)
        
        
    def pop(self):
        popped=self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
        
        