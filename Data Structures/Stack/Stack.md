A stack is a fundamental data structure in computer science that allows for the efficient storage and retrieval of
a collection of elements. It follows the Last-In-First-Out (LIFO) principle, which means that the last element added
to the stack is the first one to be removed. In other words, the most recently added element is always at the top of
the stack. The stack can be visualized as a stack of plates in a cafeteria. When you add a plate, you place it on top
of the stack. When you want to remove a plate, you remove the one on top first, since that's the one that was added
most recently. This analogy is useful in understanding the operations of a stack data structure.

The two primary operations supported by a stack are push and pop. The push operation adds an element to the top of
the stack, while the pop operation removes the top element from the stack. The peek operation is also supported,
which allows you to examine the top element without removing it.

In addition to the core operations, a stack may also support other operations such as isEmpty to check if the stack
is empty, size to determine the number of elements in the stack, and clear to remove all elements from the stack.

One of the key advantages of using a stack is its simplicity and efficiency. Because only the top element can be
accessed, the implementation can be optimized for fast insertions and deletions. Additionally, because the stack is
simple, it is easy to reason about and debug.

Stacks are used in a wide range of applications, including but not limited to:

1. Function Calls: Stacks are used to keep track of the order in which functions are called in a program. When a
   function is called, its parameters and return address are pushed onto the stack. When the function completes,
   its parameters and return address are popped from the stack.

2. Expression Evaluation: Stacks can be used to evaluate expressions, such as infix, postfix, and prefix
   expressions. In postfix notation, also known as Reverse Polish Notation (RPN), the operands are pushed onto the
   stack, and the operators are evaluated when encountered.

3. Memory Management: Stacks are used in memory management to allocate and deallocate memory dynamically. When
   memory is allocated, a block of memory is pushed onto the stack. When the memory is deallocated, the block of
   memory is popped from the stack.

Overall, a stack is a powerful data structure that is essential to many applications in computer science. Its
simplicity, efficiency, and ease of use make it a popular choice for many programmers.

<img style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 100%;" 
      src="..\..\Assets\Images\array_linkedlist_queue_stack_big_O.png" alt="hash table big O" width="700">
