# dynamic queue implementation
class Queue(object):

    def __init__(self, limit =5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isempty(self):
        return self.size <= 0

    def enqueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0

        else:
            self.size += 1
            self.rear = self.size

        print("The queue after adding %s" %self.que)

    def dequeue(self):
        if self.size <= 0:
            print('queue is empty')
            return 0

        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size
            print("The queue after deleting %s" %self.que)

    def queue_rear(self):
        if self.rear is None:
            print("queue is empty")

        else:
            return self.que[self.rear]

    def queue_front(self):
        if self.front is None:
            print("queue is empty")

        else:
            return self.que[self.front]

    def size(self):
        return self.size

    def resize(self):
        newque = list(self.que)
        self.limit = 2*self.limit
        self.que = newque

que = Queue()
que.enqueue("first")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.enqueue("second")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.enqueue("third")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.enqueue("fourth")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.enqueue("fifth")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.enqueue("sixth")
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.dequeue()
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())
que.dequeue()
print("The element in front side of a queue is %s" %que.queue_front())
print("The element in rear side of the queue is %s" %que.queue_rear())

# one of the way to implement the queue(FIFO)