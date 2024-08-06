class Stack:
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items) == 0
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if not self.isempty():
           return self.items.pop()
        else:
            print("stack is empty")
    def peek(self):
        if not self.isempty():
            return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
st = Stack()
st.push(4)
st.push(7)
st.push(9)
st.push(8)
st.push(98)
st.push(99)
print(st.peek())
print(st.size())
# print(st.pop())
# print(st.pop())
# print(st.pop())
# print(st.pop())