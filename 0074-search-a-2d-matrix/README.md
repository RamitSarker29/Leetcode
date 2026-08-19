# 74. Search a 2D Matrix

## Problem

You are given an `m x n` integer matrix `matrix` with the following properties:

* Each row is sorted in **non-decreasing order**.
* The first element of each row is greater than the last element of the previous row.

Given an integer `target`, return:

```text
true
```

if the target exists in the matrix, otherwise return:

```text
false
```

The solution must have a time complexity of:

```text
O(log(m * n))
```

---

## Examples

### Example 1

**Input**

```text
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 3
```

**Output**

```text
true
```

**Explanation**

`3` exists in the matrix at row `0`, column `1`.

![Image](https://images.openai.com/static-rsc-4/t-0vCUIH-xNjXQpbfDMSCDGkw4qF4QHAcbhgXY2KVemD3EcyQ8aLh380i58pqRVpqSAtsTO7Es_ipqU1jjOcaqH0eF4Rn_mHedC5h1MLZMlJ19IwBPpwmoiz1E80XSAtwxpn3SgiIUMZW5d_M8_dOSvxKXthLEGnOQoTIHBJrvy90DkLwLfGZZ1FMXOIxxkD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/BfPhAllqhIJwZmBnXbFQ-omTWgTqyARADF7uvBkXXLqL-segqRHoUw9QdFfbknimefwVSetvRbeHIn7Wr4_zJdaWvK16QeCM6IdFUo-wAzXIKZLydJ738P_QffVbE7ZI60Cci2Z4vy5XUTDq8dmIwMt2LQ6CDkPwbXOwrFtLsvHXmtUzTb4-74wcLbNoFDjZ?purpose=fullsize)

---

### Example 2

**Input**

```text
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 13
```

**Output**

```text
false
```

**Explanation**

`13` does not exist in the matrix.

![Image](https://images.openai.com/static-rsc-4/EVufEmO9JlDt2_7J_rpxfEstKbWCUajWUh1aYjwzcKy6qYr_zFQl0AvEPGdekd7l6sk4z1xZKbXndxf8AU_HKmpDnEtZrLSaWFSL-JfTy_yygaWtImZNHqh2ERXrFOegjfTvmE6cO7NF3sdloUinC5owaYhpYuYSs6JtacIr_olmfZB_KZZ-KPrLnOWSpleP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Kp6SK28bFuCOE8j7mnrU6O5ZjJOVIJpVi_eut-lj5lZWIxc4H6CsdiJEktx2HW0-BkloYxK-VOGt46OoiCzHP-YmMnhQcxTqnajTGpt3PQDdXybWPlO3SzyxH7hHSXKVgJc86GAQ4TG9GN-rmdd-c8OgrjWVpgtABdQ1Ii-qjM8sx14n6nl4UjBSeysqJVqd?purpose=fullsize)

---

# Approach

We can solve this problem using **two Binary Searches**:

1. Find the correct row where the target could exist.
2. Perform Binary Search inside that row.

The key observation is that every row has a clear range of values.

For example:

```text
[1,  3,  5,  7]
[10, 11, 16, 20]
[23, 30, 34, 60]
```

The ranges are:

```text
Row 0 → 1 to 7
Row 1 → 10 to 20
Row 2 → 23 to 60
```

Because:

```text
first element of next row
>
last element of previous row
```

we can determine which row could contain the target using Binary Search.

---

# Step 1: Find the Correct Row

We perform Binary Search on the rows.

Instead of checking the first element of each row, we compare the target with the **last element** of the current row:

```python
matrix[mid][-1]
```

Why the last element?

Suppose:

```text
Row 0 → [1,3,5,7]
Row 1 → [10,11,16,20]
Row 2 → [23,30,34,60]
```

If:

```text
matrix[mid][-1] < target
```

then the target cannot be in that row or any row before it.

So we move right:

```python
low = mid + 1
```

---

# Case 1: Last Element < Target

Suppose:

```text
target = 13
```

and the current row is:

```text
[1,3,5,7]
```

The last element is:

```text
7
```

Since:

```text
7 < 13
```

the target cannot be in this row.

It also cannot be in any previous row.

Therefore:

```python
low = mid + 1
```

---

# Case 2: Last Element > Target

Suppose:

```text
target = 13
```

and the current row is:

```text
[23,30,34,60]
```

The last element is:

```text
60
```

Since:

```text
60 > 13
```

the target could potentially be in this row or an earlier row.

So we store this row as a candidate:

```python
row = mid
```

and continue searching left:

```python
high = mid - 1
```

This allows us to find the **first row whose last element is greater than the target**.

---

# Case 3: Last Element == Target

If:

```python
matrix[mid][-1] == target
```

then we have directly found the target.

So we can immediately return:

```python
True
```

---

# Why Store `row`?

Suppose:

```text
matrix =
[1,3,5,7]
[10,11,16,20]
[23,30,34,60]

target = 13
```

The correct row is:

```text
[10,11,16,20]
```

because:

```text
10 <= 13 <= 20
```

Our first Binary Search finds this row and stores:

```python
row = 1
```

Then we perform another Binary Search inside:

```text
[10,11,16,20]
```

---

# Step 2: Binary Search Inside the Row

Once we have found the possible row, we perform normal Binary Search.

Initialize:

```python
low = 0
high = len(matrix[row]) - 1
```

Then calculate:

```python
mid = (low + high) // 2
```

Compare:

```python
matrix[row][mid]
```

with the target.

---

# Normal Binary Search Logic

### If value < target

Move right:

```python
low = mid + 1
```

### If value > target

Move left:

```python
high = mid - 1
```

### If value == target

Return:

```python
True
```

If the search finishes without finding it:

```python
False
```

---

# Algorithm

### Find the Row

1. Set `low = 0`.
2. Set `high = len(matrix) - 1`.
3. Set `row = -1`.
4. Perform Binary Search on the rows.
5. Compare `matrix[mid][-1]` with `target`.
6. If the last element is smaller, move right.
7. If the last element is greater, save the row and move left.
8. If equal, return `True`.

### Search Inside the Row

1. If `row == -1`, return `False`.
2. Set `low = 0`.
3. Set `high = len(matrix[row]) - 1`.
4. Perform normal Binary Search.
5. Return `True` if found.
6. Otherwise return `False`.

---

# Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1
        row = -1

        # Find the possible row
        while low <= high:

            mid = (low + high) // 2

            if matrix[mid][-1] < target:
                low = mid + 1

            if matrix[mid][-1] > target:
                row = mid
                high = mid - 1

            if matrix[mid][-1] == target:
                return True

        if row == -1:
            return False

        # Binary search inside the row
        low = 0
        high = len(matrix[row]) - 1

        while low <= high:

            mid = (low + high) // 2

            if matrix[row][mid] < target:
                low = mid + 1

            if matrix[row][mid] > target:
                high = mid - 1

            if matrix[row][mid] == target:
                return True

        return False
```

---

# Dry Run

Consider:

```text
matrix =
[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

target = 3
```

---

## Step 1: Find the Row

Initial:

```text
low = 0
high = 2
row = -1
```

### Iteration 1

```text
mid = (0 + 2) // 2
mid = 1
```

Current row:

```text
[10,11,16,20]
```

Last element:

```text
20
```

Compare:

```text
20 > 3
```

So this row could contain the target.

Store:

```text
row = 1
```

Search left:

```text
high = 0
```

---

### Iteration 2

Now:

```text
low = 0
high = 0
```

Calculate:

```text
mid = 0
```

Current row:

```text
[1,3,5,7]
```

Last element:

```text
7
```

Compare:

```text
7 > 3
```

So:

```text
row = 0
high = -1
```

The loop ends.

We found:

```text
row = 0
```

---

# Step 2: Search Inside Row 0

Row:

```text
[1,3,5,7]
```

Initial:

```text
low = 0
high = 3
```

Calculate:

```text
mid = (0 + 3) // 2
mid = 1
```

Value:

```text
matrix[0][1] = 3
```

Compare:

```text
3 == 3
```

Target found.

Return:

```text
True
```

---

# Dry Run: Target Not Found

Consider:

```text
target = 13
```

The matrix is:

```text
[1,3,5,7]
[10,11,16,20]
[23,30,34,60]
```

---

## Find the Row

Initial:

```text
low = 0
high = 2
```

### Iteration 1

```text
mid = 1
```

Last element:

```text
20
```

Since:

```text
20 > 13
```

store:

```text
row = 1
```

and move left:

```text
high = 0
```

### Iteration 2

```text
mid = 0
```

Last element:

```text
7
```

Since:

```text
7 < 13
```

move right:

```text
low = 1
```

Now:

```text
low = 1
high = 0
```

The row is:

```text
row = 1
```

---

## Search Row 1

Row:

```text
[10,11,16,20]
```

Initial:

```text
low = 0
high = 3
```

### Iteration 1

```text
mid = 1
matrix[1][1] = 11
```

Since:

```text
11 < 13
```

move right:

```text
low = 2
```

### Iteration 2

```text
mid = 2
matrix[1][2] = 16
```

Since:

```text
16 > 13
```

move left:

```text
high = 1
```

Now:

```text
low = 2
high = 1
```

The search ends.

`13` was not found.

Return:

```text
False
```

---

# Why Does the Row Search Work?

Each row has a distinct range.

For example:

```text
Row 0: 1  → 7
Row 1: 10 → 20
Row 2: 23 → 60
```

If:

```text
last element of row < target
```

then the target must be in a later row.

If:

```text
last element of row >= target
```

then this row might contain the target, so we save it and search earlier rows.

Therefore, the first Binary Search identifies the row whose range could contain the target.

---

# Visual Understanding

Think of the matrix as a collection of sorted ranges:

```text
          Target
             ↓
[1, 3, 5, 7]        → 1 to 7
[10,11,16,20]        → 10 to 20
[23,30,34,60]        → 23 to 60
```

For:

```text
target = 13
```

we can immediately see:

```text
10 ≤ 13 ≤ 20
```

Therefore, only row `1` needs to be searched.

Binary Search finds this without checking every row.

---

# Why Not Search the Entire Matrix Linearly?

A straightforward approach would be:

```python
for row in matrix:
    for value in row:
        if value == target:
            return True
```

This could take:

```text
O(m * n)
```

time.

But the matrix is sorted in a special way, so we can take advantage of that ordering.

Our approach performs:

```text
Binary Search on rows
        +
Binary Search on columns
```

giving:

```text
O(log m + log n)
```

which is equivalent to:

```text
O(log(m * n))
```

---

# Complexity

Let:

```text
m = number of rows
n = number of columns
```

### Finding the Row

Binary Search over `m` rows:

```text
O(log m)
```

### Searching Inside the Row

Binary Search over `n` columns:

```text
O(log n)
```

Therefore:

```text
O(log m + log n)
```

Since:

```text
log m + log n = log(m * n)
```

the overall complexity is:

```text
O(log(m * n))
```

### Space Complexity

Only a constant number of variables are used.

Therefore:

```text
O(1)
```

---

# Important Edge Cases

### Target Is the Last Element of a Row

For example:

```text
target = 20
```

and:

```text
[10,11,16,20]
```

The row search detects:

```python
matrix[mid][-1] == target
```

and immediately returns:

```text
True
```

---

### Target Is the First Element of a Row

For:

```text
target = 10
```

the correct row is:

```text
[10,11,16,20]
```

The second Binary Search finds it at index `0`.

---

### Target Smaller Than Every Element

For:

```text
target = 0
```

the first suitable row becomes row `0`.

The second Binary Search fails, so:

```text
False
```

is returned.

---

### Target Greater Than Every Element

For:

```text
target = 100
```

every row's last element is smaller than the target.

Eventually:

```text
row = -1
```

Therefore:

```text
False
```

is returned immediately.

---

# Key Takeaways

* The matrix has **sorted rows**.
* Each row starts after the previous row ends.
* Use Binary Search to find the **possible row**.
* Compare the target with the **last element of each row**.
* If:

```python
matrix[mid][-1] < target
```

move down:

```python
low = mid + 1
```

* If:

```python
matrix[mid][-1] > target
```

save the row and search upward:

```python
row = mid
high = mid - 1
```

* Once the row is found, perform normal Binary Search inside it.
* **Time Complexity:** `O(log(m * n))`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
