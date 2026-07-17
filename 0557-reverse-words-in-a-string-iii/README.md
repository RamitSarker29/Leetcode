# LeetCode 557 - Reverse Words in a String III

## Problem

Given a string `s`, reverse the characters of each word while preserving the order of the words and the whitespace.

---

## Example

### Input

```text
Let's take LeetCode contest
```

### Output

```text
s'teL ekat edoCteeL tsetnoc
```

---

## Approach

- Use two pointers (`left` and `right`) to identify each word.
- Move the `right` pointer until a space or the end of the string is reached.
- Extract the current word using string slicing.
- Reverse the word using `[::-1]`.
- Store the reversed word in a list.
- Move `left` to the beginning of the next word.
- Join all reversed words with spaces to form the final string.

---

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:

        result = []

        left = 0
        right = 0

        while right <= len(s):

            if right == len(s) or s[right] == " ":

                word = s[left:right]
                result.append(word[::-1])

                left = right + 1

            right += 1

        return " ".join(result)
```

---

## Explanation

- `left` marks the beginning of the current word.
- `right` moves through the string character by character.
- Whenever `right` reaches a space or the end of the string, the current word is extracted.
- The word is reversed using slicing (`[::-1]`) and added to the `result` list.
- `left` is updated to point to the beginning of the next word.
- Finally, all reversed words are joined together with spaces.

---

## Algorithm

1. Initialize an empty list `result`.
2. Set `left = 0` and `right = 0`.
3. Traverse the string using the `right` pointer.
4. When a space or the end of the string is reached:
   - Extract the current word.
   - Reverse it.
   - Append it to `result`.
   - Move `left` to the next word.
5. Continue until the entire string is processed.
6. Return `" ".join(result)`.

---

## Time Complexity

```text
O(n)
```

Each character is visited only once.

---

## Space Complexity

```text
O(n)
```

Extra space is used to store the reversed words.

---

## Concepts Used

- Two Pointers
- String Traversal
- String Slicing
- Lists
- String Joining

---

## Python Features Used

- String Slicing (`[::-1]`)
- `append()`
- `" ".join()`

---

## Author

**Ramit Sarker**
