# 100. Same Tree

## Problem

Given the roots of two binary trees `p` and `q`, determine whether the two trees are **exactly the same**.

Two binary trees are considered the same when:

1. They have the **same structure**.
2. Corresponding nodes contain the **same values**.

So matching values alone are not enough — the nodes must also appear in the same positions.

---

# Examples

## Example 1

![Example 1](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

**Input:**

```text
p = [1,2,3]
q = [1,2,3]
```

**Output:**

```text
true
```

Both trees are:

```text
       1              1
      / \            / \
     2   3          2   3
```

They have:

- the same structure
- the same values

Therefore:

```text
true
```

---

## Example 2

![Example 2](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

**Input:**

```text
p = [1,2]
q = [1,null,2]
```

**Output:**

```text
false
```

The trees are:

```text
       1              1
      /                \
     2                  2
```

Both contain `1` and `2`, but their **structures are different**.

Therefore:

```text
false
```

---

## Example 3

![Example 3](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

**Input:**

```text
p = [1,2,1]
q = [1,1,2]
```

**Output:**

```text
false
```

The structures are the same, but corresponding node values are different:

```text
       1              1
      / \            / \
     2   1          1   2
```

Therefore:

```text
false
```

---

# Approach

We can solve this problem using **recursion**.

The idea is to compare corresponding nodes from both trees at the same time.

For every pair of nodes `p` and `q`, there are three important situations.

### Case 1: Both Nodes Are `None`

```python
if p == None and q == None:
    return True
```

If both are `None`, both trees ended at exactly the same position.

So this part of the trees is identical.

---

### Case 2: Only One Node Is `None`

```python
if p == None or q == None:
    return False
```

If only one is `None`, the structures are different.

For example:

```text
Tree p             Tree q

   1                  1
  /                    \
 2                      2
```

At some point we compare:

```text
p = node 2
q = None
```

Since only one exists, the trees cannot be the same.

---

### Case 3: Values Are Different

```python
if p.val != q.val:
    return False
```

If both nodes exist but contain different values, the trees are not identical.

For example:

```text
p.val = 2
q.val = 5
```

Immediately:

```text
False
```

---

# Compare the Left Subtrees

If both current nodes exist and their values are equal, we compare their left children:

```python
if not fun(p.left, q.left):
    return False
```

If the left subtrees are different, there is no reason to continue.

We immediately return:

```text
False
```

---

# Compare the Right Subtrees

If the left subtrees are identical, we compare the right children:

```python
if not fun(p.right, q.right):
    return False
```

Again, if they are different:

```text
False
```

---

# If Everything Matches

If:

```text
Current values match
        +
Left subtrees match
        +
Right subtrees match
```

then:

```python
return True
```

So the basic recursive idea is:

```text
              Compare p and q
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
   Compare Left         Compare Right
   p.left, q.left       p.right, q.right
```

---

# Understanding the Base Cases

The order of the conditions is important.

## Both Are `None`

```python
if p == None and q == None:
    return True
```

Suppose:

```text
p = None
q = None
```

That means both trees ended at the same position.

So they match.

---

## One Is `None`

```python
if p == None or q == None:
    return False
```

Suppose:

```text
p = Node(2)
q = None
```

or:

```text
p = None
q = Node(2)
```

The structures are different.

So:

```text
False
```

---

## Why Check `None` Before `.val`?

We cannot immediately write:

```python
if p.val != q.val:
```

because `p` or `q` could be `None`.

A `None` object has no `.val`.

Therefore, we first handle:

```text
None cases
    ↓
Value comparison
    ↓
Recursive comparison
```

---

# Dry Run — Same Trees

Consider:

```text
Tree p              Tree q

    1                   1
   / \                 / \
  2   3               2   3
```

We call:

```python
fun(p, q)
```

---

## Step 1: Compare Root Nodes

```text
p.val = 1
q.val = 1
```

Both exist.

Values are equal.

So we compare the left children:

```python
fun(p.left, q.left)
```

---

## Step 2: Compare Node 2

```text
p.val = 2
q.val = 2
```

Values match.

Now compare their left children:

```text
p.left = None
q.left = None
```

So:

```python
fun(None, None)
```

returns:

```text
True
```

Now compare their right children:

```text
p.right = None
q.right = None
```

Again:

```python
fun(None, None)
```

returns:

```text
True
```

Therefore, the subtrees rooted at `2` are identical.

---

## Step 3: Compare Node 3

Now we return to node `1` and compare:

```python
fun(p.right, q.right)
```

We have:

```text
p.val = 3
q.val = 3
```

Their values match.

Both left children are `None`.

Both right children are `None`.

Therefore this subtree also returns:

```text
True
```

---

## Final Result

Everything matched:

```text
Root values     → Same
Left subtrees   → Same
Right subtrees  → Same
```

Therefore:

```text
True
```

---

# Recursion Tree

For:

```text
       1              1
      / \            / \
     2   3          2   3
```

the recursive calls look like:

```text
fun(1, 1)
│
├── fun(2, 2)
│   │
│   ├── fun(None, None) → True
│   └── fun(None, None) → True
│
└── fun(3, 3)
    │
    ├── fun(None, None) → True
    └── fun(None, None) → True
```

Since every comparison succeeds:

```text
fun(1,1) → True
```

---

# Dry Run — Different Structure

Consider Example 2:

```text
Tree p             Tree q

   1                  1
  /                    \
 2                      2
```

At the roots:

```text
1 == 1
```

So we compare their left children:

```python
fun(p.left, q.left)
```

Now:

```text
p.left = Node(2)
q.left = None
```

The condition:

```python
if p == None or q == None:
    return False
```

becomes true.

Therefore:

```text
False
```

is immediately returned.

There is no need to check anything else.

---

# Dry Run — Different Values

Consider:

```text
Tree p              Tree q

    1                   1
   / \                 / \
  2   3               5   3
```

Roots match:

```text
1 == 1
```

Now compare the left children:

```text
2 != 5
```

This condition becomes true:

```python
if p.val != q.val:
    return False
```

So we immediately return:

```text
False
```

---

# Why the Early Returns Are Useful

Your code uses:

```python
if not fun(p.left, q.left):
    return False
```

and:

```python
if not fun(p.right, q.right):
    return False
```

This means as soon as we discover **one difference**, we stop.

For example:

```text
             Root matches
                  |
          Left subtree
                  |
              DIFFERENT
                  ↓
             return False
```

There is no need to continue checking the remaining nodes because we already know the trees are not identical.

---

# Code

```python
class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        def fun(p, q):
            if p == None and q == None:
                return True

            if p == None or q == None:
                return False

            if p.val != q.val:
                return False

            if not fun(p.left, q.left):
                return False

            if not fun(p.right, q.right):
                return False

            return True

        return fun(p, q)
```

---

# Algorithm

1. Start by comparing the roots `p` and `q`.
2. If both nodes are `None`, return `True`.
3. If only one node is `None`, return `False`.
4. If their values are different, return `False`.
5. Recursively compare:
   ```text
   p.left with q.left
   ```
6. If the left subtrees are different, return `False`.
7. Recursively compare:
   ```text
   p.right with q.right
   ```
8. If the right subtrees are different, return `False`.
9. If everything matches, return `True`.

---

# Why Does It Work?

Two trees are identical only when **all three** of these conditions hold:

```text
1. Current nodes match
2. Left subtrees match
3. Right subtrees match
```

Your recursive function checks exactly these conditions.

Conceptually:

```text
same(p, q)
    =
same current node
    AND
same left subtree
    AND
same right subtree
```

If any one of them fails:

```text
False
```

If all of them succeed:

```text
True
```

Therefore, the algorithm correctly determines whether the entire trees are identical.

---

# Complexity

Let `n` be the number of nodes compared.

## Time Complexity

```text
O(n)
```

In the worst case, we need to compare every corresponding node in both trees.

Each node is processed once.

Therefore:

```text
Time = O(n)
```

The algorithm may finish earlier if it discovers a mismatch.

---

## Space Complexity

```text
O(h)
```

where `h` is the height of the tree.

The algorithm does not create another data structure such as a queue or list.

However, recursion uses the **call stack**.

The maximum number of recursive calls active at the same time depends on the height of the tree.

### Balanced Tree

For a balanced tree:

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

The height is approximately:

```text
h = log n
```

Therefore:

```text
Space = O(log n)
```

### Skewed Tree

For a skewed tree:

```text
1
 \
  2
   \
    3
     \
      4
```

The height can become:

```text
h = n
```

Therefore, in the worst case:

```text
Space = O(n)
```

So the general auxiliary space complexity is:

```text
O(h)
```

---

# Key Takeaways

- Two trees are the same only if both their **values and structures** are identical.
- Compare corresponding nodes from both trees simultaneously.
- If both nodes are `None`, that position matches.
- If only one node is `None`, the structures are different.
- If the node values differ, the trees are different.
- Recursively compare:
  ```text
  Left with Left
  Right with Right
  ```
- As soon as a mismatch is found, return `False`.
- Time complexity is:
  ```text
  O(n)
  ```
- Recursive auxiliary space is:
  ```text
  O(h)
  ```
  where `h` is the height of the tree.

---

## Author

**Ramit Sarker**
