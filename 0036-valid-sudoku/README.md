# 36. Valid Sudoku

## Problem

Given a `9 × 9` Sudoku board, determine whether it is valid.

The board is valid if all three rules are satisfied:

1. **Rows:** Each row must not contain duplicate digits from `1` to `9`.
2. **Columns:** Each column must not contain duplicate digits from `1` to `9`.
3. **3 × 3 Sub-boxes:** Each of the nine sub-boxes must not contain duplicate digits from `1` to `9`.

Empty cells are represented by `"."` and should be ignored.

**Important:** The board does not need to be solvable. We only need to check whether the currently filled cells violate any rule.

---

# Examples

## Example 1

![Sudoku Board](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```text
Input: board =
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
```

The board contains no repeated digits in any row, column, or 3 × 3 sub-box.

---

## Example 2

![Invalid Sudoku Board](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```text
Input: board =
[["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
```

The digit `"8"` appears twice in the top-left 3 × 3 sub-box.

Therefore, the board is invalid.

---

# Approach

Your solution checks the board in **three separate passes**:

<text color="secondary" size="sm">Pass 1</text>

**Validate every row**

- Create a set for each row.
- Ignore `"."`.
- If a digit is already in the set, return `False`.
- Otherwise, add the digit to the set.

<text color="secondary" size="sm">Pass 2</text>

**Validate every column**

- Create a set for each column.
- Traverse all rows in that column.
- Ignore `"."`.
- Return `False` if a duplicate is found.

<text color="secondary" size="sm">Pass 3</text>

**Validate every 3 × 3 sub-box**

- Use `range(0, 9, 3)` to move between sub-box starting positions.
- Create a fresh set for each sub-box.
- Use two nested loops to visit its nine cells.
- Ignore `"."` and check for duplicates.

If all three passes finish without finding a duplicate, return `True`.

---

# Code

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in board[i]:
                if j == '.':
                    continue
                if j in seen:
                    return False
                seen.add(j)

        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row + i][col + j]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)

        return True
```

---

# Code Explanation

## 1. Check Every Row

```python
for i in range(len(board)):
    seen = set()
    for j in board[i]:
        if j == '.':
            continue
        if j in seen:
            return False
        seen.add(j)
```

### Outer loop

```python
for i in range(len(board)):
```

Since the board has nine rows, `i` goes from `0` to `8`.

### Create a set

```python
seen = set()
```

A set stores unique values. It allows us to check whether a digit has already appeared in the current row.

**Important:** The set is created inside the outer loop, so every row gets its own set.

### Traverse the row

```python
for j in board[i]:
```

Here, `j` represents each cell value in the current row.

For example, the first row is:

```text
["5", "3", ".", ".", "7", ".", ".", ".", "."]
```

### Skip empty cells

```python
if j == '.':
    continue
```

Empty cells do not violate Sudoku rules, so we skip them.

### Detect duplicates

```python
if j in seen:
    return False
```

If the digit is already in the set, it has appeared earlier in the same row.

The board is invalid, so we immediately return `False`.

### Add the digit

```python
seen.add(j)
```

If the digit is new, store it in the set.

For the first row:

```text
5 → not present → add 5
3 → not present → add 3
. → skip
. → skip
7 → not present → add 7
```

The set becomes:

```text
{"5", "3", "7"}
```

No duplicate exists in this row.

---

## 2. Check Every Column

```python
for col in range(len(board)):
    seen = set()
    for row in range(len(board)):
        num = board[row][col]
        if num == '.':
            continue
        if num in seen:
            return False
        seen.add(num)
```

This time, we move vertically through the board.

### Outer loop

```python
for col in range(len(board)):
```

`col` represents the current column, from `0` to `8`.

A new set is created for each column.

### Inner loop

```python
for row in range(len(board)):
```

`row` moves through every row in the current column.

### Access a cell

```python
num = board[row][col]
```

This is an important difference from the row check.

- `row` selects the row.
- `col` selects the column.

For example:

```python
num = board[0][0]  # "5"
num = board[1][0]  # "6"
num = board[2][0]  # "."
```

These cells all belong to column `0`.

### Check for duplicates

The remaining logic is the same as the row check:

```python
if num == '.':
    continue

