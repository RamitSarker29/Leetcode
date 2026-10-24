# 49. Group Anagrams

## Problem

Given an array of strings `strs`, group all **anagrams** together.

Anagrams are strings that contain the same characters with the same frequencies, but the characters may appear in a different order.

For example:

```text
"eat", "tea", "ate"
```

All three strings contain:

```text
a → 1 time
e → 1 time
t → 1 time
```

Therefore, they belong to the same group.

Return the groups in any order.

---

# Examples

## Example 1

```text
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

Explanation:

- `"eat"`, `"tea"`, and `"ate"` are anagrams.
- `"tan"` and `"nat"` are anagrams.
- `"bat"` has no other anagram in the array.

The order of the groups and the strings inside each group does not matter.

## Example 2

```text
Input: strs = [""]
Output: [[""]]
```

The empty string forms a group of its own.

## Example 3

```text
Input: strs = ["a"]
Output: [["a"]]
```

There is only one string, so the result contains one group.

---

# Approach

Your solution uses a **hash map of character frequencies** to identify anagrams.

Instead of sorting every string, you count how many times each letter appears.

Since the problem guarantees that strings contain only lowercase English letters, we use a list of size `26`.

For every string:

1. Create a list of 26 zeros.
2. Count the frequency of each character.
3. Convert the frequency list into a tuple.
4. Use that tuple as a dictionary key.
5. If the key does not exist, create an empty group.
6. Append the current string to that group.
7. Finally, return all the groups.

### Main Idea

Anagrams have identical character frequencies.

For example:

```text
"eat" → a:1, e:1, t:1
"tea" → a:1, e:1, t:1
"ate" → a:1, e:1, t:1
```

All three strings generate the same frequency key, so they are placed in the same group.

---

# Code

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for i in range(len(strs)):
            hash_map = [0] * 26

            for j in range(len(strs[i])):
                char = strs[i][j]
                hash_map[ord(char) - ord('a')] += 1

            key = tuple(hash_map)

            if key not in groups:
                groups[key] = []

            groups[key].append(strs[i])

        return list(groups.values())
```

---

# Code Explanation

## 1. Create the Dictionary

```python
groups = {}
```

This dictionary stores the anagram groups.

- **Key:** A tuple containing the character frequencies.
- **Value:** A list containing strings with those frequencies.

For example, conceptually:

```text
groups = {
    frequency_key_1: ["eat", "tea", "ate"],
    frequency_key_2: ["tan", "nat"],
    frequency_key_3: ["bat"]
}
```

The actual keys are tuples of 26 numbers, not names such as `frequency_key_1`.

---

## 2. Traverse Every String

```python
for i in range(len(strs)):
```

This loop processes every string in the input array.

For example:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

The variable `i` moves through the indices:

```text
i = 0 → "eat"
i = 1 → "tea"
i = 2 → "tan"
i = 3 → "ate"
i = 4 → "nat"
i = 5 → "bat"
```

Each string gets its own frequency list.

---

## 3. Create a Frequency List

```python
hash_map = [0] * 26
```

This creates a list containing 26 zeros.

```text
[0, 0, 0, 0, ..., 0]
```

Why 26?

Because the problem guarantees lowercase English letters:

```text
a, b, c, ..., z
```

Each position represents one letter:

| Index | Character |
|---:|:---|
| 0 | a |
| 1 | b |
| 2 | c |
| 3 | d |
| ... | ... |
| 25 | z |

Initially, every letter has a frequency of zero.

For the string `"eat"`, we will increment the positions corresponding to `e`, `a`, and `t`.

---

## 4. Traverse the Characters of the String

```python
for j in range(len(strs[i])):
```

This loop visits each character in the current string.

For example, if:

```python
strs[i] = "eat"
```

then:

```text
j = 0 → "e"
j = 1 → "a"
j = 2 → "t"
```

---

## 5. Get the Current Character

```python
char = strs[i][j]
```

This extracts the character at index `j` from the current string.

For `"eat"`:

```text
j = 0 → char = "e"
j = 1 → char = "a"
j = 2 → char = "t"
```

---

## 6. Convert the Character Into an Index

```python
hash_map[ord(char) - ord('a')] += 1
```

This is the most important line for building the frequency list.

### What does `ord()` do?

Python's `ord()` returns the Unicode code point of a character.

For lowercase English letters, the code points are consecutive:

```text
ord('a') = 97
ord('b') = 98
ord('c') = 99
...
ord('z') = 122
```

Therefore:

```python
ord(char) - ord('a')
```

converts a lowercase letter into an index from `0` to `25`.

For example:

