class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        while current:
            print(current.data, end = "<--")
            current = current.next
        print("None")
    def dequeue(self):
        first_node = self.head
        self.head = self.head.next
        first_node.next = None
        return first_node.data
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node.next = None
            current.next = new_node

Queue1 = Queue()
Queue1.enqueue(4)
Queue1.enqueue(73)
Queue1.enqueue(37)
Queue1.enqueue(2)
Queue1.enqueue(21)
Queue1.display()
print("before dequeue")
Queue1.dequeue()
print("after dequeue")
Queue1.display()
print("added 29")
Queue1.enqueue(29)
Queue1.display()
