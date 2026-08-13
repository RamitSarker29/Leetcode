# Delete Smaller Than Next

## Problem

Given an array `arr[]` and an integer `k`, delete exactly `k` elements that are **smaller than the next element**.

An element should be deleted if:

```text
arr[i] < arr[i+1]
```

An important point is that after deleting an element, the next element can move closer to the previous element and create a **new deletion opportunity**.

If multiple elements can be deleted, we always delete the **leftmost possible element**.

---

## Examples

### Example 1

**Input**

```text
arr = [20, 10, 25, 30, 40]
k = 2
```

**Output**

```text
[25, 30, 40]
```

**Explanation**

Initially:

```text
[20, 10, 25, 30, 40]
```

`10 < 25`, so delete `10`:

```text
[20, 25, 30, 40]
```

Now `20 < 25`, so delete `20`:

```text
[25, 30, 40]
```

We have deleted exactly `2` elements.

---

### Example 2

**Input**

```text
arr = [3, 100, 1]
k = 1
```

**Output**

```text
[100, 1]
```

**Explanation**

Since:

```text
3 < 100
```

delete `3`.

The remaining array is:

```text
[100, 1]
```

---

# Approach

We can solve this problem efficiently using a **stack**.

The stack represents the elements that have survived so far.

We traverse the array from **left to right**.

For every current element `arr[i]`, we check the top of the stack.

If:

```python
stack[-1] < arr[i]
```

then the element at the top of the stack is smaller than the current element.

Therefore, it should be deleted.

We pop it from the stack and decrease `k`.

We continue doing this while:

```python
stack[-1] < arr[i]
```

and:

```python
k != 0
```

Then we push the current element into the stack.

---

# Why Does the Stack Work?

Consider:

```text
arr = [20, 10, 25, 30, 40]
k = 2
```

We process from left to right.

After processing `20`:

```text
stack = [20]
```

Process `10`:

```text
10 < 20
```

This does not cause deletion because `10` is smaller than the element before it.

So:

```text
stack = [20, 10]
```

Now process `25`.

We compare it with the top:

```text
10 < 25
```

Therefore, `10` should be deleted:

```text
stack = [20]
k = 1
```

We check again:

```text
20 < 25
```

Now `20` must also be deleted:

```text
stack = []
k = 0
```

Finally, push `25`:

```text
stack = [25]
```

Then `30` and `40` are added normally.

Final result:

```text
[25, 30, 40]
```

---

# Important Observation

The key idea is that the **current element becomes the next element** for the elements stored in the stack.

For example:

```text
[20, 10, 25]
```

When `25` arrives:

```text
10 < 25
```

so `10` is deleted.

After deleting `10`:

```text
[20, 25]
```

Now:

```text
20 < 25
```

so `20` also becomes eligible for deletion.

The stack automatically handles this chain reaction.

---

# Algorithm

1. Create an empty stack.
2. Traverse the array from left to right.
3. For each element:

   * While the stack is not empty.
   * The top of the stack is smaller than the current element.
   * And `k > 0`.
   * Pop the stack and decrease `k`.
4. Push the current element into the stack.
5. Return the stack.

---

# Code

```python
class Solution:
    def deleteElement(self, arr, k):
        # Code here
        stack = []

        for i in range(len(arr)):
            while len(stack) != 0 and stack[-1] < arr[i] and k != 0:
                stack.pop()
                k -= 1

            stack.append(arr[i])

        return stack
```

---

# Dry Run

Consider:

```text
arr = [20, 10, 25, 30, 40]
k = 2
```

Initial:

```text
stack = []
k = 2
```

### Element `20`

Stack is empty:

```text
stack = [20]
```

---

### Element `10`

Check:

```text
20 < 10
```

False.

Push `10`:

```text
stack = [20, 10]
```

---

### Element `25`

Check top:

```text
10 < 25
```

True.

Delete `10`:

```text
stack = [20]
k = 1
```

Check again:

```text
20 < 25
```

True.

Delete `20`:

```text
stack = []
k = 0
```

Push `25`:

```text
stack = [25]
```

---

### Element `30`

`k = 0`, so no more deletions are allowed.

Push `30`:

```text
stack = [25, 30]
```

---

### Element `40`

Again `k = 0`.

Push `40`:

```text
stack = [25, 30, 40]
```

Final result:

```text
[25, 30, 40]
```

---

# Another Example

Consider:

```text
arr = [3, 100, 1]
k = 1
```

### `3`

```text
stack = [3]
```

### `100`

Since:

```text
3 < 100
```

delete `3`:

```text
stack = []
k = 0
```

Push `100`:

```text
stack = [100]
```

### `1`

No deletions remain because:

```text
k = 0
```

Push `1`:

```text
stack = [100, 1]
```

Final:

```text
[100, 1]
```

---

# Why Do We Use a `while` Loop?

A single `if` would not be enough.

Consider:

```text
arr = [20, 10, 25]
k = 2
```

When `25` arrives:

```text
stack = [20, 10]
```

First:

```text
10 < 25
```

Delete `10`.

But now `20` becomes the element immediately before `25`:

```text
20 < 25
```

So `20` must also be deleted.

Therefore, we need:

```python
while stack and stack[-1] < arr[i] and k != 0:
```

rather than just:

```python
if stack and stack[-1] < arr[i]:
```

The `while` loop handles multiple consecutive deletions.

---

# Why Is the Leftmost Element Deleted?

The stack processes elements from left to right.

When a larger current element arrives, we remove elements from the **top of the stack**, which represents the rightmost surviving element.

If that element is deleted, we immediately check the element before it.

This effectively performs the required **leftmost deletion process** while accounting for elements becoming adjacent after deletion.

---

# Complexity

Let:

```text
n = len(arr)
```

### Time Complexity

Each element is:

* pushed into the stack at most once
* popped from the stack at most once

Therefore, despite the nested `while` loop, the total work is:

```text
O(n)
```

### Space Complexity

In the worst case, no elements are deleted and the stack contains all `n` elements.

Therefore:

```text
O(n)
```

---

# Key Takeaways

* Use a **monotonic stack**.
* Traverse the array from **left to right**.
* The stack stores the elements that currently survive.
* If `stack[-1] < arr[i]`, the stack top can be deleted.
* Use a **`while` loop** because deleting one element can make another element eligible for deletion.
* Stop deleting once `k == 0`.
* Each element is pushed and popped at most once.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Author

**Ramit Sarker**