```text
char = "a"

ord("a") - ord("a")
= 97 - 97
= 0
```

So `"a"` uses index `0`.

For `"e"`:

```text
ord("e") - ord("a")
= 101 - 97
= 4
```

So `"e"` uses index `4`.

For `"t"`:

```text
ord("t") - ord("a")
= 116 - 97
= 19
```

So `"t"` uses index `19`.

The statement then increments the corresponding frequency by one.

---

# Understanding the Frequency List

Consider:

```python
strs[i] = "eat"
```

Initially:

```text
hash_map = [0, 0, 0, 0, 0, ..., 0]
```

### Process `"e"`

```python
hash_map[ord("e") - ord("a")] += 1
```

Index `4` is incremented.

```text
e → frequency 1
```

### Process `"a"`

Index `0` is incremented.

```text
a → frequency 1
e → frequency 1
```

### Process `"t"`

Index `19` is incremented.

```text
a → frequency 1
e → frequency 1
t → frequency 1
```

The final list has:

```text
index 0  → 1   (a)
index 4  → 1   (e)
index 19 → 1   (t)
all other indices → 0
```

The frequency list now represents the character composition of `"eat"`.

---

## 7. Convert the List Into a Tuple

```python
key = tuple(hash_map)
```

This line converts the frequency list into a tuple.

For example:

```python
hash_map = [1, 0, 0, 0, 1, ..., 1, ..., 0]
```

After conversion:

```python
key = (1, 0, 0, 0, 1, ..., 1, ..., 0)
```

The tuple contains the same frequency values as the list.

### Why do we need a tuple?

Python dictionary keys must be hashable. A list is mutable and cannot be used as a dictionary key.

For example, this is invalid:

```python
groups[hash_map] = []
```

because `hash_map` is a list.

But this works:

```python
key = tuple(hash_map)
groups[key] = []
```

A tuple of integers is hashable, so it can be used as a dictionary key.

**Most importantly:** Every anagram has the same frequency tuple.

For example:

```text
"eat" → same frequency tuple
"tea" → same frequency tuple
"ate" → same frequency tuple
```

The letters occur in a different order, but their frequencies are identical.

---

# 8. Check Whether the Group Exists

```python
if key not in groups:
    groups[key] = []
```

This checks whether the current frequency tuple already exists in `groups`.

If the key is not present, we create a new empty list for that group.

For the first string `"eat"`, the key does not exist yet.

So we create:

```python
groups[key] = []
```

Conceptually:

```text
groups = {
    key_for_eat: []
}
```

The empty list is ready to hold the strings belonging to this group.

---

# 9. Add the String to Its Group

```python
groups[key].append(strs[i])
```

This appends the current string to the list associated with its frequency key.

For `"eat"`:

```text
groups[key] = ["eat"]
```

When `"tea"` is processed, it generates the same key.

The key already exists, so no new group is created.

The string is appended to the existing group:

```text
groups[key] = ["eat", "tea"]
```

When `"ate"` is processed:

```text
groups[key] = ["eat", "tea", "ate"]
```

All three strings are grouped together automatically.

---

# Why Does `groups[key] = []` Not Overwrite the Existing Group?

Consider these lines:

```python
if key not in groups:
    groups[key] = []

groups[key].append(strs[i])
```

The dictionary only creates a new list when the key does not exist.

When another anagram generates the same key, the condition is false.

Therefore, the existing list is preserved, and the new string is appended to it.

For example:

```text
Process "eat":
key does not exist → create []
append "eat"       → ["eat"]

Process "tea":
key exists         → keep existing list
append "tea"       → ["eat", "tea"]

Process "ate":
key exists         → keep existing list
append "ate"       → ["eat", "tea", "ate"]
```

This is how the dictionary builds each group.

---

# 10. Return the Groups

```python
return list(groups.values())
```

The dictionary contains frequency tuples as keys and lists of anagrams as values.

For example:

```python
groups = {
    key1: ["eat", "tea", "ate"],
    key2: ["tan", "nat"],
    key3: ["bat"]
}
```

Calling:

```python
groups.values()
```

gives the collection of group lists.

Wrapping it with `list()` converts those values into a list:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

That is the required output format.

The order may differ because the problem allows any order.

---

# Dry Run

Consider:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

### Step 1: Process `"eat"`

Frequency:

```text
a → 1
e → 1
t → 1
```

Create its tuple key.

The key does not exist, so create a group and append `"eat"`.

```text
groups = {
    key_A: ["eat"]
}
```

Here, `key_A` is shorthand for the actual 26-number tuple.

### Step 2: Process `"tea"`

