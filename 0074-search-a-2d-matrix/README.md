# 74. Search a 2D Matrix

## Problem

Given an `m x n` matrix where:

* Each row is sorted in **non-decreasing order**.
* The first element of each row is greater than the last element of the previous row.

Return `true` if `target` exists in the matrix, otherwise return `false`.

The solution must run in:

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

`3` exists at row `0`, column `1`.

![Example 1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

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

![Example 2](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

---

# Approach

We can solve this problem using **two Binary Searches**.

### Step 1: Find the possible row

We perform Binary Search on the rows.

For every middle row, we look at its **last element**:

```python
matrix[mid][-1]
```

Why?

Because the rows are arranged like:

```text
[1, 3, 5, 7]
[10, 11, 16, 20]
[23, 30, 34, 60]
```

So each row represents a continuous range of values.

For example:

```text
Row 0 → 1 to 7
Row 1 → 10 to 20
Row 2 → 23 to 60
```

---

## Finding the Row

Suppose:

```text
target = 13
```

If:

```python
matrix[mid][-1] < target
```

then the target cannot be in that row or any row before it.

So:

```python
low = mid + 1
```

If:

```python
matrix[mid][-1] > target
```

then this row **might** contain the target.

We store it:

```python
row = mid
```

and search toward the left:

```python
high = mid - 1
```

If:

```python
matrix[mid][-1] == target
```

we have found the target directly:

```python
return True
```

---

# Step 2: Binary Search Inside the Row

Once we find the possible row, we perform a normal Binary Search inside it.

For example:

```text
[10,11,16,20]
```

For every `mid`:

### If:

```python
matrix[row][mid] < target
```

search right:

```python
low = mid + 1
```

### If:

```python
matrix[row][mid] > target
```

search left:

```python
high = mid - 1
```

### If:

```python
matrix[row][mid] == target
```

return:

```python
True
```

If the search finishes without finding the target, return:

```python
False
```

---

# Algorithm

1. Initialize:

   ```python
   low = 0
   high = len(matrix) - 1
   row = -1
   ```

2. Binary Search through the rows.

3. Compare the **last element** of the middle row with `target`.

4. Find the row that could contain the target.

5. If no such row exists, return `False`.

6. Perform Binary Search inside the selected row.

7. Return `True` if found, otherwise `False`.

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

        # Binary Search inside the row
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
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 3
```

Initial:

```text
low = 0
high = 2
row = -1
```

### First Binary Search

```text
mid = (0 + 2) // 2
mid = 1
```

Row `1`:

```text
[10,11,16,20]
```

Last element:

```text
20
```

Since:

```text
20 > 3
```

this row could contain the target.

So:

```text
row = 1
high = 0
```

---

### Next iteration

```text
mid = (0 + 0) // 2
mid = 0
```

Row `0`:

```text
[1,3,5,7]
```

Last element:

```text
7
```

Since:

```text
7 > 3
```

we update:

```text
row = 0
high = -1
```

The row search ends.

We have:

```text
row = 0
```

---

# Search Inside Row 0

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

Since:

```text
3 == target
```

return:

```text
True
```

---

# Dry Run: Target Not Found

Consider:

```text
target = 13
```

The possible row is:

```text
[10,11,16,20]
```

because:

```text
10 <= 13 <= 20
```

Now perform Binary Search:

```text
[10,11,16,20]
```

Middle:

```text
11
```

Since:

```text
11 < 13
```

move right.

Now:

```text
16
```

Since:

```text
16 > 13
```

move left.

The search range becomes empty.

Therefore:

```text
False
```

---

# Why Does It Work?

The matrix can effectively be viewed as one sorted sequence:

```text
[1,3,5,7,10,11,16,20,23,30,34,60]
```

The special property of the matrix guarantees that every row continues directly after the previous row.

Instead of performing one large Binary Search, the solution breaks the problem into:

```text
Find Row
   ↓
Binary Search Row
```

The first search determines where the target **could** be.

The second search determines whether the target actually exists there.

---

# Why Use the Last Element of Each Row?

Suppose:

```text
Row 0 → [1,3,5,7]
Row 1 → [10,11,16,20]
Row 2 → [23,30,34,60]
```

For:

```text
target = 13
```

we can compare it with the row endings:

```text
7 < 13
20 > 13
60 > 13
```

The first row ending greater than the target identifies the row that could contain it.

That's why we use:

```python
matrix[mid][-1]
```

---

# Complexity

Let:

```text
m = number of rows
n = number of columns
```

### First Binary Search

Searching through the rows:

```text
O(log m)
```

### Second Binary Search

Searching inside one row:

```text
O(log n)
```

Therefore:

```text
O(log m + log n)
```

which is equivalent to:

```text
O(log(m * n))
```

### Space Complexity

Only a few variables are used.

```text
O(1)
```

---

# Key Takeaways

* The matrix is sorted both **row-wise** and **across rows**.
* Use Binary Search to find the possible row.
* Compare `target` with the **last element** of each row.
* Then perform another Binary Search inside that row.
* If `matrix[mid][-1] < target` → move down.
* If `matrix[mid][-1] > target` → store the row and move up.
* If the last element equals the target → immediately return `True`.
* **Time Complexity:** `O(log(m * n))`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
