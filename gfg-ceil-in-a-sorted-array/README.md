# Ceil in a Sorted Array

## Problem

Given a **sorted array** `arr[]` and an integer `x`, find the **0-based index of the smallest element that is greater than or equal to `x`**.

This element is called the **ceil of `x`**.

If no element is greater than or equal to `x`, return:

```text
-1
```

If the ceil occurs multiple times, return the **index of its first occurrence**.

---

## Examples

### Example 1

**Input**

```text
arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
```

**Output**

```text
2
```

**Explanation**

The elements greater than or equal to `5` are:

```text
8, 10, 11, 12, 19
```

The smallest one is `8`, which is at index `2`.

---

### Example 2

**Input**

```text
arr = [1, 2, 8, 10, 11, 12, 19]
x = 20
```

**Output**

```text
-1
```

**Explanation**

There is no element greater than or equal to `20`.

Therefore, return `-1`.

---

### Example 3

**Input**

```text
arr = [1, 1, 2, 8, 10, 11, 12, 19]
x = 0
```

**Output**

```text
0
```

**Explanation**

The smallest element greater than or equal to `0` is `1`.

There are two occurrences of `1`:

```text
Index:  0  1  2  3 ...
Array: [1, 1, 2, 8 ...]
        ↑
```

We need the **first occurrence**, so the answer is `0`.

---

# Approach

Since the array is already **sorted**, we can use **Binary Search**.

We are looking for the first index where:

```python
arr[i] >= x
```

This is essentially a **lower bound** search.

We maintain:

```python
low
high
ans
```

Initially:

```python
low = 0
high = len(arr) - 1
ans = -1
```

---

# Binary Search Logic

For every iteration, calculate:

```python
mid = (low + high) // 2
```

Then check `arr[mid]`.

### Case 1: `arr[mid] >= x`

We have found a possible ceil.

Store its index:

```python
ans = mid
```

But there might be another valid element **earlier** in the array.

Therefore, search the left half:

```python
high = mid - 1
```

This is what ensures that we find the **first occurrence**.

---

### Case 2: `arr[mid] < x`

The current element is too small.

Since the array is sorted, everything to the left is also too small.

Therefore, search the right half:

```python
low = mid + 1
```

---

# Why Do We Keep `ans`?

Suppose:

```text
arr = [1, 1, 2, 8, 10]
x = 1
```

When we find:

```text
arr[mid] = 2
```

it is greater than or equal to `1`, so it is a valid candidate.

But there might be another valid element before it.

So instead of immediately returning, we store:

```python
ans = mid
```

and continue searching left.

Eventually, we find the **first valid index**.

---

# Algorithm

1. Set `low = 0`.
2. Set `high = len(arr) - 1`.
3. Set `ans = -1`.
4. While `low <= high`:

   * Calculate `mid`.
   * If `arr[mid] >= x`:

     * Store `mid` in `ans`.
     * Move `high` left.
   * Otherwise:

     * Move `low` right.
5. Return `ans`.

---

# Code

```python
class Solution:
    def findCeil(self, arr, x):
        # code here
        low = 0
        high = len(arr) - 1
        ans = -1

        while high >= low:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1

            if arr[mid] < x:
                low = mid + 1

        return ans
```

---

# Dry Run

Consider:

```text
arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
```

Initial:

```text
low = 0
high = 6
ans = -1
```

---

### Iteration 1

Calculate:

```text
mid = (0 + 6) // 2
mid = 3
```

Value:

```text
arr[3] = 10
```

Check:

```text
10 >= 5
```

True.

So:

```text
ans = 3
high = 2
```

We found a possible ceil, but there may be a smaller valid element on the left.

Search:

```text
[1, 2, 8]
```

---

### Iteration 2

Now:

```text
low = 0
high = 2
```

Calculate:

```text
mid = (0 + 2) // 2
mid = 1
```

Value:

```text
arr[1] = 2
```

Check:

```text
2 < 5
```

True.

So the ceil must be to the right:

```text
low = 2
```

---

### Iteration 3

Now:

```text
low = 2
high = 2
```

Calculate:

```text
mid = 2
```

Value:

```text
arr[2] = 8
```

Check:

```text
8 >= 5
```

True.

Update:

```text
ans = 2
high = 1
```

Now:

```text
low = 2
high = 1
```

The loop ends.

Return:

```text
2
```

---

# Dry Run: Duplicate Values

Consider:

```text
arr = [1, 1, 2, 8, 10]
x = 1
```

We need the **first occurrence** of `1`.

Initial:

```text
low = 0
high = 4
ans = -1
```

### Iteration 1

```text
mid = 2
arr[mid] = 2
```

Since:

```text
2 >= 1
```

store:

```text
ans = 2
```

and search left:

```text
high = 1
```

---

### Iteration 2

```text
low = 0
high = 1
mid = 0
```

Now:

```text
arr[0] = 1
```

Since:

```text
1 >= 1
```

update:

```text
ans = 0
```

and continue left:

```text
high = -1
```

The search ends.

Return:

```text
0
```

So the algorithm correctly finds the **first occurrence**.

---

# Why Does It Work?

The array is sorted, so whenever:

```text
arr[mid] >= x
```

we know that `mid` is a valid answer, but there may be another valid answer before it.

Therefore:

```python
ans = mid
high = mid - 1
```

keeps searching toward the left.

Whenever:

```text
arr[mid] < x
```

we know that `mid` and everything before it cannot be the answer.

Therefore:

```python
low = mid + 1
```

moves the search to the right.

At the end, `ans` contains the **leftmost index whose value is at least `x`**.

---

# Important Connection: Lower Bound

This problem is essentially asking for the **lower bound** of `x`.

Lower bound means:

> Find the first position where the element is greater than or equal to `x`.

The condition is:

```python
arr[mid] >= x
```

and when we find it, we continue searching left:

```python
high = mid - 1
```

This same pattern is useful in many binary-search problems.

---

# Edge Cases

### Ceil Exists at Index `0`

```text
arr = [1, 2, 3, 4]
x = 0
```

The answer is:

```text
0
```

because `1` is the smallest element greater than or equal to `0`.

---

### Exact Match

```text
arr = [1, 2, 3, 4]
x = 3
```

The ceil is `3` itself.

Answer:

```text
2
```

---

### No Ceil Exists

```text
arr = [1, 2, 3, 4]
x = 5
```

No element satisfies:

```text
arr[i] >= 5
```

Therefore:

```text
-1
```

---

### Multiple Occurrences

```text
arr = [1, 1, 1, 2, 3]
x = 1
```

The answer must be:

```text
0
```

The algorithm continues searching left whenever it finds a valid candidate, so it correctly returns the first occurrence.

---

# Complexity

Let:

```text
n = len(arr)
```

### Time Complexity

Binary Search eliminates approximately half of the search space after every iteration.

Therefore:

```text
O(log n)
```

### Space Complexity

Only three variables are used:

```text
low
high
ans
```

Therefore:

```text
O(1)
```

---

# Key Takeaways

* The array must be **sorted**.
* This problem is a **Binary Search / Lower Bound** problem.
* We search for the first index satisfying:

```python
arr[i] >= x
```

* If `arr[mid] >= x`, store `mid` and search left.
* If `arr[mid] < x`, search right.
* `ans` stores the best valid answer found so far.
* Searching left after finding a valid candidate ensures the **first occurrence** is returned.
* If no valid candidate exists, `ans` remains `-1`.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