if num in seen:
    return False

seen.add(num)
```

Each column is checked independently.

---

## 3. Check Every 3 × 3 Sub-box

This is the most important part of the solution.

```python
for col in range(0, 9, 3):
    for row in range(0, 9, 3):
        seen = set()
        for i in range(3):
            for j in range(3):
                num = board[row + i][col + j]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
```

### Why `range(0, 9, 3)`?

```python
range(0, 9, 3)
```

produces:

```text
0, 3, 6
```

These are the starting positions of the three groups of rows and columns.

The board is divided into nine sub-boxes:

<box border radius="lg" padding={3} gap={2}>
  <grid columns={3} gap={2}>
    {#each ["Box 1\nRows 0–2\nCols 0–2","Box 2\nRows 0–2\nCols 3–5","Box 3\nRows 0–2\nCols 6–8","Box 4\nRows 3–5\nCols 0–2","Box 5\nRows 3–5\nCols 3–5","Box 6\nRows 3–5\nCols 6–8","Box 7\nRows 6–8\nCols 0–2","Box 8\nRows 6–8\nCols 3–5","Box 9\nRows 6–8\nCols 6–8"] as box}
      <grid-item>
        <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" minHeight="64px">
          <text textAlign="center" size="sm" preserveWhitespace>{box}</text>
        </box>
      </grid-item>
    {/each}
  </grid>
</box>

The two outer loops select each sub-box's starting row and column.

For example:

```text
col = 0
row = 0
```

selects the top-left sub-box.

Next:

```text
col = 0
row = 3
```

selects the middle-left sub-box.

The loops eventually cover all nine sub-boxes.

### Why create `seen` here?

```python
seen = set()
```

It is inside both outer loops, so each sub-box gets a fresh set.

Digits from one sub-box should not affect another sub-box.

### Why `range(3)`?

```python
for i in range(3):
    for j in range(3):
```

Each sub-box has three rows and three columns.

Both `i` and `j` take the values:

```text
0, 1, 2
```

Together, the loops visit all nine cells.

### Understanding `board[row + i][col + j]`

```python
num = board[row + i][col + j]
```

The starting coordinates are `row` and `col`.

- `i` moves down within the sub-box.
- `j` moves right within the sub-box.

For the top-left box, where `row = 0` and `col = 0`:

| `i` | `j` | Accessed cell |
|---:|---:|---|
| 0 | 0 | `board[0][0]` |
| 0 | 1 | `board[0][1]` |
| 0 | 2 | `board[0][2]` |
| 1 | 0 | `board[1][0]` |
| 1 | 1 | `board[1][1]` |
| 1 | 2 | `board[1][2]` |
| 2 | 0 | `board[2][0]` |
| 2 | 1 | `board[2][1]` |
| 2 | 2 | `board[2][2]` |

These are exactly the nine cells in the top-left sub-box.

The code then skips empty cells, checks for duplicates, and adds each new digit to `seen`.

---

# Dry Run

Consider the top-left 3 × 3 sub-box from Example 1:

![Sudoku Example](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

The sub-box contains:

```text
5  3  .
6  .  .
.  9  8
```

The starting coordinates are:

```text
row = 0
col = 0
seen = {}
```

### Step 1

```python
num = board[0][0]
```

Value:

```text
num = "5"
```

`"5"` is not in `seen`, so add it:

```text
seen = {"5"}
```

### Step 2

```python
num = board[0][1]
```

Value:

```text
num = "3"
```

Add it:

```text
seen = {"5", "3"}
```

### Step 3

```python
num = board[0][2]
```

Value:

```text
num = "."
```

The code executes:

```python
continue
```

Nothing is added to the set.

### Step 4

```python
num = board[1][0]
```

Value:

```text
num = "6"
```

Add it:

```text
seen = {"5", "3", "6"}
```

### Step 5

The next cell is empty, so it is skipped.

### Step 6

The next cell is also empty, so it is skipped.

### Step 7

```python
num = board[2][0]
```

The cell is empty and is skipped.

### Step 8

```python
num = board[2][1]
```

Value:

```text
num = "9"
```

Add it:

```text
seen = {"5", "3", "6", "9"}
```

### Step 9

```python
num = board[2][2]
```

Value:

```text
num = "8"
```

Add it:

```text
seen = {"5", "3", "6", "9", "8"}
```

All filled cells are unique, so this sub-box is valid.

The algorithm repeats this process for the remaining eight sub-boxes.

If no duplicate is found in any row, column, or sub-box, the function returns `True`.

---

# Dry Run: Invalid Sub-box

In Example 2, the top-left cell changes from `"5"` to `"8"`.

The top-left sub-box now contains:

```text
8  3  .
6  .  .
.  9  8
```

The first `"8"` is added to the set:

```text
seen = {"8", "3", "6", "9"}
```

When the algorithm reaches the second `"8"`:

```python
if num in seen:
    return False