Frequency:

```text
a → 1
e → 1
t → 1
```

Its tuple is identical to the tuple for `"eat"`.

The key already exists, so append `"tea"`.

```text
groups = {
    key_A: ["eat", "tea"]
}
```

### Step 3: Process `"tan"`

Frequency:

```text
a → 1
n → 1
t → 1
```

This produces a different tuple.

Create a new group:

```text
groups = {
    key_A: ["eat", "tea"],
    key_B: ["tan"]
}
```

### Step 4: Process `"ate"`

Its character frequencies match `"eat"` and `"tea"`.

Append it to `key_A`:

```text
key_A → ["eat", "tea", "ate"]
```

### Step 5: Process `"nat"`

Its frequencies match `"tan"`.

Append it to `key_B`:

```text
key_B → ["tan", "nat"]
```

### Step 6: Process `"bat"`

Its frequencies differ from every previous string.

Create a new group:

```text
key_C → ["bat"]
```

### Final Dictionary

Conceptually:

```text
groups = {
    key_A: ["eat", "tea", "ate"],
    key_B: ["tan", "nat"],
    key_C: ["bat"]
}
```

### Final Output

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

The order of groups and strings is not important.

---

# Why Does It Work?

Two strings are anagrams if and only if each character appears the same number of times in both strings.

Your algorithm creates a 26-element frequency list for every string.

Because each position corresponds to a particular letter, two strings with identical character frequencies produce identical lists and therefore identical tuple keys.

The dictionary uses these keys to identify which strings belong together.

- If a key is new, a new group is created.
- If a key already exists, the string is appended to the existing group.

Thus, every string is placed into the group containing exactly its anagrams.

---

# Algorithm

1. Create an empty dictionary called `groups`.
2. Traverse each string in `strs`.
3. Create a frequency list of 26 zeros.
4. Traverse the current string and count each character using `ord(char) - ord('a')`.
5. Convert the frequency list into a tuple.
6. If the tuple is not a key in `groups`, create an empty list for it.
7. Append the current string to the list associated with the tuple.
8. Return `list(groups.values())`.

---

# Complexity Analysis

Let:

- `n` = number of strings
- `m` = maximum length of a string

### Time Complexity

For each string, the algorithm:

- Creates a list of 26 zeros.
- Counts its characters in `O(m)` time.
- Converts the frequency list into a tuple of 26 values.
- Performs dictionary operations using the tuple key.

Since the alphabet size is fixed at 26, creating and converting the frequency list take constant time.

Therefore, the overall expected time complexity is:

```text
O(n × m)
```

### Space Complexity

Each string has a frequency list of size 26, which requires constant auxiliary space.

The dictionary stores one key per distinct anagram group and stores all input strings in its values.

Therefore, the overall space complexity, including the returned groups, is:

```text
O(n × m)
```

The auxiliary frequency-counting space per string is:

```text
O(1)
```

because the frequency list always has exactly 26 entries.

---

# Concepts Used

- Hash maps / dictionaries
- Character frequency counting
- Hashable dictionary keys
- Tuples
- ASCII-compatible character indexing using `ord()`
- Nested loops
- Grouping by a common key
- Lists and `append()`

---

# Python Features Used

### List Initialization

```python
hash_map = [0] * 26
```

Creates a list of 26 zeros.

### `ord()`

```python
ord(char) - ord('a')
```

Converts a lowercase letter into its index from `0` to `25`.

### `tuple()`

```python
key = tuple(hash_map)
```

Converts the frequency list into an immutable, hashable tuple suitable for use as a dictionary key.

### Dictionary Membership

```python
if key not in groups:
```

Checks whether a group for the current frequency pattern already exists.

### Dictionary Insertion

```python
groups[key] = []
```

Creates a new group when the key is encountered for the first time.

### List `append()`

```python
groups[key].append(strs[i])
```

Adds the current string to its anagram group.

### Dictionary `values()`

```python
list(groups.values())
```

Collects all group lists into the final result.

---

# Key Takeaways

- Anagrams contain exactly the same characters with the same frequencies.
- A 26-element list efficiently represents lowercase English letter frequencies.
- `ord(char) - ord('a')` maps each lowercase letter to an index from `0` to `25`.
- `tuple(hash_map)` converts the mutable frequency list into a hashable dictionary key.
- Identical frequency tuples identify anagrams.
- A new key creates a new group; an existing key reuses its group.
- The algorithm avoids sorting each string and runs in expected **O(n × m)** time.
- The dictionary stores the groups, so the overall space complexity is **O(n × m)**, including the result.

---

# Author

**Ramit Sarker**
