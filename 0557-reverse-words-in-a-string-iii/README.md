# Reverse Words in a String III

## Problem

Given a string `s`, reverse the characters of each word while preserving the order of the words and the whitespace.

### Example

**Input**

```text
Let's take LeetCode contest
```

**Output**

```text
s'teL ekat edoCteeL tsetnoc
```

---

## Approach

* Use two pointers (`left` and `right`) to identify each word.
* Move the `right` pointer until a space or the end of the string is reached.
* Extract the current word using string slicing.
* Reverse the word using `[::-1]`.
* Store the reversed word in a list.
* Move `left` to the beginning of the next word.
* Join all reversed words with spaces to form the final string.

---

## Algorithm

1. Initialize an empty list `result`.
2. Set `left = 0` and `right = 0`.
3. Traverse the string using the `right` pointer.
4. When a space or the end of the string is encountered:

   * Extract the word.
   * Reverse it.
   * Append it to `result`.
   * Update `left` to the next character.
5. Return `" ".join(result)`.

---

## Time Complexity

```text
O(n)
```

Each character is processed once.

---

## Space Complexity

```text
O(n)
```

Extra space is used to store the reversed words.

---

## Concepts Used

* Two Pointers
* String Traversal
* String Slicing
* Lists
* String Joining

---

## Python Features Used

* String Slicing (`[::-1]`)
* List `append()`
* `" ".join()`

---

## Author

**Ramit Sarker**
