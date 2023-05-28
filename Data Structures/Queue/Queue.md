A queue is a fundamental data structure in computer science that is used to store a collection of elements. A
queue operates on a first-in, first-out (FIFO) basis, meaning that the first element added to the queue will be the first one to be removed.

Queues are commonly used in programming for implementing algorithms that require processing elements in a specific
order, such as breadth-first search or in simulations where events occur in a specific order. They are also used for
managing resources in operating systems, such as scheduling processes to be executed by a processor.

In a queue, elements are added to the back (also known as the "tail") of the queue and removed from the front (also
known as the "head") of the queue. This ensures that elements are processed in the order they were added to the
queue, and that newer elements are processed after older ones.

There are several common operations that can be performed on a queue, including:

- Enqueue: Adding an element to the back of the queue
- Dequeue: Removing and returning the element at the front of the queue
- Peek: Returning the element at the front of the queue without removing it
- Size: Returning the number of elements currently in the queue

Queues can be implemented using various data structures, such as arrays, linked lists, or circular buffers.
The choice of data structure depends on the specific requirements of the application, such as the need for
constant-time enqueue and dequeue operations or the amount of memory available.

<img style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 100%;" 
      src="..\..\Assets\Images\array_linkedlist_queue_stack_big_O.png" alt="hash table big O" width="700">
