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
    
### Sets and Sorting

Sets are one type of data interface - you can keep adding items to it and query them.
They're containers with the following operations 
    - build(A)
    - len
    
    - find(k)

    - insert(x)
    - delete(k)

Sets are python lists
Every operation should take linear time

destructive - overwrites the input array
In place - uses O(1) extra space
    - IE think of a variable holding a loop counter

Selection sort
    Take the highest number and stick it at the end
    Every number is before the highest

    loop through this process
    (an array of length 1 is already in sorted order)

    ```py
    def prefix_max(A, i):
        '''return index of maximum in A[:i + 1]'''
        if i > 0:
            j = prefix_max(A, i = 1)
            if A[i] < A[j]:
                return j
        return i
    ```

    This isn't the best way to do this, it's more theoretical, but it's a good example

Merge Sort
    Take every pair of numbers, and sort those pairs
    Then take every 2 pairs together (4 numbers)
    Sort those
    recurse this until you're back to 1 list

    When you're at exactly 2 lists, you basically loop throguh both from the end and see which numbers are bigger

    ```py
    def merge_sort(A, a=0, b=None):
        '''sort A[A:B]'''
        if b is None: 
            b = len(A)

        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            L, R = A[a:c], A[c:b]
            merge(L, R, A, len(L), len(R), a, b)

            # read "c" as meaning "centre"
    ```



# L4 - Hashing
- Prove that you cant find (k) faster than O(log n)
- Show how to find (k) faster thann O(log n)

Two types of sets already
    - Array - everything in O(n)
    - Sorted Array
        - build O(n log n)
        - find(k) O(log n)
        - Insert O(n)
        - Delete O(n)
        - Find min/max O(1)
        - Find prev/next O(log n)

Today's focus - the static find. (Can it be faster than log n)
Make insert/delete faster than O(n), make them dynamic

Comparison model - why we can't do faster than log n for find
    The items being stored can be thought of as black boxes
    Until I have to check between them and use a key to compare them

    Most of the algorithms we've seen so far are comparison algorithms
    We can do all the basic comparison forms on This
        They all boil down to "this statement is true or false"

    This can be easily represented by a binary tree - each node is a computation we can make
        - "How many leaves can this tree have?"
            n + 1
        Longest path = height of the tree
        What is the height of the tree?
            min height = at least log(n) height (theta (log n))
            This maens we have to use log time to see if a value is in the set

    If I have an item that has key 10, and i'm going to have an array storing This
    in the array at location 9 (the 10th location)
        This is a direct access array

        finding and inserting are all at constant time
        searching/sorting is based

Direct Access Arrays
    - build - u
    - find - linear
    - insert/delete - linear
    - find min/max - u
    - find prev/next - u

    (See u as the size of the largest key we can store)

    This is a set data structure

You can take a set/sequence and implement a sequence/set, they just wont have particularly well implemented

to get this to run in constant time, u < 2^w (where w is the "word" your CPU can take)
If we have a number of keys u but want to store it in a DAA of size m (which is theta(n))
    The length of the keys u need to be mapped in a range 0 - m-1
    We can map it down using a function, somehow

    The problem is that we may have to store multiple pieces of data at one index location in the DAA
    if u is n^2, we'll end up with the nth space in DAA holding n items, so it's not that good
    This is called a collision

    1 solution
        if m is greater than n, just stick the second hashed item there to avoid a collision
        This is called open addressing
        Python uses this method
        This is notoriously difficult to analyse

    2nd solution
        Instead of storing the hashed data in the hash table
        we store the key and then add a pointer to another data structure

        This is an idea called chaining, pointing from one DS to anther
        usually this uses a linked list, but you can use anything you want

At initialisation, a hash table is an empty data structure
Picking a good hash function
    - Any good function is going to encounter collisions anyway
    - Simplest method is just to use modulus
        - This is called the division method
        - Take a key and set it to k % m so it wraps around the hash table
        - This is basically what python does

    - Use a non-deterministic hash function 
        - Don't pick a single hash function at start, pick a random one at rumtime

