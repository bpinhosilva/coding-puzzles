# Knapsack 0/1 Problem

## Description

The Knapsack 0/1 problem is a classic problem in combinatorial optimization. Given a set of items, each with a weight
and a value, determine the number of each item to include in a collection so that the total weight is less than or equal
to a given limit and the total value is as large as possible. In the 0/1 knapsack problem, each item can either be
included or excluded from the knapsack (hence the name 0/1).

## Problem Statement

You are given:

- A list of values `v` where `v[i]` is the value of the `i-th` item.
- A list of weights `w` where `w[i]` is the weight of the `i-th` item.
- An integer `n` representing the number of items.
- An integer `capacity` representing the maximum weight capacity of the knapsack.

The goal is to maximize the total value of the items in the knapsack without exceeding the weight capacity.

* m[0, w] = 0
* m[i, w] = m[i - 1, w] if w[i] > w
* m[i, w] = max(m[i - 1, w], m[i - 1, w - w[i]] + v[i]) if w[i] <= w
* The solution can be found at m[n, capacity]

## Example

Consider the following example:

- Values: `[5, 4, 3, 2]`
- Weights: `[4, 3, 2, 1]`
- Number of items: `4`
- Capacity: `6`

The optimal solution is to include the items with values `4`, `3` and `2`, resulting in a total value of `9` and a total
weight of `6`.

## Dynamic Programming Solution

The dynamic programming approach to solve the 0/1 knapsack problem involves creating a 2D array `m` where `m[i][j]`
represents the maximum value that can be obtained with the first `i` items and a knapsack capacity of `j`.

The solution can be built using the following steps:

1. Initialize a 2D array `m` with dimensions `(n+1) x (capacity+1)` filled with zeros.
2. Iterate through each item and each capacity, updating the array based on whether the current item is included or
   excluded.
3. The value at `m[n][capacity]` will be the maximum value that can be obtained.

## Usage

The provided Python code implements the dynamic programming solution for the 0/1 knapsack problem. It includes a
`Solution` class with a `solve` method and a `TestSolution` class for unit testing.

To run the tests, execute the following command:

```bash
python3 knapsack_0_1.py
```

This will run the unit tests and verify the correctness of the solution.
