# 778. Reorganize String

## Problem

Given a string `s`, rearrange its characters so that **no two adjacent characters are the same**.

Return any valid rearrangement.

If it is impossible to rearrange the string while satisfying the condition, return:

```text
""
```

---

## Examples

### Example 1

**Input**

```text
s = "aab"
```

**Output**

```text
"aba"
```

**Explanation**

The characters can be rearranged as:

```text
a b a
```

No two adjacent characters are the same.

---

### Example 2

**Input**

```text
s = "aaab"
```

**Output**

```text
""
```

**Explanation**

There are three `a`s but only one `b`.

It is impossible to arrange them without having two `a`s next to each other.

---

# Approach

We use:

1. A **Hash Map** to count the frequency of every character.
2. A **Max Heap** to always select the character with the highest remaining frequency.

Python's `heapq` is a **min heap**, so we store the frequency as a negative number to simulate a max heap.

For example:

```text
a → 3
b → 2
c → 1
```

is stored as:

```text
[-3, 'a']
[-2, 'b']
[-1, 'c']
```

The character with the highest frequency will be at the top.

---

# Why Use a Max Heap?

At every step, we want to use the character that has the **highest remaining frequency**.

For example:

```text
a → 3
b → 2
c → 1
```

The heap gives us:

```text
a
```

first because it occurs most frequently.

This helps distribute the most frequent characters across the string.

---

# The Main Problem

There is one important situation we need to handle.

Suppose the result currently ends with:

```text
"a"
```

and the most frequent character in the heap is also:

```text
"a"
```

We cannot use it immediately because that would create:

```text
"aa"
```

So we temporarily choose the **next most frequent character**.

For example:

```text
ans = "a"
```

and heap:

```text
a → 2
b → 1
```

We cannot choose `a`.

So we choose:

```text
b
```

giving:

```text
"ab"
```

Then we put `a` back into the heap.

---

# Important Idea

The algorithm follows this rule:

```text
Most frequent character
        ↓
Is it different from last character?
        ↓
      YES
        ↓
Use it
```

If it is the same:

```text
Most frequent character
        ↓
Same as last character
        ↓
Take the second most frequent character
        ↓
Use it
        ↓
Put the first character back
```

---

# Why Put `current` Back?

Suppose:

```text
ans = "a"
```

and:

```text
current = "a"
other = "b"
```

We cannot use `current` because it would produce:

```text
"aa"
```

So we use `b`:

```text
"ab"
```

But `a` still has remaining occurrences.

Therefore, we must put `a` back into the heap so it can be used later:

```python
heapq.heappush(heap, current)
```

This is very important.

---

# Algorithm

### Step 1: Count Frequencies

Create a hash map:

```python
hash_map = {}
```

For every character:

```python
if i in hash_map:
    hash_map[i] += 1
else:
    hash_map[i] = 1
```

---

### Step 2: Build a Max Heap

For every character, push:

```python
[-frequency, character]
```

into the heap.

Example:

```text
a → 3
b → 2
c → 1
```

becomes:

```text
[-3, 'a']
[-2, 'b']
[-1, 'c']
```

---

### Step 3: Build the Answer

While the answer is not complete:

```python
while len(ans) < len(s):
```

take the most frequent character:

```python
current = heapq.heappop(heap)
```

---

### Step 4: Check the Previous Character

If:

```python
not ans or ans[-1] != current[1]
```

we can safely use the character.

Add it:

```python
ans.append(current[1])
```

Then decrease its frequency:

```python
current[0] += 1
```

Because frequencies are stored as negative values.

For example:

```text
-3 → -2
```

means:

```text
3 occurrences → 2 occurrences
```

If it still has occurrences remaining, put it back:

```python
if current[0] != 0:
    heapq.heappush(heap, current)
```

---

# What If the Character Is the Same?

Suppose:

```python
ans[-1] == current[1]
```

We cannot use `current`.

So we check whether another character exists:

```python
if not heap:
    return ""
```

If the heap is empty, there is no other character available.

Therefore, a valid rearrangement is impossible.

Otherwise:

```python
other = heapq.heappop(heap)
```

We use `other` instead.

Then we decrease its frequency:

```python
other[0] += 1
```

If it still has occurrences remaining, push it back.

Finally, put `current` back:

```python
heapq.heappush(heap, current)
```

so that it can be used in a later position.

---

# Code

```python
import heapq

class Solution:

    def reorganizeString(self, s: str) -> str:

        heap = []
        hash_map = {}
        ans = []

        # Count frequencies
        for i in s:

            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        # Build max heap using negative frequencies
        for i in hash_map:
            heapq.heappush(heap, [-hash_map[i], i])

        # Build the answer
        while len(ans) < len(s):

            current = heapq.heappop(heap)

            if not ans or ans[-1] != current[1]:

                ans.append(current[1])

                current[0] += 1

                if current[0] != 0:
                    heapq.heappush(heap, current)

            else:

                if not heap:
                    return ""

                other = heapq.heappop(heap)

                ans.append(other[1])

                other[0] += 1

                if other[0] != 0:
                    heapq.heappush(heap, other)

                heapq.heappush(heap, current)

        return ''.join(ans)
```

