# Dynamic Array and Linked List Comparison Assignment

## Overview

This Python assignment compares different strategies for dynamic array resizing while storing words from the **Open English Word List (EOWL)** dataset. The goal is to investigate the trade-offs between various array resizing techniques, analyze time and space complexities, and compare the performance of custom dynamic arrays with Python's built-in list implementation.

The assignment covers:
1. Different resizing strategies (Incremental, Doubling, Fibonacci).
2. Inserting words using binary search to keep the array sorted.
3. Measuring the time and space complexity for each resizing strategy.
4. Comparing these strategies to Python's built-in list (ArrayList) implementation.

## Problem Specification

Data structures such as arrays and linked lists have different performance characteristics. In this assignment, we:
1. Load the **Open English Word List (EOWL)**.
2. Store the words in a dynamic array using three different resizing strategies.
3. Insert words in a sorted manner using binary search.
4. Measure the time for each insertion and array resize.
5. Theoretical analysis of time and space complexity for each strategy.
6. Empirical analysis of the same.
7. Comparison of the results with Python's built-in list.

## Resizing Strategies

The following resizing strategies are implemented:
- **Strategy A (Incremental Growth)**: The array size increases by 10 every time it becomes full.
- **Strategy B (Doubling Growth)**: The array size is doubled when it becomes full.
- **Strategy C (Fibonacci Growth)**: The array size increases according to the Fibonacci sequence when it becomes full.

## Program Details

The program is structured to:
1. Load words from the EOWL dataset.
2. Insert words using binary search into a dynamic array.
3. Dynamically resize the array based on the chosen strategy.
4. Measure time taken for insertion and track space usage.
5. Compare the performance of custom dynamic arrays with Python's built-in list.

### Theoretical Complexity Analysis
- **Time Complexity**:
  - Inserting an element with binary search takes \(O(\log n)\) to find the position and \(O(n)\) to shift elements, leading to \(O(n)\) for insertion.
  - Resizing strategies have the following complexity:
    - **Strategy A (Incremental Growth)**: Frequent resizing results in \(O(n^2)\) time over all insertions.
    - **Strategy B (Doubling Growth)**: Resizing occurs less frequently, leading to \(O(n \log n)\) time.
    - **Strategy C (Fibonacci Growth)**: Resizing behaves similarly to Strategy B, with an amortized \(O(1)\) time for resizing.
- **Space Complexity**:
  - The space used increases according to the selected strategy.

### Empirical Complexity Analysis
- The program measures the actual time and space usage of each strategy using Python’s `time` and `sys.getsizeof()` functions.

## Instructions to Run the Program

### Prerequisites
- **Python 3.x** installed on your system.
- The **Open English Word List (EOWL)** dataset (you can download it from the [EOWL GitHub repository](https://github.com/dwyl/english-words)).

### Clone the repository 
- https://github.com/srivalya2909/Prog_For_Grad
