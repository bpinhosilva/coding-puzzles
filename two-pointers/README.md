# Table of Contents

1. [Two-Pointers Technique](#two-pointers-technique)
2. [Key Concepts](#key-concepts)
3. [Common Use Cases](#common-use-cases)
4. [Remarks](#remarks)
5. [Advantages](#advantages)
6. [Limitations](#limitations)

## Two-Pointers Technique

The two-pointers technique is a common algorithmic approach used to solve problems involving arrays or linked lists. It
involves using two pointers to iterate through the data structure, often from different ends or at different speeds, to
achieve a specific goal. This technique is particularly useful for problems that require finding pairs, triplets, or
sub-arrays that meet certain conditions.

## Key Concepts

1. **Initialization**: Two pointers are initialized, typically at the start and end of the array or list.
2. **Movement**: The pointers are moved towards each other or in a specific pattern based on the problem's requirements.
3. **Condition Checking**: At each step, the values at the pointers are checked against the problem's conditions.
4. **Termination**: The process continues until the pointers meet or cross each other, or until the desired condition is
   met.

## Common Use Cases

- **Finding Pairs**: Identifying pairs of elements that sum up to a specific target.
- **Removing Duplicates**: Removing duplicate elements from a sorted array.
- **Partitioning**: Partitioning an array around a pivot element.
- **Palindrome Checking**: Checking if a string is a palindrome by comparing characters from both ends.

## Remarks

- [Remove n-th node from end of list](remove_nth_node_from_end_of_list.py): demonstrates moving the right pointer n
  steps ahead to position the left pointer correctly (right before the n-th item) for node removal.

## Advantages

- **Efficiency**: Often reduces the time complexity compared to brute-force solutions.
- **Simplicity**: Easy to implement and understand for many problems.

## Limitations

- **Sorted Data**: Many problems require the data to be sorted, which may add preprocessing time.
- **Specific Use Cases**: Not all problems can be solved using this technique.

The two-pointers technique is a powerful tool in a programmer's arsenal, especially for solving problems involving
arrays and linked lists efficiently.

