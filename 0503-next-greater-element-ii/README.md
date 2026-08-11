````markdown
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
````

**Output**

```text
[2,-1,2]
```

Explanation:

* First `1` → next greater is `2`
* `2` → no greater element exists → `-1`
* Second `1` → searching circularly → `2`

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

The array is **circular**, so an element near the end may need to search from the beginning.

For example:

```text
[1,2,1]
```

The last `1` needs to look past the end:

```text
1 → 1 → 2
        ↑
```

To handle this, we can conceptually make the array twice as long:

```text
nums = [1,2,1]

nums2 = [1,2,1,1,2,1]
```

Now the circular array behaves like a normal linear array.

---

# Monotonic Stack

We use a **monotonic decreasing stack**.

The stack stores **indices of elements that are still waiting for a greater element**.

When the current value is greater than the value at the top of the stack:

```python
nums2[i] > nums2[stack[-1]]
```

we have found the next greater element for that index.

We then:

1. Pop the previous index.
2. Store the current value as its answer.
3. Continue checking the stack.

---

# Why Store Indices?

We need to know **where to put the answer**.

Suppose:

```text
nums = [1,2,1]
```

and the stack contains:

```text
[0]
```

This means index `0` (`value = 1`) is waiting.

When `2` arrives:

```text
2 > 1
```

we pop index `0` and set:

```python
res[0] = 2
```

So the stack stores indices, while the comparison uses the corresponding values.

---

# Handling the Circular Array

We traverse:

```python
nums + nums
```

but we only push indices from the **first copy** into the stack.

Why?

The second copy exists only to give the original elements a chance to find a greater element after wrapping around.

Therefore:

```python
if i < len(nums):
    stack.append(i)
```

The second half helps resolve the original indices but doesn't add new elements that need answers.

---

# Algorithm

1. Create a result array filled with `-1`.
2. Create an empty stack.
3. Traverse `nums + nums`.
4. While the stack isn't empty and the current value is greater than the value at the stack top:

   * Pop the previous index.
   * Set its answer to the current value.
5. Only push indices from the original array.
6. Return `res`.

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

Initial:

```text
stack = []
res = [-1,-1,-1]
```

### Index 0 → `1`

Push index `0`:

```text
stack = [0]
```

### Index 1 → `2`

`2 > 1`, so index `0` gets:

```text
res[0] = 2
```

Stack becomes empty.

Push index `1`:

```text
stack = [1]
```

### Index 2 → `1`

`1` is not greater than `2`.

Push index `2`:

```text
stack = [1,2]
```

### Index 3 → `1`

This is the beginning of the second copy.

`1` is not greater than the top value `1`.

We don't push index `3` because it belongs to the duplicated half.

### Index 4 → `2`

Now:

```text
2 > 1
```

So:

```text
res[2] = 2
```

Pop index `2`.

Then:

```text
2 > 2
```

is false, so index `1` remains unresolved.

Final:

```text
res = [2,-1,2]
```

---

# Why Does It Work?

Each original element is placed into the stack and waits for its next greater element.

The first copy handles elements normally.

The second copy allows elements near the end to search from the beginning, which is exactly what circular traversal requires.

If an element is never popped, no greater element exists anywhere in the circular array, so its answer correctly remains:

```text
-1
```

---

# Complexity

Let `n = len(nums)`.

### Time Complexity

We traverse `2n` elements.

Each original index is pushed once and popped at most once.

Therefore:

```text
O(n)
```

### Space Complexity

The stack can contain up to `n` indices, and the result array contains `n` elements.

The temporary doubled array `nums2` also takes `O(n)` space.

Therefore:

```text
O(n)
```

extra space.

---

# Key Takeaways

* This is a **Next Greater Element** problem.
* Use a **monotonic decreasing stack**.
* Store **indices** in the stack.
* Compare the corresponding **values**.
* Double the array to handle circular traversal.
* Only push indices from the original array.
* Initialize the result with `-1`.
* If an index is never popped, it has no greater element.
* Complexity: **O(n) time, O(n) space**.

```
```
**Author**
**Ramit Sarker**
