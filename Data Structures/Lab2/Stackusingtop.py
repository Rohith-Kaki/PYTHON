class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0]*size
        self.top = -1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.size - 1
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = item
        else:
            print("stack overflow")
    def pop(self):
        if not self.isEmpty():
            item = self.stack.pop(self.top)
            self.top -= 1
            return item
        else:
            print("stack underflow")
    def peek(self):
        return self.stack[self.top]
    def display(self):
        if not self.isEmpty():
            for i in self.stack:
                print(i, end="|")
            print("none")
        else:
            print("stack is underflow")
    

if __name__ =="__main__" :
    st = Stack(2)
    st.push(1)
    st.push(2)
    st.display()
    print(st.pop())
    print()
    st.display()
    print()
    print(st.pop())
    print()
    st.display()
    # print(st.peek())
    # print(st.peek())
    # print()
    # print(st.pop())
    # print()
    # print(st.display())

