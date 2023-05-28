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
