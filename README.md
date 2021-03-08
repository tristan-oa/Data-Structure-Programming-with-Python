# Data Structures and Algorithm Programming using Python

In this project, different algorithms are implemented using the Python programming language for the [ICT1018: Data Structures and Algorithms](https://www.um.edu.mt/courses/studyunit/ICT1018) course, forming part of my BSc Computer Science.

# Task Breakdown

In this project, the following 12 tasks were implemented:

1.  Integer arrays are **randomly generated** and **sorted** using:

    - Shell Sort
    - Quick Sort

2.  The sorted pair of arrays from the previous task is **merged** in linear time.

3.  An integer array is **randomly generated** and any **extreme elements** are returned. <br>
    An element is considered extreme if:

    - it is not the first, nor the last element of its array AND
    - is either

      - less than its successor and predecessor OR
      - greater than its successor and predecessor

      Eg:

          A = [0, 5, 3, 6, 8, 7, 15, 9]
          extremePoints(A) -> 5, 3, 8, 7, 15

4.  An integer array is **randomly generated** and all **2-pairs of integers** are returned. <br>
    A 2-pair refers to any 2 distinct pairs of integers ((a,b),(c,d)) where a X b = c X d and a ≠ b ≠ c ≠ d.
5.  An ADT Stack is used to evaluate arithmetic expressions in RPN format. <br>
    Available Operands: **+**, **-**, **x**, and **/**.
6.  The **Sieve of Eratosthenes** algorithm is implemented and a given number is checked if it is **prime**.
7.  An unbalanced **BST** (Binary Search Tree) is built from user input and displayed.
8.  The **Newton-Raphson Method** is used to approximate the square root of a given number.
9.  An integer array is **randomly generated** and all **repeating integers** are returned in the fastest and most memory-efficient way possible.
10. An integer array is **randomly generated** and the **largest integer** is returned.
11. The first n terms of the **Maclaurin Series Expansion** are used to compute the:
    - **COSINE**
    - **SINE**
12. The sum of the first n terms of the **Fibonacci Sequence** are computed.

# Documentation

A report describing the design process and motivation behind this project can be found [here](https://github.com/tristan-oa/Python-DataStructures-Algorithms1-1st-year/blob/master/Assignment_SPECIFICATION.pdf).

A detailed technical documentation of the source code written can be found [here](https://github.com/tristan-oa/Python-DataStructures-Algorithms1-1st-year/blob/master/DOCUMENTATION.pdf).
