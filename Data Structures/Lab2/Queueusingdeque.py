from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.popleft()
        else:
            print("isempty")
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())