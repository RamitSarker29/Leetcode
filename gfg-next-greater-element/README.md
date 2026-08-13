# Next Greater Element

## Problem

Given an array `arr`, find the **next greater element** for every element.

The **next greater element** of an element is the first element to its right that is **strictly greater** than it.

If no greater element exists, return `-1`.

---

## Examples

### Example 1

**Input**

```text
arr = [1, 3, 2, 4]
```

**Output**

```text
[3, 4, 4, -1]
```

**Explanation**

* `1` → next greater is `3`
* `3` → next greater is `4`
* `2` → next greater is `4`
* `4` → no greater element → `-1`

---

### Example 2

**Input**

```text
arr = [4, 5, 2, 10, 8]
```

**Output**

```text
[5, 10, 10, -1, -1]
```

---

# Approach

We use a **monotonic decreasing stack**.

Instead of searching to the right for every element separately, we traverse the array **from right to left**.

The stack stores elements that could potentially be the next greater element for elements to their left.

For every `arr[i]`:

1. Remove all elements from the stack that are **less than or equal to** `arr[i]`.
2. If the stack is not empty, its top is the next greater element.
3. Push `arr[i]` into the stack.

---

# Why Traverse From Right to Left?

Consider:

```text
arr = [1, 3, 2, 4]
```

When processing `2`, we have already processed everything to its right:

```text
2 → 4
```

So `4` can potentially be its next greater element.

By moving from right to left, we always have information about the elements to the right available in the stack.

---

# Monotonic Decreasing Stack

The stack is maintained so that its elements are useful candidates for future elements.

Before finding the answer for `arr[i]`, we remove:

```python
stack[-1] <= arr[i]
```

because these elements **cannot be the next greater element**.

For example:

```text
arr[i] = 5
stack = [10, 7, 4]
```

The `4` and `7` cannot be greater than `5`.

So we remove them until we find:

```text
10 > 5
```

Now `10` is the next greater element.

---

# Why Use `<=`?

The problem asks for an element that is **strictly greater**.

Therefore, an equal element cannot be an answer.

For example:

```text
arr = [5, 5, 7]
```

For the first `5`, the second `5` is not greater.

So we remove elements satisfying:

```python
stack[-1] <= arr[i]
```

---

# Why Store Values Instead of Indices?

In this implementation, the stack stores the **actual values** rather than their indices.

We only need to return the next greater value, so there is no need to remember its position.

Therefore:

```python
stack.append(arr[i])
```

stores values directly.

This makes the implementation simpler.

---

# Algorithm

1. Create an empty stack.
2. Create a result array filled with `-1`.
3. Traverse the array from right to left.
4. Remove elements from the stack while they are less than or equal to the current element.
5. If the stack is not empty, its top is the next greater element.
6. Push the current element onto the stack.
7. Return the result.

---

# Code

```python
class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        res = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()

            if len(stack) != 0 and stack[-1] > arr[i]:
                res[i] = stack[-1]

            stack.append(arr[i])

        return res
```

---

# Dry Run

Consider:

```text
arr = [1, 3, 2, 4]
```

Initial:

```text
stack = []
res = [-1, -1, -1, -1]
```

### Index 3 → `4`

Stack is empty.

```text
res[3] = -1
```

Push `4`:

```text
stack = [4]
```

---

### Index 2 → `2`

Check:

```text
4 > 2
```

So:

```text
res[2] = 4
```

Push `2`:

```text
stack = [4, 2]
```

---

### Index 1 → `3`

Top is `2`.

Since:

```text
2 <= 3
```

pop `2`.

Now:

```text
stack = [4]
```

Check:

```text
4 > 3
```

Therefore:

```text
res[1] = 4
```

Push `3`:

```text
stack = [4, 3]
```

---

### Index 0 → `1`

Top is `3`.

Since:

```text
3 > 1
```

we have:

```text
res[0] = 3
```

Push `1`:

```text
stack = [4, 3, 1]
```

---

### Final Result

```text
[3, 4, 4, -1]
```

---

# Why Does It Work?

For every element, the stack removes all elements that cannot possibly be its next greater element.

After removing those elements, the top of the stack is the **closest valid greater element to the right**.

If the stack becomes empty, there is no greater element to the right, so the answer remains `-1`.

Each element is:

* pushed onto the stack once
* popped from the stack at most once

This allows us to solve the problem efficiently.

---

# Complexity

Let:

```text
n = len(arr)
```

### Time Complexity

We traverse the array once.

Although there is a `while` loop, each element can be pushed and popped at most once.

Therefore:

```text
O(n)
```

### Space Complexity

In the worst case, the stack can contain all `n` elements.

The result array also requires `O(n)` space.

Therefore:

```text
O(n)
```

---

# Key Takeaways

* This is a **Next Greater Element** problem.
* Use a **monotonic decreasing stack**.
* Traverse the array **from right to left**.
* Store **values** in the stack.
* Remove elements using `<=` because the next element must be **strictly greater**.
* The stack top gives the next greater element.
* If the stack is empty, the answer is `-1`.
* Each element is pushed and popped at most once.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Author

**Ramit Sarker**

