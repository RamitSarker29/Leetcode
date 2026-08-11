# 503. Next Greater Element II

## Problem

Given a **circular integer array** `nums`, return the next greater element for every element.

Because the array is circular, after reaching the last element, we continue from the first element.

The **next greater element** of `nums[i]` is the first element encountered while moving forward that is strictly greater than `nums[i]`.

If no greater element exists, return `-1`.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,1]
```

**Output**

```text
[2,-1,2]
```

**Explanation**

* First `1` → next greater element is `2`
* `2` → no greater element exists → `-1`
* Second `1` → searching circularly, the next greater element is `2`

---

### Example 2

**Input**

```text
nums = [1,2,3,4,3]
```

**Output**

```text
[2,3,4,-1,4]
```

---

# Approach

The main difficulty is that the array is **circular**.

For example:

```text
nums = [1,2,1]
```

For the last `1`, after reaching the end of the array, we need to continue searching from the beginning:

```text
[1, 2, 1]
       ↓
       1 → 2
```

A simple way to handle this is to **traverse the array twice**.

Conceptually:

```text
nums = [1,2,1]

nums + nums
     ↓
[1,2,1,1,2,1]
```

The second copy allows elements near the end of the original array to find a greater element from the beginning.

---

# Monotonic Stack

We use a **monotonic decreasing stack**.

The stack stores **indices** of elements that are still waiting for their next greater element.

For every current element:

```python
while stack and nums[stack[-1]] < nums2[i]:
```

If the current value is greater than the value represented by the index at the top of the stack, then we have found the next greater element.

We:

1. Pop the index.
2. Store the current value as its answer.
3. Continue checking the remaining stack.

---

# Why Store Indices?

We store indices instead of values because we need to know **where to place the answer**.

For example:

```text
nums = [1,2,1]
```

Suppose:

```text
stack = [0]
```

Index `0` represents the value:

```text
nums[0] = 1
```

When `2` arrives:

```text
2 > 1
```

we pop index `0` and set:

```python
res[0] = 2
```

So:

* **Stack → stores indices**
* **Comparison → uses values**
* **Result → uses indices**

---

# Handling the Circular Array

We create:

```python
nums2 = nums + nums
```

and traverse all `2n` elements.

However, we only push indices from the **first copy**:

```python
if i < len(nums):
    stack.append(i)
```

Why?

The second copy is only used to help the original elements find their next greater elements after wrapping around.

We don't want the duplicated elements to become new elements that require answers.

---

# Algorithm

1. Create a result array filled with `-1`.
2. Create an empty stack.
3. Create a doubled array using `nums + nums`.
4. Traverse the doubled array.
5. While the stack is not empty and the current value is greater than the value at the stack top:

   * Pop the index.
   * Set its answer to the current value.
6. Push the index only if it belongs to the original array.
7. Return the result.

---

# Code

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        nums2 = nums + nums

        for i in range(len(nums2)):
            while stack and nums[stack[-1]] < nums2[i]:
                prev = stack.pop()
                res[prev] = nums2[i]

            if i < len(nums):
                stack.append(i)

        return res
```

---

# Dry Run

Consider:

```text
nums = [1,2,1]
```

Doubled array:

```text
nums2 = [1,2,1,1,2,1]
```

Initial state:

```text
stack = []
res = [-1,-1,-1]
```

### Index 0 → `1`

Stack is empty, so push index `0`:

```text
stack = [0]
```

---

### Index 1 → `2`

Current value:

```text
2
```

Top of stack:

```text
nums[0] = 1
```

Since:

```text
2 > 1
```

index `0` has found its next greater element.

```text
res[0] = 2
```

Pop index `0`:

```text
stack = []
```

Now push index `1`:

```text
stack = [1]
```

---

### Index 2 → `1`

Compare:

```text
1 > 2
```

False.

So push index `2`:

```text
stack = [1,2]
```

---

### Index 3 → `1`

This belongs to the **second copy**.

The current value is not greater than the value at index `2`:

```text
1 > 1
```

False.

We also don't push index `3` because:

```text
3 >= len(nums)
```

---

### Index 4 → `2`

Now:

```text
2 > nums[2]
2 > 1
```

Therefore:

```text
res[2] = 2
```

Pop index `2`:

```text
stack = [1]
```

Now compare with index `1`:

```text
2 > nums[1]
2 > 2
```

False.

So index `1` remains unresolved.

---

### Final Result

```text
res = [2,-1,2]
```

---

# Why Does It Work?

Every original element is placed into the stack and waits for a greater element.

The first traversal handles elements in their normal order.

The second traversal allows elements near the end of the array to continue searching from the beginning, which simulates circular traversal.

When a greater element is found, the waiting index is popped and its answer is recorded.

If an index is never popped, it means there is no strictly greater element anywhere in the circular array. Its answer therefore correctly remains:

```text
-1
```

---

# Complexity

Let:

```text
n = len(nums)
```

### Time Complexity

We traverse `2n` elements.

Although the loop runs twice over the array, every original index is:

* pushed at most once
* popped at most once

Therefore:

```text
O(n)
```

### Space Complexity

The stack can contain up to `n` indices.

The result array requires `O(n)` space.

The doubled array `nums2` also requires `O(n)` space.

Therefore:

```text
O(n)
```

extra space.

---

# Key Takeaways

* This is a **Next Greater Element** problem.
* Use a **monotonic decreasing stack**.
* Store **indices**, not values.
* Compare the values represented by those indices.
* Use `nums + nums` to simulate circular traversal.
* Only push indices from the original array.
* Initialize the result with `-1`.
* An index that is never popped has no greater element.
* Each element is pushed and popped at most once.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Author

**Ramit Sarker**