---

# Dry Run

Consider:

```text
s = "aab"
```

---

## Step 1: Frequency Map

```text
a → 2
b → 1
```

---

## Step 2: Max Heap

Because we use negative frequencies:

```text
[-2, 'a']
[-1, 'b']
```

The top is:

```text
a
```

---

## Step 3: First Character

Pop:

```text
current = [-2, 'a']
```

The answer is empty, so we can use `a`.

```text
ans = ["a"]
```

Decrease frequency:

```text
-2 → -1
```

Push it back:

```text
[-1, 'a']
[-1, 'b']
```

---

## Step 4: Second Character

Suppose `a` is selected again.

We now have:

```text
ans = "a"
current = "a"
```

We cannot add `a` because:

```text
"aa"
```

would be invalid.

So we take:

```text
other = "b"
```

Add it:

```text
ans = "ab"
```

`b` has no occurrences left.

Now put `a` back into the heap.

Heap:

```text
[-1, 'a']
```

---

## Step 5: Third Character

Take:

```text
a
```

Now:

```text
ans = "aba"
```

All characters have been used.

Return:

```text
"aba"
```

---

# Dry Run: Impossible Case

Consider:

```text
s = "aaab"
```

Frequency:

```text
a → 3
b → 1
```

Heap:

```text
[-3, 'a']
[-1, 'b']
```

We can start:

```text
a
```

Then:

```text
ab
```

Now `a` is available again:

```text
aba
```

But one `a` remains.

There is no other character available to separate it from the previous `a`.

Eventually:

```text
current = 'a'
ans[-1] = 'a'
heap = []
```

The code reaches:

```python
if not heap:
    return ""
```

Therefore:

```text
""
```

is returned.

---

# Understanding the Most Important Part

This section is the key to understanding your code:

```python
else:
    if not heap:
        return ""

    other = heapq.heappop(heap)
    ans.append(other[1])

    other[0] += 1

    if other[0] != 0:
        heapq.heappush(heap, other)

    heapq.heappush(heap, current)
```

Suppose:

```text
ans = "a"
current = "a"
```

We cannot use `current`.

So:

```python
other = heapq.heappop(heap)
```

gets another character.

For example:

```text
other = "b"
```

We add it:

```python
ans.append(other[1])
```

Now:

```text
ans = "ab"
```

Then we decrease the frequency of `b`.

Finally:

```python
heapq.heappush(heap, current)
```

puts the original `a` back into the heap.

Why?

Because we didn't use `a`; we only postponed it.

---

# Why Can We Return `""`?

If:

```text
current == last character
```

and:

```text
heap is empty
```

there is no different character available to separate the repeated character.

For example:

```text
ans = "aa"
remaining = "a"
```

The only possible next character is `a`.

That would produce:

```text
"aaa"
```

which violates the condition.

Therefore, no valid rearrangement exists.

---

# Important Observation

A string is impossible to reorganize when one character occurs too many times.

For example:

```text
"aaab"
```

There are:

```text
a → 3
b → 1
```

The `a`s need spaces between them:

```text
a _ a _ a
```

But we only have one `b` to fill the spaces:

```text
a b a _ a
```

One `a` is still forced next to another `a`.

Therefore, the answer is impossible.

---

# Why Use a Max Heap?

We always want to use the character with the highest remaining frequency.

This helps prevent a highly frequent character from being left until the end, where it may become impossible to place.

The heap allows us to efficiently choose the most frequent available character.

---

# Complexity

Let:

```text
n = len(s)
```

There are at most `26` unique lowercase English letters.

### Building the Frequency Map

We traverse the string once:

```text
O(n)
```

### Building the Heap

There are at most `26` characters:

```text
O(26 log 26)
```

which is effectively:

```text
O(1)
```

### Building the Answer

For every character, we perform heap operations.

In general:

```text
O(n log 26)
```

Since `26` is constant:

```text
O(n)
```

### Overall Time Complexity

```text
O(n)
```

### Space Complexity

The answer uses `O(n)` space, while the heap and frequency map contain at most `26` characters.

Therefore:

```text
O(n)
```

including the output.

---

# Key Takeaways

* Use a **Hash Map** to count character frequencies.
* Use a **Max Heap** to always choose the most frequent character.
* Python's `heapq` is a min heap, so use **negative frequencies**.
* Never place the same character directly after itself.
* If the most frequent character is the same as the previous character, temporarily use the second most frequent character.
* Put the skipped character back into the heap afterward.
* If there is no alternative character available, return `""`.
* **Time Complexity:** `O(n)` for lowercase English letters.
* **Space Complexity:** `O(n)` including the result.

---

## Author

**Ramit Sarker**
