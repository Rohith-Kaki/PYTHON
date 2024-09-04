from collections import deque
class Stack:
    def __init__(self):
        self.items = deque()
    def push(self,item):
        self.items.append(item)
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("stack is empty")
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("stack is empty")
    def size(self):
        return len(self.items)
st = Stack()
st.push(9)
st.push(1)
st.push(94)
st.push(92)
st.push(91)
st.push(0)
print(st.peek())
