# 882. Peak Index in a Mountain Array

## Problem

You are given a **mountain array** `arr`.

A mountain array has the following structure:

```text
Increasing → Peak → Decreasing
```

The array contains a single peak element, and we need to return the **index of that peak**.

The solution must have a time complexity of:

```text
O(log n)
```

---

## Examples

### Example 1

**Input**

```text
arr = [0,1,0]
```

**Output**

```text
1
```

**Explanation**

The array increases:

```text
0 → 1
```

and then decreases:

```text
1 → 0
```

Therefore, `1` is the peak.

```text
Index:  0  1  2
Array: [0, 1, 0]
          ↑
        peak
```

---

### Example 2

**Input**

```text
arr = [0,2,1,0]
```

**Output**

```text
1
```

The array increases until `2` and then decreases:

```text
0 → 2 → 1 → 0
    ↑
   peak
```

Therefore, the peak index is `1`.

---

### Example 3

**Input**

```text
arr = [0,10,5,2]
```

**Output**

```text
1
```

The peak element is `10` at index `1`.

---

# Approach

Since the array is guaranteed to be a **mountain array**, we can use **Binary Search**.

The important observation is that by comparing:

```python
arr[mid]
```

with:

```python
arr[mid + 1]
```

we can determine which side of the array contains the peak.

There are only two possibilities.

---

# Case 1: `arr[mid] < arr[mid + 1]`

This means we are currently on the **increasing side** of the mountain.

For example:

```text
0 → 2 → 5 → 10
        ↑
       mid
```

If:

```text
arr[mid] < arr[mid + 1]
```

the array is still increasing.

Therefore, the peak must be **to the right of `mid`**.

So we move:

```python
low = mid + 1
```

---

# Case 2: `arr[mid] > arr[mid + 1]`

This means we are on the **decreasing side** of the mountain.

For example:

```text
10 → 8 → 5 → 2
 ↑
mid
```

If:

```text
arr[mid] > arr[mid + 1]
```

we are either:

* at the peak, or
* somewhere after the peak.

Therefore, the peak can be at `mid` or somewhere to its left.

So we move:

```python
high = mid
```

Notice that we use:

```python
high = mid
```

instead of:

```python
high = mid - 1
```

because `mid` itself could be the peak.

---

# Key Idea

The entire logic can be remembered as:

```text
arr[mid] < arr[mid + 1]
        ↓
Going UP
        ↓
Peak is RIGHT
        ↓
low = mid + 1
```

and:

```text
arr[mid] > arr[mid + 1]
        ↓
Going DOWN
        ↓
Peak is LEFT or MID
        ↓
high = mid
```

Eventually:

```text
low == high
```

At that point, only the peak index remains.

---

# Algorithm

1. Set:

```python
low = 0
high = len(arr) - 1
```

2. While:

```python
low < high
```

3. Calculate:

```python
mid = (low + high) // 2
```

4. Compare `arr[mid]` and `arr[mid + 1]`.

5. If:

```python
arr[mid] < arr[mid + 1]
```

move right:

```python
low = mid + 1
```

6. Otherwise:

```python
high = mid
```

7. When `low == high`, return `high`.

---

# Code

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low = 0
        high = len(arr) - 1

        while low < high:

            mid = (low + high) // 2

            if arr[mid] > arr[mid + 1]:
                high = mid

            if arr[mid] < arr[mid + 1]:
                low = mid + 1

        return high
