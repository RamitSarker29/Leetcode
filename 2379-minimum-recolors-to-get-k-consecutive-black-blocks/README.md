# 2463. Minimum Recolors to Get K Consecutive Black Blocks

## Problem

You are given a string `blocks` consisting of `'W'` (White) and `'B'` (Black) blocks and an integer `k`.

In one operation, you can recolor a white block into a black block.

Return the **minimum number of recolors** required so that there exists **at least one** substring of length `k` containing only black blocks.

---

## Example

### Example 1

```text
Input:
blocks = "WBBWWBBWBW"
k = 7

Output:
3
```

### Example 2

```text
Input:
blocks = "WBWBBBW"
k = 2

Output:
0
```

---

## Approach

Since we need **k consecutive blocks**, every valid substring has a **fixed size `k`**.

Using the **Sliding Window** technique:

- Expand the window by moving the right pointer.
- Store the frequency of `'W'` and `'B'` using a hash map.
- Whenever the window size becomes exactly `k`, count the number of white blocks.
- Since every white block must be recolored, the number of white blocks equals the required operations.
- Store the minimum value among all windows.
- Remove the leftmost character and continue sliding the window.

---

## Code

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j=0,k-1
        min_len=float('inf')
        hash_map={}
        for j in range(len(blocks)):
            if blocks[j] in hash_map:
                hash_map[blocks[j]]+=1
            else:
                hash_map[blocks[j]]=1
            if (j-i+1==k):
                min_len=min(min_len,hash_map.get('W',0))
                hash_map[blocks[i]]-=1
                i+=1
        return min_len
```

---

## Explanation

### Step 1

Initialize:

```python
i = 0
min_len = float('inf')
hash_map = {}
```

- `i` is the left pointer.
- `min_len` stores the minimum recolors required.
- `hash_map` stores the frequency of characters in the current window.

---

### Step 2

Expand the window.

```python
for j in range(len(blocks)):
```

Update the frequency of the current character.

```python
if blocks[j] in hash_map:
    hash_map[blocks[j]] += 1
else:
    hash_map[blocks[j]] = 1
```

---

### Step 3

When the window size becomes exactly `k`,

```python
if (j-i+1 == k):
```

count the number of white blocks.

```python
hash_map.get('W', 0)
```

This represents the number of recolors needed for the current window.

Update the answer.

```python
min_len = min(min_len, hash_map.get('W',0))
```

---

### Step 4

Slide the window.

Remove the leftmost character from the frequency map.

```python
hash_map[blocks[i]] -= 1
```

Move the left pointer.

```python
i += 1
```

Repeat the process until all windows are checked.

---

## Dry Run

```text
blocks = "WBWBBBW"
k = 2
```

| Window | White Blocks | Minimum |
|---------|-------------:|--------:|
| WB | 1 | 1 |
| BW | 1 | 1 |
| WB | 1 | 1 |
| BB | 0 | 0 |
| BB | 0 | 0 |
| BW | 1 | 0 |

Final Answer:

```text
0
```

---

## Time Complexity

- Each character is processed once.

**Time Complexity:** `O(n)`

---

## Space Complexity

- The hash map stores frequencies of at most two characters (`'W'` and `'B'`).

**Space Complexity:** `O(1)`

---

## Concepts Used

- Sliding Window
- Fixed Size Sliding Window
- Hash Map
- Two Pointers

---

## Python Features Used

- Dictionary
- `dict.get()`
- `float('inf')`

---

## Key Takeaways

- Fixed-size sliding window problems use `if (window_size == k)` instead of `while`.
- The number of white blocks in a window directly equals the number of recolors required.
- `dict.get(key, default)` safely returns a default value if the key is missing.
- Slide the window by removing the leftmost element and moving the left pointer.

---

## Author

**Ramit Sarker**
