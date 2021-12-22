# MIT Introduction to Algorithms 6006

_intro here_

### L1: Algorithms and Computation
This is about solving computational problems
Communicating your solution is efficient
Prove correctness

In general - communcation of ideas

What is a computational problem? What is an algorithm?
    - (Abstractly) - A set of inputs, a set of outputs, and the relation between the two
    - We specify some kind of predicate (black box testing - inputs and outputs)

General problems that have an arbitrarily sized inputs
    - A fixed size of data that we can use in the input

algorithm is different to a problem, the latter is when we don't know what the outputs are, but we can use to generate a correct output with a set of inputs
A function that takes inputs and maps them to outputs

To check if every student in the room has the same birth hour:
    - Maintain a record of birthdays
    - interview students in an order
        - check if birthday is already in order
            - if so, return the birthdays
        - otherwise add to record
    - otherwise, return none

A constantly sized piece of code that can work with any length of inputs
    - Recursion
    - Induction - a method of mathematical proof typically used to establish a given statement for all numbers
    - Looping

Inductive hypothesis:
    if first k students contain a match, algorithm returns a match before interviewing student k+1

    Base case:
        k = 0
            This certainly works
            This is the smallest possible case of data

            if K contains a match -> already returned by induction 
            else -> if k + 1 contains a match; algorithm checks all possibilities

            
            This is basically a brute force method

The end goal is to be able to write a set of instructions that another programmer could take and write some code for

    Efficiency for above hypothesis
        Not only how fast does this run, but how fast it runs compared to other methods

        The biggest issue in measuring how long this takes on any specific hardware is the strength of said hardware

            How many fixed operations does a computer take to solve the problem
            We don't measure time, but the number of fundamental operations

        Asymtotic analysis is the method of measuring the efficiency using the above method
        Performance is expected to depend on size of the input data
        (n) is usually how we represent the data size, although not always
            IE a 2d array would be (n^2)

        Big O Notation - this refers to the upper bounds
        Omega - lower bounds
        theta - both

            linear algorithm - linear time, like adding something to the middle of the list and moving everything to the end

            constant time - no matter on the length of the input, this is the same
            logorithmic time
            theta(n) - linear
            theta(n log n) - log linear
            theta (n^2) - quadratic running time
            theta(nc) - polynomial time (c is a constant) <- This is the most efficient (in this instance)

            2 ^ theta(n) - exponential time, this is bad.


        We need to define a model of computation for what our computer can do in a constant time
            This is a model of computation

            MIT uses a "Word-RAM" method - a word is how many bytes of data a cpu can hold at any one time
                                        -   This is the 64 bits of data that can be addressed at any one time
                                        - On a 32bit system, at most you can access 4gb of data at a single time
                                        - In a 64bit system, that's abut 20exabytes

            
First 8 lectures are going to be data structures
    - This is going to be about storing large amounts of data and operating on that data
Second 8 is on Shortest path Algorithms and graphs
Third 8 lectures are dynamic programming


### L2: Data Structures and Dynamic Arrays
Interface (API/ADT) vs Data Structure
What you want to do vs how you do it

Interface
 - specification
 - what data can store
- What you can do with the data (what operations you can do on it)
- A problem statement

 structures
 - representation
 - how to store data
 - This gives you algorithms to support those operations
  - a solution to that problem


 2 main interfaces and special cases of them

- Sets
- Sequences

2 main data structure tools/approaches
- Arrays
- pointer-based/linked data structures

Sequences
    Static squence interface
        Number of items doesnt change, but the actual items might
            - build(n) - build the data structure of size n
            - len() - return the number of items (n)
            - iter_sequence - output the items in the current order
            - get(i) - get any single item
            - set(i, x) - set item i to value x

        In python this is a list (kinda). In general, this is called a static array

"Array" - just means a concecutive chunk of memory 
You can get and set parts of an array in constant time
length is constant time
build/iter_sequence are in linear time

This is the memory allocation model
    Assume you can allocate an array of size n in theta(n) time


    Dynamic Sequences
        insert_at(i, x) - insert value i at location x
        delete_at(i) - delete item at location i and move every item left 1


    Linked list
        Store items in a bunch of nodes in memory
        Each node has an item in it and "next" field
            Think of these as OOP classes/objects with 2 attrs
            the "item" field has the item in the Sequence
            the "next" pointer points to the next item anywhere in memory

            The DS is represented by "head" and "length"

        This is a pointer-based list, as each item of data is an array of size 2 in RAM
        The list is in the CPU and uses pointers to point to each array
            (thats the next field - the pointer to the next item in the list)

    
Dynamic sequence operations
    Static array
    - Insert and delete anywhere costs theta(n) time
        - shifting items along, deleting and writing each item again
        - Changing the length of the array means creating a whole new static array of different size

    Linked list
    - Insert/delete at item 0 are constant time
    - Everything else is slow
        - Accessing the ith item takes theta(i) time
            - at worst, thena(n) for the final item
    
    - A doubly-linked list will also store a "tail", storing a pointer to the last item
        - This is called DS augmentation, adding extra data to the structure, but it needs to be kept up to date

    Dynamic arrays (Python lists)
        - Relax constraint size(array) = n
        - Insetad of setting an exact size, we make an array a rough size
            - How roughly is up for debate
            - This means usually throwing away constant factors
        - size of the array is theta(n) 
            - at most, a constant * n

        They create the sequence and then leave some blank items at the end
            - current length is now stored in the DS too 
            - length <= size, or we're overflowing

            If the size is bigger than the length, the dynamic array is rebuilt to be bigger 
            Deciding on the factor to increase the array size is complicated

        
Amortization:
    Operation takes T(n) amortized time if any k operations take at most k t(n) time


### Problem Session 1
First problem has 3 functions and you have to order them based on Asymtotic complexity

Asymptotics = How does the function look disregarding what n is actually equal to
    how does it act with stupid large numbers (IE, assume n=1bn and then see what's basically a rounding error at that point)

Amortized - (in terms of a data structure) - If I have an operation, the definition of it running in amortized K time, if I do N operations, it'll never take more than N*K time. 
    