```

---

# Dry Run

Consider:

```text
arr = [0,1,0]
```

Initial:

```text
low = 0
high = 2
```

---

### Iteration 1

Calculate:

```text
mid = (0 + 2) // 2
mid = 1
```

Compare:

```text
arr[1] = 1
arr[2] = 0
```

So:

```text
1 > 0
```

We are on the decreasing side.

Therefore:

```text
high = mid
high = 1
```

Now:

```text
low = 0
high = 1
```

---

### Iteration 2

Calculate:

```text
mid = (0 + 1) // 2
mid = 0
```

Compare:

```text
arr[0] = 0
arr[1] = 1
```

So:

```text
0 < 1
```

We are on the increasing side.

Therefore:

```text
low = mid + 1
low = 1
```

Now:

```text
low = 1
high = 1
```

The loop stops.

Return:

```text
1
```

Therefore:

```text
Peak Index = 1
```

---

# Another Dry Run

Consider:

```text
arr = [0,2,1,0]
```

Initial:

```text
low = 0
high = 3
```

### Iteration 1

```text
mid = (0 + 3) // 2
mid = 1
```

Compare:

```text
arr[1] = 2
arr[2] = 1
```

Since:

```text
2 > 1
```

we are on the decreasing side.

So:

```text
high = 1
```

Now:

```text
low = 0
high = 1
```

---

### Iteration 2

```text
mid = (0 + 1) // 2
mid = 0
```

Compare:

```text
arr[0] = 0
arr[1] = 2
```

Since:

```text
0 < 2
```

we are on the increasing side.

So:

```text
low = 1
```

Now:

```text
low = 1
high = 1
```

Return:

```text
1
```

---

# Why Does `high = mid` Work?

This is one of the most important details in the solution.

Suppose:

```text
arr = [0,2,5,10,7,3]
```

and:

```text
mid = 3
```

We have:

```text
arr[3] = 10
arr[4] = 7
```

Therefore:

```text
10 > 7
```

We know we are on the decreasing side.

But `mid` itself might be the peak:

```text
        10
         ↑
0 → 2 → 5 → 10 → 7 → 3
```

Therefore, we **cannot discard `mid`**.

So we use:

```python
high = mid
```

instead of:

```python
high = mid - 1
```

---

# Why Does `low = mid + 1` Work?

If:

```python
arr[mid] < arr[mid + 1]
```

then `mid` cannot be the peak because the next element is larger.

For example:

```text
0 → 2 → 5 → 10
    ↑
   mid
```

Since:

```text
arr[mid] < arr[mid + 1]
```

the peak must be somewhere after `mid`.

Therefore, we can safely discard `mid`:

```python
low = mid + 1
```

---

# Visual Understanding

A mountain array looks like:

```text
             Peak
              ↓
              10
             /  \
            /    \
           /      \
          7        5
         /          \
        3            2
       /
      1
```

Binary Search determines whether `mid` is:

### On the way up

```text
arr[mid] < arr[mid + 1]
       /
      /
     ↑
   mid

→ Move RIGHT
```

### On the way down

```text
      \
       \
        ↓
       mid

→ Move LEFT / Keep mid
```

---

# Why Does the Loop Use `low < high`?

We use:

```python
while low < high:
```

instead of:

```python
while low <= high:
```

because we want to keep narrowing the search until **one index remains**.

Eventually:

```text
low == high
```

That single index is the peak.

For example:

```text
low = 1
high = 1
```

There is only one possible answer.

So we stop and return it.

---

# Why Is the Answer `high`?

When the loop ends:

```text
low == high
```

Therefore, both variables point to the same index.

So either would work:

```python
return low
```

or:

```python
return high
```

The solution uses:

```python
return high
```

---

# Complexity

Let:

```text
n = len(arr)
```

### Time Complexity

Every iteration eliminates roughly half of the remaining search space.

Therefore:

```text
O(log n)
```

### Space Complexity

Only a few variables are used:

```text
low
high
mid
```

No additional data structure is required.

Therefore:

```text
O(1)
```

---

# Key Takeaways

* The array is guaranteed to be a **mountain array**.
* Use **Binary Search** instead of scanning the entire array.
* Compare `arr[mid]` with `arr[mid + 1]`.
* If:

```python
arr[mid] < arr[mid + 1]
```

the array is increasing → **move right**.

* If:

```python
arr[mid] > arr[mid + 1]
```

the array is decreasing → **move left or keep `mid`**.

* Use:

```python
low = mid + 1
```

when going up.

* Use:

```python
high = mid
```

when going down.

* Stop when:

```python
low == high
```

* `low`/`high` then point to the peak.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
