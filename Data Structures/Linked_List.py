"""A linked list is a popular data structure in computer science and programming. It is a collection of nodes that
are linked together through pointers or references. Each node in the list contains two parts: the data and the
reference to the next node in the list. Linked lists come in different forms, but the most common ones are singly
linked lists, where each node has a reference to the next node in the list, and doubly linked lists, where each node
has references to both the next and previous nodes in the list.

Python is a popular programming language that has in-built support for linked lists. In this implementation of a
linked list in Python, we have defined a Node class that has two attributes: the data that the node contains and a
reference to the next node in the list. We also have a LinkedList class that contains several methods for
manipulating the linked list. These methods include adding a node to the list, removing a node from the list,
appending a node to the end of the list, sorting the list, merging two lists, reversing the list, and finding the
middle node of the list.

One advantage of linked lists is that they allow for efficient insertion and deletion of nodes, as the links between
the nodes can be easily modified. However, traversing a linked list can be slower compared to accessing elements in
an array, especially for large lists. This is because accessing a specific node in a linked list requires traversing
through all the nodes before it, while accessing an element in an array can be done in constant time.

Linked lists are commonly used in a variety of applications, including implementing dynamic data structures like
stacks, queues, and hash tables, as well as in graph algorithms and memory allocation in operating systems. They are
also used in computer science education to introduce students to data structures and algorithms.

In summary, this implementation of a linked list in Python provides a basic framework for manipulating linked lists.
While it may not be as efficient as other implementations or data structures for certain use cases, linked lists
remain a useful and versatile tool in the programmer's toolbox."""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_node(self, key):
        current_node = self.head
        if current_node and current_node.val == key:
            self.head = current_node.next
            current_node = None
            return
        while current_node:
            if current_node.val == key:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        curr = self.head
        while curr:
            ptr = curr.next
            while ptr:
                if curr.val > ptr.val:
                    curr.val, ptr.val = ptr.val, curr.val
                ptr = ptr.next
            curr = curr.next

    def merge(self, l2):
        if self.head is None:
            return l2.head
        if l2.head is None:
            return self.head
        curr1 = self.head
        curr2 = l2.head
        if curr1.val <= curr2.val:
            new_head = curr1
            curr1 = curr1.next
        else:
            new_head = curr2
            curr2 = curr2.next
        curr = new_head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        return new_head

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.val, end=" ")
            currentNode = currentNode.next




a = Node(4)
b = Node(9); a.next = b
c = Node(15); b.next = c
d = Node(6); c.next = d

myLinkedList = LinkedList(a)

# 4 -> 9 -> 15 -> 6

myLinkedList.append(100)

# 4 -> 9 -> 15 -> 6 -> 100

myLinkedList.remove_node(9)

# 4 -> 15 -> 6 -> 100

myLinkedList.printLinkedList()