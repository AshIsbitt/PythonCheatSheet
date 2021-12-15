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


