"""
A queue is a fundamental data structure in computer science that is used to store a collection of elements. A 
queue operates on a first-in, first-out (FIFO) basis, meaning that the first element added to the queue will be the 
first one to be removed.

Queues are commonly used in programming for implementing algorithms that require processing elements in a specific 
order, such as breadth-first search or in simulations where events occur in a specific order. They are also used for 
managing resources in operating systems, such as scheduling processes to be executed by a processor.

In a queue, elements are added to the back (also known as the "tail") of the queue and removed from the front (also 
known as the "head") of the queue. This ensures that elements are processed in the order they were added to the 
queue, and that newer elements are processed after older ones.

There are several common operations that can be performed on a queue, including:
    Enqueue: Adding an element to the back of the queue 
    Dequeue: Removing and returning the element at the front of the queue 
    Peek: Returning the element at the front of the queue without removing it 
    Size: Returning the number of elements currently in the queue 

Queues can be implemented using various data structures, such as arrays, linked lists, or circular buffers. 
The choice of data structure depends on the specific requirements of the application, such as the need for 
constant-time enqueue and dequeue operations or the amount of memory available.
"""


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.head
        out = ""
        while current:
            out += str(current.data) + " "
            current = current.next
        return out.rstrip()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(len(q))
print(q.peek())
q.dequeue()
print(q)
print(len(q))
