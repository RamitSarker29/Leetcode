# LeetCode 904 - Fruit Into Baskets

## Problem

You are given an integer array `fruits`, where each element represents the type of fruit produced by a tree.

You have **two baskets**, and each basket can hold **only one type of fruit**.

You can:

- Start from **any tree**.
- Move **only to the right**.
- Pick **exactly one fruit** from every tree.
- Stop as soon as you encounter a fruit that cannot fit into either basket.

Return the **maximum number of fruits** you can collect.

---

## Examples

### Example 1

**Input**

```text
fruits = [1,2,1]
```

**Output**

```text
3
```

**Explanation**

Pick all the fruits.

```text
1 2 1
```

Only two fruit types (`1` and `2`) are present.

---

### Example 2

**Input**

```text
fruits = [0,1,2,2]
```

**Output**

```text
3
```

**Explanation**

The longest valid subarray is

```text
1 2 2
```

It contains only two fruit types.

---

### Example 3

**Input**

```text
fruits = [1,2,3,2,2]
```

**Output**

```text
4
```

**Explanation**

The longest valid subarray is

```text
2 3 2 2
```

It contains exactly two fruit types.

---

## Approach

This is a **Variable Size Sliding Window** problem.

The goal is to find the **longest contiguous subarray containing at most two distinct fruit types**.

Use:

- Two pointers (`i` and `j`) to represent the current window.
- A hash map to store the frequency of each fruit type inside the window.

### Algorithm

1. Expand the window by moving the right pointer.
2. Add the current fruit to the hash map.
3. If the number of distinct fruit types becomes greater than `2`, shrink the window from the left until it becomes valid.
4. Once the window contains at most `2` distinct fruit types, update the answer.
5. Continue until the end of the array.

---

## Code

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        max_fruit = 0
        hash_map = {}

        for j in range(len(fruits)):
            if fruits[j] in hash_map:
                hash_map[fruits[j]] += 1
            else:
                hash_map[fruits[j]] = 1

            while len(hash_map) > 2:
                hash_map[fruits[i]] -= 1

                if hash_map[fruits[i]] == 0:
                    del hash_map[fruits[i]]

                i += 1

            max_fruit = max(max_fruit, j - i + 1)

        return max_fruit
```

---

## Explanation

### Step 1

Initialize:

```python
i = 0
hash_map = {}
max_fruit = 0
```

- `i` → Left pointer
- `j` → Right pointer
- `hash_map` → Stores fruit frequencies
- `max_fruit` → Stores the maximum fruits collected

---

### Step 2

Expand the window.

```python
for j in range(len(fruits)):
```

The right pointer moves one step at a time.

---

### Step 3

Add the current fruit.

```python
if fruits[j] in hash_map:
    hash_map[fruits[j]] += 1
else:
    hash_map[fruits[j]] = 1
```

Example:

```text
Window

1 2 1

Hash Map

{
1:2,
2:1
}
```

---

### Step 4

If more than two fruit types exist,

```python
while len(hash_map) > 2:
```

shrink the window.

Decrease the frequency of the left fruit.

```python
hash_map[fruits[i]] -= 1
```

If its frequency becomes zero,

```python
del hash_map[fruits[i]]
```

remove it from the hash map.

Move the left pointer.

```python
i += 1
```

Repeat until only two fruit types remain.

---

### Step 5

After shrinking,

the window is always valid.

Update the answer.

```python
max_fruit = max(max_fruit, j - i + 1)
```

---

## Dry Run

### Input

```text
fruits = [1,2,3,2,2]
```

| Window | Distinct Fruits | Valid | Max Fruits |
|--------|-----------------|:-----:|-----------:|
| 1 | 1 | ✅ | 1 |
| 1 2 | 2 | ✅ | 2 |
| 1 2 3 | 3 | ❌ | Shrink |
| 2 3 | 2 | ✅ | 2 |
| 2 3 2 | 2 | ✅ | 3 |
| 2 3 2 2 | 2 | ✅ | 4 |

Final Answer:

```text
4
```

---

## Time Complexity

```text
O(n)
```

Each fruit enters and leaves the sliding window at most once.

---

## Space Complexity

```text
O(1)
```

At most three fruit types are stored in the hash map before shrinking.

Since the number of basket types is bounded by a constant, the auxiliary space is **O(1)**.

---

## Concepts Used

- Sliding Window
- Variable Size Window
- Two Pointers
- Hash Map
- Frequency Counting

---

## Python Features Used

### Dictionary

```python
hash_map = {}
```

Stores fruit frequencies.

---

### Membership Operator

```python
if fruits[j] in hash_map
```

Checks whether a fruit type already exists.

---

### Delete from Dictionary

```python
del hash_map[fruits[i]]
```

Removes a fruit type when its frequency becomes zero.

---

### Built-in Function

```python
max()
```

Maintains the maximum window length.

---

## Key Takeaways

- This is a **variable-size sliding window** problem.
- The window is valid when it contains **at most two distinct fruit types**.
- Expand the window by moving the right pointer.
- Shrink the window whenever more than two fruit types appear.
- **Update the answer only after the window becomes valid.**
- The same sliding window template is used in many substring and subarray problems.

---

**Author:** Ramit Sarker
