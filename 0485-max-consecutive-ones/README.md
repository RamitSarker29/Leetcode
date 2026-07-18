# LeetCode 485 - Max Consecutive Ones

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,0,1,1,1]
```

**Output**

```text
3
```

**Explanation**

The first two `1`s form a consecutive sequence of length `2`, while the last three `1`s form a consecutive sequence of length `3`. The maximum consecutive count is `3`.

---

### Example 2

**Input**

```text
nums = [1,0,1,1,0,1]
```

**Output**

```text
2
```

---

## Approach

- Initialize two variables:
  - `res` to count the current streak of consecutive `1`s.
  - `max_res` to store the maximum streak found so far.
- Traverse the array once.
- If the current element is `1`, increment `res` and update `max_res`.
- If the current element is `0`, reset `res` to `0`.
- Return `max_res` after the traversal.

---

## Code

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max_res = 0

        for i in nums:
            if i == 1:
                res += 1
                max_res = max(max_res, res)
            else:
                res = 0

        return max_res
```

---

## Explanation

The variable `res` keeps track of the current consecutive sequence of `1`s.

Whenever a `1` is encountered:
- Increase the current count.
- Update `max_res` if the current count is greater than the previous maximum.

Whenever a `0` is encountered:
- Reset the current count to `0` because the consecutive sequence is broken.

After traversing the array, `max_res` contains the length of the longest sequence of consecutive `1`s.

---

## Dry Run

**Input**

```text
nums = [1,1,0,1,1,1]
```

| Element | Current Count (`res`) | Maximum Count (`max_res`) |
|---------:|----------------------:|--------------------------:|
|1|1|1|
|1|2|2|
|0|0|2|
|1|1|2|
|1|2|2|
|1|3|3|

**Final Output**

```text
3
```

---

## Time Complexity

```text
O(n)
```

The array is traversed exactly once.

---

## Space Complexity

```text
O(1)
```

Only two integer variables are used regardless of the input size.

---

## Concepts Used

- Array Traversal
- Counting
- Running Maximum

---

## Python Features Used

- `for` loop over a list
- Built-in `max()` function

---

## Author

**Ramit Sarker**