```

The condition is true.

Therefore, the function returns:

```text
False
```

---

# Why Does It Work?

The algorithm independently validates all three Sudoku rules.

**Rows:** Each row has its own set, so any repeated filled digit is detected.

**Columns:** Each column has its own set, so repeated digits in a column are detected.

**Sub-boxes:** Each 3 × 3 region has its own set, and the nested loops visit every cell in that region.

In all three checks, empty cells are ignored and a repeated digit immediately causes the function to return `False`.

If all checks finish successfully, no Sudoku rule has been violated, so returning `True` is correct.

---

# Algorithm

1. Traverse each row and use a set to detect duplicate digits.
2. Traverse each column and use a set to detect duplicate digits.
3. Select each 3 × 3 sub-box using starting positions `0`, `3`, and `6`.
4. Visit all nine cells in each sub-box using two nested loops.
5. Skip cells containing `"."`.
6. Return `False` if a digit already exists in the current set.
7. If all three checks pass, return `True`.

---

# Complexity Analysis

Let \(N\) be the side length of the board. Here, \(N = 9\).

### Time Complexity

The row check processes \(N^2\) cells.

The column check also processes \(N^2\) cells.

The sub-box check processes all \(N^2\) cells once.

Therefore, the general time complexity is:

\[
O(N^2)
\]

Since the board is always `9 × 9`, its size is fixed, so the runtime is **O(1)** for this particular problem.

### Space Complexity

The algorithm uses a set to store digits from only one row, column, or sub-box at a time.

Each set can contain at most nine digits.

Therefore, auxiliary space is:

\[
O(N)
\]

For a fixed `9 × 9` board, this is **O(1)** space.

---

# Concepts Used

- Two-dimensional arrays
- Nested loops
- Sets and duplicate detection
- Row traversal
- Column traversal
- Matrix indexing
- Submatrix traversal
- Early return

---

# Python Features Used

### `set()`

```python
seen = set()
```

Creates an empty set to store unique digits.

### Membership Testing

```python
if num in seen:
```

Checks whether a digit has already appeared in the current row, column, or sub-box.

### `continue`

```python
if num == '.':
    continue
```

Skips empty cells and moves to the next iteration.

### `range()` With a Step

```python
range(0, 9, 3)
```

Generates `0`, `3`, and `6`, the starting positions of the sub-box groups.

### Two-Dimensional Indexing

```python
board[row + i][col + j]
```

Accesses a specific cell in the Sudoku board.

---

# Key Takeaways

- A valid Sudoku board must satisfy row, column, and sub-box rules.
- Sets provide a simple way to detect duplicates.
- Empty cells must be ignored.
- `board[row][col]` accesses a cell using its row and column indices.
- `range(0, 9, 3)` selects the starting positions of the nine sub-boxes.
- The nested loops `range(3)` visit all nine cells in each sub-box.
- The solution uses **O(1) time and space for the fixed-size board**; in terms of a generalized board size \(N\), it uses **O(N²) time and O(N) auxiliary space**.

---

# Author

**Ramit Sarker**
