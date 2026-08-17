# Number of Occurrence

## Problem

Given a **sorted array** `arr[]` and an integer `target`, find the **number of occurrences** of `target` in the array.

If the target is not present, return:

```text
0
```

The solution must have:

```text
Time Complexity: O(log n)
Auxiliary Space: O(1)
```

---

## Examples

### Example 1

**Input**

```text
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
```

**Output**

```text
4
```

**Explanation**

`2` occurs at indices:

```text
0  1  2  3  4  5  6
1  1  2  2  2  2  3
      ↑  ↑  ↑  ↑
      2  3  4  5
```

Therefore:

```text
4 occurrences
```

---

### Example 2

**Input**

```text
arr = [1, 1, 2, 2, 2, 2, 3]
target = 4
```

**Output**

```text
0
```

**Explanation**

`4` does not exist in the array.

Therefore, the number of occurrences is `0`.

---

### Example 3

**Input**

```text
arr = [8, 9, 10, 12, 12, 12]
target = 12
```

**Output**

```text
3
```

The target `12` occurs at indices:

```text
3, 4, 5
```

Therefore:

```text
5 - 3 + 1 = 3
```

occurrences.

---

# Approach

Because the array is **sorted**, we can solve this efficiently using **Binary Search**.

Instead of counting every occurrence one by one, we find:

1. The **first occurrence** of `target`.
2. The **last occurrence** of `target`.

Once we have both indices, the number of occurrences is:

```text
last - first + 1
```

---

# Why `last - first + 1`?

Suppose:

```text
first = 2
last = 5
```

The target occurs at:

```text
2, 3, 4, 5
```

That's `4` positions.

Therefore:

```text
5 - 2 + 1 = 4
```

The `+1` is necessary because both the first and last positions are included.

---

# Finding the First Occurrence

We use Binary Search.

When:

```python
arr[mid] == target
```

we have found a possible first occurrence.

Store:

```python
first = mid
```

But there may be another occurrence to the **left**.

Therefore:

```python
high = mid - 1
```

This keeps searching for an earlier occurrence.

### Logic

```text
target found
     ↓
save index
     ↓
search LEFT
```

---

# Finding the Last Occurrence

We perform another Binary Search.

When:

```python
arr[mid] == target
```

we have found a possible last occurrence.

Store:

```python
last = mid
```

But there may be another occurrence to the **right**.

Therefore:

```python
low = mid + 1
```

This keeps searching for a later occurrence.

### Logic

```text
target found
     ↓
save index
     ↓
search RIGHT
```

---

# Algorithm

### First Binary Search

1. Set `first = -1`.
2. Perform Binary Search.
3. If `arr[mid] > target`, move left.
4. If `arr[mid] < target`, move right.
5. If `arr[mid] == target`:

   * Store `mid` in `first`.
   * Continue searching left.

### Second Binary Search

1. Set `last = -1`.
2. Perform Binary Search again.
3. If `arr[mid] > target`, move left.
4. If `arr[mid] < target`, move right.
5. If `arr[mid] == target`:

   * Store `mid` in `last`.
   * Continue searching right.

### Calculate Answer

If the target was never found:

```text
first = -1
last = -1
```

return:

```text
0
```

Otherwise:

```text
last - first + 1
```

---

# Code

```python
class Solution:
    def countFreq(self, arr, target):
        # code here
        first = -1
        last = -1

        # Find first occurrence
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                high = mid - 1

            if arr[mid] < target:
                low = mid + 1

            if arr[mid] == target:
                first = mid
                high = mid - 1

        # Find last occurrence
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                high = mid - 1

            if arr[mid] < target:
                low = mid + 1

            if arr[mid] == target:
                last = mid
                low = mid + 1

        return 0 if first == -1 and last == -1 else last - first + 1
```

---

# Dry Run

Consider:

```text
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
```

Initial:

```text
first = -1
last = -1
```

---

## First Binary Search

We want the **first `2`**.

Eventually, Binary Search finds `2` at an index.

Whenever it finds `2`:

```python
first = mid
high = mid - 1
```

So it keeps moving toward the left.

The final value becomes:

```text
first = 2
```

The array is:

```text
Index:  0  1  2  3  4  5  6
        1  1  2  2  2  2  3
           ↑
        first = 2
```

---

## Second Binary Search

Now we search for the **last `2`**.

Whenever we find `2`:

```python
last = mid
low = mid + 1
```

So we continue searching toward the right.

Eventually:

```text
last = 5
```

The array is:

```text
Index:  0  1  2  3  4  5  6
        1  1  2  2  2  2  3
                    ↑
                 last = 5
```

---

## Calculate Frequency

Now:

```text
first = 2
last = 5
```

Therefore:

```text
last - first + 1
= 5 - 2 + 1
= 4
```

Final answer:

```text
4
```

---

# Dry Run: Target Not Present

Consider:

```text
arr = [1, 1, 2, 2, 2, 2, 3]
target = 4
```

Since the array contains no `4`, neither Binary Search finds the target.

Therefore:

```text
first = -1
last = -1
```

The condition:

```python
first == -1 and last == -1
```

is true.

So:

```python
return 0
```

---

# Why Does It Work?

The array is sorted, so Binary Search lets us efficiently locate the boundaries of the target.

The target occurrences form one continuous range:

```text
... < target | target target target target | > target ...
              ↑                         ↑
            first                     last
```

Once we know the boundaries, every index between `first` and `last` contains the target.

Therefore, the count is simply:

```text
last - first + 1
```

---

# Important Binary Search Pattern

This problem is an extension of the **First and Last Position** problem.

Remember:

### First Occurrence

When target is found:

```python
first = mid
high = mid - 1
```

Move **left**.

### Last Occurrence

When target is found:

```python
last = mid
low = mid + 1
```

Move **right**.

So the pattern is:

```text
First occurrence → LEFT
Last occurrence  → RIGHT
```

---

# Alternative Way to Think About It

The number of occurrences can also be understood as the distance between the first and last occurrence.

For example:

```text
first = 3
last = 7
```

Indices are:

```text
3, 4, 5, 6, 7
```

There are:

```text
7 - 3 + 1 = 5
```

elements.

This is why the formula works for every contiguous range of equal elements in a sorted array.

---

# Edge Cases

### Target Appears Once

```text
arr = [1, 2, 3, 4]
target = 3
```

Then:

```text
first = 2
last = 2
```

Therefore:

```text
2 - 2 + 1 = 1
```

---

### Target Appears Multiple Times

```text
arr = [1, 2, 2, 2, 3]
target = 2
```

Then:

```text
first = 1
last = 3
```

Therefore:

```text
3 - 1 + 1 = 3
```

---

### Target Does Not Exist

```text
arr = [1, 2, 3]
target = 5
```

Then:

```text
first = -1
last = -1
```

Return:

```text
0
```

---

# Complexity

Let:

```text
n = len(arr)
```

We perform two Binary Searches.

### First Search

```text
O(log n)
```

### Second Search

```text
O(log n)
```

Therefore:

```text
O(log n) + O(log n) = O(log n)
```

### Auxiliary Space

Only a constant number of variables are used:

```text
first
last
low
high
mid
```

Therefore:

```text
O(1)
```

---

# Key Takeaways

* The array is **sorted**, so Binary Search can be used.
* Find the **first occurrence** of the target.
* Find the **last occurrence** of the target.
* First occurrence → when found, move `high` left.
* Last occurrence → when found, move `low` right.
* If the target is absent, both indices remain `-1`.
* Number of occurrences:

```text
last - first + 1
```

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Author

**Ramit Sarker**
