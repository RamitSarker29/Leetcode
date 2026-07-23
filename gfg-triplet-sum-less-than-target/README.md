# Count Triplets with Sum Smaller than Given Value

## Problem

Given an array `arr[]` of **distinct integers** and an integer `sum`, count the number of triplets `(i, j, k)` such that:

- `i < j < k`
- `arr[i] + arr[j] + arr[k] < sum`

---

## Examples

### Example 1

**Input:**

```text
sum = 2
arr = [-2, 0, 1, 3]
```

**Output:**

```text
2
```

**Explanation:**

Valid triplets are:

```text
(-2, 0, 1)
(-2, 0, 3)
```

---

### Example 2

**Input:**

```text
sum = 12
arr = [5, 1, 3, 4, 7]
```

**Output:**

```text
4
```

**Explanation:**

Valid triplets are:

```text
(1, 3, 4)
(5, 1, 3)
(5, 1, 4)
(1, 3, 7)
```

---

## Approach

A brute-force solution checks every possible triplet, resulting in **O(n³)** time complexity.

We can optimize it using **sorting** and the **two-pointer technique**.

### Steps

1. Sort the array.
2. Fix one element (`i`).
3. Use two pointers:
   - `j = i + 1`
   - `k = n - 1`
4. Compute the current triplet sum.
5. If the sum is less than the target:
   - Then **every element from `j+1` to `k`** also forms a valid triplet because the array is sorted.
   - Add `k - j` to the answer.
   - Move `j` forward.
6. Otherwise, move `k` backward to reduce the sum.

---

## Code

```python
class Solution:
    def countTriplets(self, sum, arr):
        count = 0
        arr.sort()

        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1

            while j < k:
                current_sum = arr[i] + arr[j] + arr[k]

                if current_sum < sum:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1

        return count
```

---

## Explanation

Suppose

```text
arr = [1,2,3,4,5]
sum = 10
```

After sorting:

```text
[1,2,3,4,5]
```

Fix

```text
i = 0 (1)
```

Pointers

```text
j = 1 (2)
k = 4 (5)
```

Current sum

```text
1 + 2 + 5 = 8
```

Since

```text
8 < 10
```

the following triplets are also valid because the array is sorted:

```text
(1,2,5)
(1,2,4)
(1,2,3)
```

Instead of checking each individually, we directly count them:

```python
count += k - j
```

which is

```text
4 - 1 = 3
```

Then move `j` forward to search for more triplets.

---

## Dry Run

### Input

```text
arr = [-2,0,1,3]
sum = 2
```

Sorted array

```text
[-2,0,1,3]
```

### Iteration 1

```text
i = 0
j = 1
k = 3
```

```text
-2 + 0 + 3 = 1 < 2
```

Count

```text
k - j = 2
```

Valid triplets

```text
(-2,0,3)
(-2,0,1)
```

Move

```text
j++
```

---

Now

```text
j = 2
k = 3
```

```text
-2 + 1 + 3 = 2
```

Not smaller.

Move

```text
k--
```

Loop ends.

---

### Iteration 2

```text
i = 1
j = 2
k = 3
```

```text
0 + 1 + 3 = 4
```

Not smaller.

Move

```text
k--
```

Loop ends.

---

Final Answer

```text
2
```

---

## Time Complexity

- Sorting: **O(n log n)**
- Two-pointer traversal: **O(n²)**

Overall:

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

(ignoring the space used by sorting)

---

## Concepts Used

- Sorting
- Two Pointers
- Greedy Counting
- Array Traversal

---

## Python Features Used

- `sort()`
- `for` loop
- `while` loop

---

## Key Takeaways

- Sorting allows us to use the two-pointer technique efficiently.
- If `arr[i] + arr[j] + arr[k] < sum`, then every index between `j` and `k` also forms a valid triplet.
- Instead of checking every triplet individually, we add `k - j` directly.
- This reduces the complexity from **O(n³)** to **O(n²)**.

---

**Author:** Ramit Sarker
