# Remove Two Consecutive Same

## Problem

Given a sequence of words `arr[]`, if **two consecutive words are the same**, they destroy each other.

This process continues until no two consecutive equal words remain.

Return the **number of words left** after all possible pairwise destructions.

---

## Examples

### Example 1

**Input**

```text
arr = ["ab", "aa", "aa", "bcd", "ab"]
```

**Output**

```text
3
```

**Explanation**

Initially:

```text
["ab", "aa", "aa", "bcd", "ab"]
```

The two consecutive `"aa"` words are the same, so they destroy each other:

```text
["ab", "bcd", "ab"]
```

No more consecutive equal words exist.

Therefore:

```text
3
```

words remain.

---

### Example 2

**Input**

```text
arr = ["tom", "jerry", "jerry", "tom"]
```

**Output**

```text
0
```

**Explanation**

First, the two `"jerry"` words destroy each other:

```text
["tom", "tom"]
```

Now the two `"tom"` words become consecutive and destroy each other:

```text
[]
```

Therefore:

```text
0
```

words remain.

---

# Approach

This problem can be efficiently solved using a **stack**.

The stack represents the sequence of words that remain after processing the elements seen so far.

For every word in the array:

* If the stack is empty, add the word.
* If the top of the stack is the same as the current word, remove the top element.
* Otherwise, add the current word to the stack.

The important observation is that when two equal words are removed, the elements before them can become consecutive.

The stack naturally handles this situation.

---

# Why Does the Stack Work?

Consider:

```text
["tom", "jerry", "jerry", "tom"]
```

Process from left to right.

### Step 1

Add `"tom"`:

```text
stack = ["tom"]
```

### Step 2

Add `"jerry"`:

```text
stack = ["tom", "jerry"]
```

### Step 3

Current word is `"jerry"`.

The stack top is also `"jerry"`:

```text
stack[-1] == arr[i]
```

So they destroy each other.

```text
stack = ["tom"]
```

### Step 4

Current word is `"tom"`.

The stack top is `"tom"` again.

They destroy each other:

```text
stack = []
```

The final stack is empty, so the answer is:

```text
0
```

---

# Algorithm

1. Create an empty stack.
2. Traverse the array from left to right.
3. For each word:

   * If the stack is empty, push the word.
   * Otherwise, compare it with the top of the stack.
   * If they are equal, pop the stack.
   * Otherwise, push the word.
4. Return the size of the stack.

---

# Code

```python
class Solution:
    def removeConsecutiveSame(self, arr):
        # code here
        stack = []

        for i in range(len(arr)):
            if len(stack) != 0:
                if stack[-1] == arr[i]:
                    stack.pop()
                else:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])

        return len(stack)
```

---

# Dry Run

Consider:

```text
arr = ["ab", "aa", "aa", "bcd", "ab"]
```

Initial:

```text
stack = []
```

### `"ab"`

Stack is empty, so push:

```text
stack = ["ab"]
```

### `"aa"`

`"aa"` is different from `"ab"`:

```text
stack = ["ab", "aa"]
```

### `"aa"`

The top is also `"aa"`.

Destroy the pair:

```text
stack = ["ab"]
```

### `"bcd"`

Different from `"ab"`:

```text
stack = ["ab", "bcd"]
```

### `"ab"`

Different from `"bcd"`:

```text
stack = ["ab", "bcd", "ab"]
```

Final stack:

```text
["ab", "bcd", "ab"]
```

Therefore:

```text
len(stack) = 3
```

---

# Important Observation

The stack doesn't just remove the current pair.

When a pair is removed, the element before the pair automatically becomes adjacent to the next element.

For example:

```text
["tom", "jerry", "jerry", "tom"]
```

After removing:

```text
"jerry", "jerry"
```

we get:

```text
["tom", "tom"]
```

The stack handles this automatically because after popping `"jerry"`, `"tom"` becomes the stack top.

This is why no repeated scanning or deletion of the array is required.

---

# Complexity

Let:

```text
n = len(arr)
```

### Time Complexity

We traverse the array once.

Each element is pushed at most once and popped at most once.

Therefore:

```text
O(n)
```

### Space Complexity

In the worst case, no pairs are destroyed and the stack contains all `n` elements.

Therefore:

```text
O(n)
```

---

# Key Takeaways

* Use a **stack** to simulate pairwise destruction.
* Compare every word with the **top of the stack**.
* If they are equal → **pop**.
* If they are different → **push**.
* Removing a pair automatically exposes the previous element.
* This naturally handles **chain reactions**.
* The final answer is simply `len(stack)`.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Author

**Ramit Sarker**
