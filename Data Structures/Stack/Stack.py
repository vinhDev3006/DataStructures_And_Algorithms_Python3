class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Added {item} to the stack.")

    def pop(self):
        item = self.items.pop()
        print(f"Removed {item} from the stack.")
        return item

    def is_empty(self):
        empty = len(self.items) == 0
        print(f"The stack is{' ' if empty else ' not '}empty.")
        return empty

    def size(self):
        size = len(self.items)
        print(f"The size of the stack is {size}.")
        return size

    def peek(self):
        if self.is_empty():
            return None
        item = self.items[-1]
        print(f"The top item on the stack is {item}.")
        return item



s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.peek()
s.pop()
s.size()
s.is_empty()

