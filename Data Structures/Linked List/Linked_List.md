A linked list is a popular data structure in computer science and programming. It is a collection of nodes that
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

<img style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 100%;" 
      src="..\..\Assets\Images\array_linkedlist_queue_stack_big_O.png" alt="hash table big O" width="700">

Linked lists are commonly used in a variety of applications, including implementing dynamic data structures like
stacks, queues, and hash tables, as well as in graph algorithms and memory allocation in operating systems. They are
also used in computer science education to introduce students to data structures and algorithms.

In summary, this implementation of a linked list in Python provides a basic framework for manipulating linked lists.
While it may not be as efficient as other implementations or data structures for certain use cases, linked lists
remain a useful and versatile tool in the programmer's toolbox.
