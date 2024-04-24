maxsize = 6
Array = [0]*maxsize
front = 0
rear = -1
itemcount = 0

def peek():
    return Array[front]
def isfull():
    return itemcount == maxsize
def isempty():
    return itemcount == 0
def size():
    return itemcount
def insert(data):
    global rear, itemcount
    if not isfull():
        if rear == maxsize-1:
            rear = -1
        rear += 1
        Array[rear]= data
        itemcount += 1
def dequeue():
    global rear, itemcount
    data = Array[front]
    if front == maxsize -1:
        front = 0
    else:
        front += 1
        itemcount -=1
        return data
    
insert(47)
insert(44)
insert(30)
insert(43)
insert(33)
insert(31)
print("Queue Size:", size())
print("Queue:")
for i in range(maxsize):
    print(Array[i], end=" ")
if isfull():
    print("\nQueue is full!")
print("Element at fornt", peek())
