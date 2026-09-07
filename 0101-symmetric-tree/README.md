# 101. Symmetric Tree

## Problem

Given the `root` of a binary tree, check whether it is a **mirror of itself**.

In other words, we need to determine whether the tree is **symmetric around its center**.

For a tree to be symmetric:

- The left and right sides must have the same structure.
- Corresponding nodes on opposite sides must have the same values.
- The left child of one side must correspond to the right child of the other side.
- The right child of one side must correspond to the left child of the other side.

The key idea is to compare the **left subtree and right subtree as mirror images**.

---

# Examples

## Example 1

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

**Input:**

```text id="9p9z2x"
root = [1,2,2,3,4,4,3]
```

**Output:**

```text id="v75q9x"
true
```

The tree is symmetric around its center.

The left side:

```text id="v8yq0r"
    2
   / \
  3   4
```

is the mirror image of the right side:

```text id="0pl3xr"
    2
   / \
  4   3
```

Therefore, the answer is `true`.

---

## Example 2

![Example 2](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

**Input:**

```text id="jj1w6p"
root = [1,2,2,null,3,null,3]
```

**Output:**

```text id="8z3b0c"
false
```

The values `3` exist on both sides, but they are positioned differently.

Therefore, the two sides are not mirror images.

---

# Approach

We can solve this problem using **recursion**.

The important idea is that we don't simply compare:

```text id="0xq47d"
left ↔ left
right ↔ right
```

Instead, because we need a **mirror**, we compare:

```text id="v9b6w4"
left ↔ right
right ↔ left
```

So if we have:

```text id="g7f8q4"
       1
      / \
     2   2
    / \ / \
   3  4 4  3
```

we compare:

```text id="8g5f4e"
3 ↔ 3
4 ↔ 4
```

The recursive comparisons are:

```python id="9p6j4w"
fun(p.left, q.right)
fun(p.right, q.left)
```

This is the main trick of the solution.

---

# Understanding the Code

First, we take the two children of the root:

```python id="z9y0wb"
p = root.left
q = root.right
```

Now:

```text id="6xqf9b"
p = left side of the tree
q = right side of the tree
```

We then define a recursive function:

```python id="4l8pby"
def fun(p, q):
```

This function checks whether the two given subtrees are mirror images of each other.

---

# Step 1: Both Nodes Are `None`

```python id="n9m5cs"
if p == None and q == None:
    return True
```

If both nodes are `None`, then both sides ended at the same position.

For example:

```text id="f4p1se"
Left side:       Right side:

   3                 3
  / \               / \
None None          None None
```

When we compare:

```text id="7y7e2s"
fun(None, None)
```

both sides are empty at that position.

Therefore:

```text id="3h2l3e"
True
```

---

# Step 2: Only One Node Is `None`

```python id="4fd0ot"
if p == None or q == None:
    return False
```

If one node exists but the corresponding mirror position on the other side does not exist, the tree cannot be symmetric.

For example:

```text id="u0t8qr"
Left side:       Right side:

    2                2
   /                  \
  3                    3
```

When comparing the corresponding positions:

```text id="h8z6ay"
p = 3
q = None
```

the structures are different.

Therefore:

```text id="9k0f1v"
False
```

---

# Step 3: Compare Values

```python id="4f0w6x"
if p.val != q.val:
    return False
```

If both nodes exist, their values must be equal.

For example:

```text id="u9q7o2"
p = 3
q = 4
```

Since:

```text id="5j5r7s"
3 != 4
```

the tree is not symmetric.

So we immediately return:

```text id="2cvw8x"
False
```

---

# Step 4: Compare Opposite Children

This is the most important part of the solution.

Your code does:

```python id="z2u4fs"
if not fun(p.left, q.right):
    return False
```

Notice:

```text id="3h9gk4"
p.left ↔ q.right
```

not:

```text id="q4q0p7"
p.left ↔ q.left
```

This is because we are checking for a **mirror**.

Then:

```python id="6l9h1c"
if not fun(p.right, q.left):
    return False
```

So:

```text id="c8a6lo"
p.right ↔ q.left
```

Together:

```text id="3i4qkl"
        p                 q

       / \               / \
      A   B             C   D

Compare:

      A ↔ D
      B ↔ C
```

This is exactly what mirror symmetry requires.

---

# Step 5: Everything Matches

If all the checks pass:

```python id="6q3q5c"
return True
```

That means:

```text id="d3j9yu"
✓ Both nodes exist or both are None
✓ Their values match
✓ Their outer children match
✓ Their inner children match
```

Therefore, the two subtrees are mirror images.

---

# Why `p.left` Is Compared With `q.right`

This is the most important concept in this problem.

Suppose we have:

```text id="h5xj56"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

Look at the left and right sides.

For the left `2`:

```text id="z1y0r5"
left child  = 3
right child = 4
```

For the right `2`:

```text id="9ax4ap"
left child  = 4
right child = 3
```

Because the tree is a mirror:

```text id="k7d9h4"
left 2's left  → right 2's right
      3         →       3

left 2's right → right 2's left
      4         →       4
```

Therefore:

```python id="az0mjm"
fun(p.left, q.right)
fun(p.right, q.left)
```

is exactly what we need.

---

# Dry Run

Let's use Example 1:

```text id="8o7mqs"
root = [1,2,2,3,4,4,3]
```

Tree:

```text id="m3t0na"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

First:

```python id="8qz4rh"
p = root.left
q = root.right
```

So:

```text id="5z6qfw"
p = 2
q = 2
```

Call:

```python id="5y25mg"
fun(2,2)
```

---

## Compare the Root's Two Children

Both nodes exist.

Their values are:

```text id="ym1p6z"
p.val = 2
q.val = 2
```

So they match.

Now compare:

```python id="5t6d3w"
fun(p.left, q.right)
```

This becomes:

```text id="9o3n9g"
fun(3,3)
```

---

## Compare `3` and `3`

Both values match:

```text id="o0r4z6"
3 == 3
```

Compare their children:

```text id="g6fl8p"
fun(None, None)
```

returns `True`.

The other pair:

```text id="q4b3y2"
fun(None, None)
```

also returns `True`.

Therefore:

```text id="x3k9cv"
fun(3,3) → True
```

---

## Compare `4` and `4`

Now the second comparison:

```python id="r0jz9m"
fun(p.right, q.left)
```

becomes:

```text id="d9q5yr"
fun(4,4)
```

Again:

```text id="4v6x71"
4 == 4
```

Both children are `None`, so both recursive calls return `True`.

Therefore:

```text id="5k1e4a"
fun(4,4) → True
```

---

## Final Result

We have:

```text id="x7u1x3"
fun(2,2)

        /          \
       /            \
   fun(3,3)       fun(4,4)
       ↓              ↓
     True           True
```

Both sides match.

Therefore:

```text id="8y6l9a"
fun(2,2) → True
```

and finally:

```text id="v1d7rx"
return True
```

The tree is symmetric.

---

# Dry Run When the Tree Is Not Symmetric

Consider Example 2:

```text id="0l7f4a"
root = [1,2,2,null,3,null,3]
```

The tree is:

```text id="j6w1i9"
        1
       / \
      2   2
       \   \
        3   3
```

We start with:

```text id="8y9l4j"
p = 2
q = 2
```

Their values match.

Now compare:

```python id="7v6h1x"
fun(p.left, q.right)
```

Here:

```text id="o4t7y5"
p.left  = None
q.right = 3
```

So we call:

```text id="a1p3k8"
fun(None, 3)
```

The first condition:

```python id="5r4b6p"
p == None and q == None
```

is false.

Then:

```python id="1k1f2d"
p == None or q == None
```

is true.

Therefore:

```text id="d8z9ye"
return False
```

The entire function returns `False`.

So the tree is not symmetric.

---

# Recursion Flow

For the symmetric tree:

```text id="r3k4yz"
             fun(2,2)
              /    \
             /      \
      fun(3,3)      fun(4,4)
        / \           / \
       T   T         T   T
```

The important thing is that the pairs are mirrored:

```text id="a8h3w2"
p.left  ↔ q.right
p.right ↔ q.left
```

---

# Why Does It Work?

A tree is symmetric if its left and right subtrees are **mirror images**.

For two nodes `p` and `q` to be mirrors:

1. Both must be `None`, or both must exist.
2. Their values must be equal.
3. `p.left` must mirror `q.right`.
4. `p.right` must mirror `q.left`.

Your recursive function checks exactly these four conditions.

The recursive calls:

```python id="c8f7x2"
fun(p.left, q.right)
fun(p.right, q.left)
```

continue this mirror comparison all the way down the tree.

If even one pair does not match, the function immediately returns `False`.

If every pair matches, the tree is symmetric and the function returns `True`.

---

# Algorithm

1. Take the root's left child as `p`.
2. Take the root's right child as `q`.
3. Define a recursive function `fun(p, q)`.
4. If both `p` and `q` are `None`, return `True`.
5. If only one is `None`, return `False`.
6. If their values are different, return `False`.
7. Compare `p.left` with `q.right`.
8. Compare `p.right` with `q.left`.
9. If both comparisons succeed, return `True`.
10. Return the result of `fun(root.left, root.right)`.

---

# Code

```python id="1u6v5a"
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right

        def fun(p, q):
            if p == None and q == None:
                return True

            if p == None or q == None:
                return False

            if p.val != q.val:
                return False

            if not fun(p.left, q.right):
                return False

            if not fun(p.right, q.left):
                return False

            return True

        return fun(p, q)
```

---

# Complexity

Let `n` be the number of nodes in the tree.

## Time Complexity

```text id="3k9u4h"
O(n)
```

In the worst case, every node needs to be compared with its mirror node.

Each node is processed at most once.

Therefore:

```text id="r7f4mz"
Time Complexity = O(n)
```

---

## Space Complexity

```text id="8c0l9f"
O(h)
```

where `h` is the height of the tree.

This space is used by the recursive call stack.

For a balanced tree:

```text id="9w6n4e"
O(log n)
```

For a completely skewed tree:

```text id="p5f2ka"
O(n)
```

So the worst-case auxiliary space is:

```text id="e1m8s7"
O(n)
```

---

# Key Takeaways

- A symmetric tree is a **mirror of itself**.
- We compare the left and right subtrees as mirror images.
- The comparison is:
  ```text
  left ↔ right
  right ↔ left
  ```
- The most important recursive calls are:
  ```python
  fun(p.left, q.right)
  fun(p.right, q.left)
  ```
- Both `None` means the current positions match.
- Only one `None` means the structures are different.
- Corresponding mirror nodes must have the same value.
- The recursion checks the entire tree pair by pair.
- Time complexity is `O(n)`.
- Recursive auxiliary space is `O(h)`.
- The follow-up asks for an **iterative** solution, which can be implemented using a queue or stack.

---

## Author

**Ramit Sarker**
