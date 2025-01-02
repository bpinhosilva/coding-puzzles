## Table of Contents

1. [Description](#description)
2. [Properties](#properties)
3. [Applications](#applications)
4. [Example](#example)

# Binary Search Tree

## Description

A Binary Search Tree (BST) is a data structure that facilitates fast lookup, addition, and deletion of items. It
maintains a sorted order of elements, which allows for efficient binary search operations.

## Properties

1. **Node Structure**:
    - Each node contains a key (value), a reference to the left child, and a reference to the right child.

2. **Binary Tree**:
    - Each node has at most two children.

3. **Ordering**:
    - For any given node, all values in the left subtree are less than the node's value, and all values in the right
      subtree are greater than the node's value.

4. **Operations**:
    - **Insertion**: Adding a new node while maintaining the BST property.
    - **Deletion**: Removing a node and reorganizing the tree to maintain the BST property.
    - **Search**: Finding a node with a specific value.
    - **Traversal**: Visiting all nodes in a specific order (in-order, pre-order, post-order).

5. **Time Complexity**:
    - **Average Case**: O(log n) for search, insertion, and deletion.
    - **Worst Case**: O(n) for search, insertion, and deletion (when the tree becomes unbalanced).

6. **Space Complexity**:
    - O(n) for storing n nodes.

## Applications

- **Searching**: Efficiently finding elements.
- **Sorting**: In-order traversal of a BST results in sorted order of elements.
- **Dynamic Set Operations**: Insertion, deletion, and lookup operations.

## Example

Here is a simple example of a BST:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

In this example:

- The root node is 8.
- The left subtree of 8 contains nodes with values less than 8.
- The right subtree of 8 contains nodes with values greater than 8.


