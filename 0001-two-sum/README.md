# LeetCode 1 - Two Sum

## Problem

Given an integer array `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that:

* Exactly one valid solution exists.
* The same element cannot be used twice.
* The answer can be returned in any order.

---

## Examples

### Example 1

**Input**

```text
nums = [2,7,11,15], target = 9
```

**Output**

```text
[0,1]
```

**Explanation**

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

### Example 2

**Input**

```text
nums = [3,2,4], target = 6
```

**Output**

```text
[1,2]
```

---

### Example 3

**Input**

```text
nums = [3,3], target = 6
```

**Output**

```text
[0,1]
```

---

## Approach

* Create an empty hash map (dictionary).
* Traverse the array once.
* For each element, calculate the required value (`target - current number`).
* Check if the required value already exists in the hash map.

  * If it exists, return the indices.
  * Otherwise, store the current number and its index in the hash map.
* Since the problem guarantees exactly one solution, the answer will always be found.

---

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[n] = i
```

---

## Explanation

The hash map stores each number along with its index.

For every number:

1. Calculate the complement (`target - current number`).
2. Check if the complement has already been seen.
3. If yes, return both indices.
4. Otherwise, store the current number and continue.

This allows us to find the answer in a single traversal of the array.

---

## Time Complexity

```text
O(n)
```

The array is traversed only once.

---

## Space Complexity

```text
O(n)
```

The hash map stores at most `n` elements.

---

## Concepts Used

* Hash Map (Dictionary)
* Array Traversal
* One-Pass Algorithm
* Enumeration

---

## Author

**Ramit Sarker**
