
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size
    
    def get_item(self, i):
        if i < 0 or i >= self.num:
            raise Exception("Invalid index")
        return self.Q[(self.first + i) % self.max_size]


# Example usage
q = Queue(10)
q.enqueue("ra'na")
q.enqueue("vez")
q.enqueue("Arya")
print("queue size is: ", q.size())
print(q.dequeue(), "left the queue")
print("front of queue is:", q.front())
q.enqueue("milda")
q.dequeue()
q.dequeue()
q.dequeue()

if q.size() > 1:
    print("Second item in the queue:", q.get_item(1))
else:
    print("There is no second item in the queue.")


