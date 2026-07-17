# LeetCode 66 - Plus One

## Problem

You are given a large integer represented as an array of digits, where each element is a single digit of the number.

Increment the integer by **one** and return the resulting array of digits.

---

## Examples

### Example 1

**Input**

```text
digits = [1,2,3]
```

**Output**

```text
[1,2,4]
```

---

### Example 2

**Input**

```text
digits = [4,3,2,1]
```

**Output**

```text
[4,3,2,2]
```

---

### Example 3

**Input**

```text
digits = [9]
```

**Output**

```text
[1,0]
```

---

## Approach

- Traverse the array from **right to left**.
- If the current digit is **less than 9**, simply increment it by `1` and return the array.
- If the current digit is `9`, change it to `0` and continue moving left because of the carry.
- If every digit was `9`, all digits become `0`. In that case, prepend `1` to the array and return it.

---

## Code

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
```

---

## Explanation

The addition starts from the last digit, just like manual addition.

- If a digit is not `9`, adding `1` does not produce a carry, so the answer is complete.
- If a digit is `9`, it becomes `0` and the carry moves to the previous digit.
- The process continues until a digit less than `9` is found.
- If all digits are `9`, a new leading digit `1` is added.

---

## Dry Run

**Input**

```text
digits = [1,9,9]
```

| i | Current Digit | Action | Array |
|---|--------------:|--------|-------|
|2|9|Set to 0|[1,9,0]|
|1|9|Set to 0|[1,0,0]|
|0|1|Increment and Return|[2,0,0]|

**Final Output**

```text
[2,0,0]
```

---

### Special Case

**Input**

```text
digits = [9,9,9]
```

After processing all digits:

```text
[0,0,0]
```

Since all digits were `9`, prepend `1`:

```text
[1,0,0,0]
```

---

## Time Complexity

```text
O(n)
```

The array is traversed at most once.

---

## Space Complexity

```text
O(1)
```

The solution modifies the array in-place and uses constant extra space.

---

## Concepts Used

- Array Traversal
- Carry Propagation
- In-Place Modification
- Simulation

---

## Python Features Used

- Reverse iteration using `range(start, stop, step)`
- List concatenation (`[1] + digits`)
- Early `return`

---

## Author

**Ramit Sarker**
