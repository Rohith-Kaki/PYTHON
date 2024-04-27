class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            print("|\nv")
        print("None")
    def pop(self):
        first_node = self.head
        self.head = self.head.next
        first_node.next = None
        return first_node.data
    def push(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    #IN these above two methods we are using the linked list vertiacally, so the push and pop both happens at the start that is 
    #add at start and delete at start.
    
    #if you want to do it in horizontal direction then add at end delete at end.

stack1 = stack()
stack1.push(4)
stack1.push(73)
stack1.push(37)
stack1.push(2)
stack1.push(21)
stack1.display()
print("before pop")
stack1.pop()
stack1.pop()
print("after pop")
stack1.display()
