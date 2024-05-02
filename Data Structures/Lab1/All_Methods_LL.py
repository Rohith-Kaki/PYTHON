class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_start(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.next = None

    def add_index(self,index,data):
        new_node = Node(data)
        if(index < 0):
            print("-ve index is not possible")
        if(index == 0):
            return self.add_start()
        current = self.head
        count = 0
        while current.next is not None and count < index -1:
            current = current.next
            count +=1
        new_node.next = current.next
        current.next = new_node

    def add_at_index_newmethod(self,index,data):
        new_node = Node(data)
        current = self.head
        prev = None
        count = 0
        while (count != index):
            prev = current
            current = current.next
            count += 1 
        new_node.next = current
        prev.next = new_node

    def after_head(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = "-->")
            current = current.next
        print("None")

    def delete_start(self):
        first_node = self.head
        self.head = self.head.next
        first_node.next = None
        return first_node.data

    def delete_index(self,index):
        if(index < 0):
            print("-ve index is not possible")
        if(index == 0):
            return self.delete_start()
        current = self.head
        prev = None
        count = 0
        while current.next is not None and count < index:
            prev = current
            current = current.next
            count += 1
        prev.next = current.next 
        current.next = None
        return current.data

    def delete_end(self):
        Last_node = self.head
        prev = None
        while Last_node.next is not None:
            prev = Last_node
            Last_node = Last_node.next
        if(prev == None):
            self.head = None
        else:
            prev.next = None
        return Last_node.data
    
    def reversal(self):
        next = None
        prev = None
        current = self.head  #Inplace of current you can also type self.head
        while current is not None:
            next = current.next 
            current.next = prev
            prev = current 
            current = next
        self.head = prev

        

    
ll1 = LinkedList()
print("After adding")
ll1.add_start(4)
ll1.add_start(7)
ll1.display()
ll1.delete_end()
ll1.display()
# print(ll1.delete_index(0))
# print(ll1.delete_start())
# print("After deleting")
