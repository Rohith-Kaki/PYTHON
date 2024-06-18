class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [0]*size
        self.rear = self.front = 0
    def isEmpty(self):
        return self.rear == self.front
    def isFull(self):
        return self.rear == self.size
    def enqueue(self,item):
        if not self.isFull():
            self.queue[self.rear] = item
            self.rear += 1
        else:
            print("fulled")
    def dequeue(self):
        if not self.isEmpty():
            item = self.queue.pop(self.front)
            self.rear -= 1
            return item
        else:
            print("empty")
    def display(self):
        if not self.isEmpty():
            for i in self.queue:
                print(i, end = "<---")
            print("none")
        else:
            print("queue is empty")
    def peek(self):
        return self.queue[self.front]
    
if __name__ == "__main__":
     q = Queue(10)
     q.enqueue(10)
     q.enqueue(20)
     q.enqueue(30)
     q.enqueue(40)
     q.enqueue(50)
     q.enqueue(60)
     q.enqueue(70)
     q.display()
     print(q.dequeue())
     q.display()
     print(q.dequeue())
     print(q.dequeue())
     print(q.dequeue())
     print(q.dequeue())
     print(q.dequeue())
     print(q.dequeue())
     q.enqueue(4)
     q.display()


