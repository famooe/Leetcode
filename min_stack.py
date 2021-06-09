class MinStack(object):
    min = float('inf')
    def __init__(self):
        self.min = float('inf')
        self.stack = []
                

    def push(self, val):
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)
                

    def pop(self):
        top = self.stack[-1]
        self.stack.pop()
        if self.min == top:
            self.min = self.stack[-1]
            self.stack.pop()
                

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min