Universal hash function
    - 'universal' is a descriptor, there are many functions that could be described as universal

    h a b(k) = (((a k + b)mod p) mod m)
    H(p, m) = {h a b(k) | a, b...

    Univerality - probability of any specific hash function key colliding with another key
                    is less than/equal to 1/m for any different two keys in my universe

Indicator random variable
    Var with some probability = 1
    1 - probability == 0

    Xij is a var over choice in the hash function
    Xij == 1 if h(ki) = h(kj) (IE if they collide), otherwise it's 0

    Size of the chain at h(ki) in the hash table == Xi == sum j/0 over u-1 of Xij

    expected value of this chain length over random choice
        heH{Xi} = (choosing a hash value from this family of the length of the chain)

### Problem Set 2
Master theorem - T(n) = a T(n/b) + f(n)
This is basically a way to explain what you do with a binary tree
f(n) = O(n^logb of a - epsilon) for any positive epsilon
(This is only an upper bound)

There are two other function formulae here that I didn't copy down. They're all to do with calculating how fast a recursive problem is
It'll come out if you google it

Binary searching of an unknown length data set
- go to item 2i from i=0
- until k <= 2i
- This takes log(k) time

2^i-1 <= k <= 2i

Now I have an upper bound, then I can binary search

### L5: Linear sorting

Hash tabke
    - build n(e)
    - find log(e)
    - insert/delete log(e)
    - find min/max n
    - find prev/next n

Python dicts/sets are rebuilt with amortized bounds when new space is needed
If I know that all my keys are unique, I don't have ot check the whole table

Sorting algorithms
    insertion sort
        - time O(n^2)
        - in-place - yes
        - stable - yes
        - comments - O(nk) for k-proximate

    selection sort
        - time O(n^2)
        - in-place - yes
        - stable - No
        - comments - O(n) swaps

    merge sort
        - time O(n log n)
        - in-place - no
        - stable - yes
        - comments - stable, optimal comparison

Comparison model
    Some comparisons happen
    They branch in a binary sense (it can be generalised)
    At least n+1 outputs
    Height must be (log n)
    
What is the output of a sorting algorithm
    - A list

How do I sort a list of tuples, where each tuple is a representation of a number in 
base n (if n is 5, 17 is (3, 2) because 3x5 + 2 == 17)
    This is basically k div n and k mod n

    Tuple sorting
        Turn them into base 5 ints ((3,2) becomes 32) and sort them like that
        In the case of ties, you want the more significant value to take preference, so you do it last

        Counting sort
            Create a Direct Access Array
            At each key K we store a pointer to a chain
                We need a sequence data structure at K

            We add items to the end of teh sequence and when it adds to the DAA

            0  1  2  3  4
            =============
            03
                22
                    32
                        42
                        44

            This takes O(n+u) where u is the size of the sequence
            You make sure that you sort the tuples by the most significant bit first, then create the sequence above

    
### L6: Binary Trees part 1
Binary tree and traversal order
subtree ops: first, successor, insert, delete
set binary tree (binary search tree)
sequence binary tree via via subtree-size algorithm

efficient == logorithmic

Binary trees let us represent a sorted order of items dynamically

Any node (x) will have a parent pointer, a left child, and a right child
It will also contain an item
There's a single unique nood with no parent, the root node

            A
        B       C
    D       E
F

The subtree of a node is everything below the node/all the descendants
Depth of the node is the number of its ancestors/all the above nodes
The height is how many paths downward from the node
    B is height 2, A is height 3, C is 0

Traversal order
F, D, B, E, A, C
For every node, nodes in x.left are before x
nodes in x.right are after x

If I want to iterate all the nodes within a subtree
    I just iterate through the left, then output x, then output the right

That's for sequences ^^
For sets, you just take the sorted order

Playing aroudn with traversal order/Traversal operations
    Subtree.first(n)
        - given n, this creates a subtree and calculates what comes first in traversal order
        - Go left as much as possible
            node = node.left
    
    successor node
        next after node in tree's traversal order
        - If node.right: return subtree.First
        - else walk up the tree until we go up and left branch

    Both of these are in O(h) where h is the height of the tree

    subtree.insert_after(n, new)
        In traversal order, add new after item n

            If there's no right child, put new there
            else, put new as successsor(n),left

    subtree.delete(n)
        if n is a leaf, detatch from parent
        else if node.left exists
            swap node with predeccessor
            recursively delete predeccessor


### Binary trees PT 2
AVL trees are "height balance" trees.

Set binary trees == binary search trees


Sequence binary trees
    traversal order = sequence order
    
    size(node) = number of nodes in subtree(node)

    subtree augmentation
        each node can stoore a constant number of extra fields/properties
        subtree properties are things that can be computed from properties of the children


