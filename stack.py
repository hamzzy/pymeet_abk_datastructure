class Stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
      return self.stack.pop()
    def push(self,val):
        self.stack.append(val)
        return self.stack
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size()==0


s=Stack()
t=[2,3,4]
l=s.push(t)
print(t.pop())
