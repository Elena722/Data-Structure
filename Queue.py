'''The Queue module implements multi-producer, multi-consumer queues. It is especially useful in
threaded programming when information must be exchanged safely between multiple threads. There are three
types of queues provides by queue module,Which are as following : 1. Queue 2. LifoQueue 3. PriorityQueue Exception
which could be come: 1. Full (queue overflow) 2. Empty (queue underflow)'''

# 1) simple example
print('---1-simple example----')
from queue import Queue

question_queue = Queue()
for x in range(1, 10):
    temp_dict = ('key', x)
    question_queue.put(temp_dict)
while(not question_queue.empty()):
    item = question_queue.get()
    print(str(item))

# 2) Create Queue
class Queue:
    def __init__(self):
        self.__queue = []

    def push(self, v):
        self.__queue.append(v)

    def pop(self):
        return self.__queue.pop(0)

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        return self.__queue == []


q = Queue()
print(f"The queue is empty - {q.is_empty()}")
q.push("first")
q.push("second")
print(f"The queue is empty - {q.is_empty()}")
print(f"Queue size - {len(q)}")
print(q.pop())
print(q.pop())
print(f"The queue is empty - {q.is_empty()}")