# 236. Lowest Common Ancestor of a Binary Tree

## Problem

Given a binary tree, find the **Lowest Common Ancestor (LCA)** of two given nodes `p` and `q`.

The **Lowest Common Ancestor** of two nodes is the lowest node in the tree that has both `p` and `q` as descendants.

A node is also considered a descendant of **itself**.

The main goal is to find the **deepest node** that contains both `p` and `q` somewhere below it.

---

# Example 1

![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**Input:**

```text id="8p7y4w"
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
```

**Output:**

```text id="w6a8z3"
3
```

**Explanation:**

The LCA of nodes `5` and `1` is `3`.

The tree can be visualized as:

```text id="6u2m8v"
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

Node `3` has both `5` and `1` as descendants.

Therefore:

```text id="h3k4qz"
LCA(5, 1) = 3
```

---

# Example 2

![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**Input:**

```text id="t8q2n1"
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4
```

**Output:**

```text id="0x9s6a"
5
```

**Explanation:**

Node `4` is inside the subtree rooted at `5`.

Since a node is allowed to be a descendant of itself, node `5` can be the LCA.

Therefore:

```text id="p2c8kd"
LCA(5, 4) = 5
```

---

# Example 3

**Input:**

```text id="q0t3j8"
root = [1,2]
p = 1
q = 2
```

**Output:**

```text id="c6n4x1"
1
```

Since `1` is the root and `2` is its descendant:

```text id="f3r7v2"
LCA(1,2) = 1
```

---

# Approach

We can solve this problem using **recursion**.

The main idea is to recursively search the tree for `p` and `q`.

For every node, we ask:

```text id="w9m2c5"
Does the left subtree contain p or q?
Does the right subtree contain p or q?
```

There are several important cases.

### Case 1: Current node is `None`

There is nothing to search:

```python id="7z3k1a"
if root == None:
    return None
```

---

### Case 2: Current node is `p` or `q`

If we find either target:

```python id="k4p8s2"
if p == root or q == root:
    return root
```

we return that node immediately.

This is also important for cases like Example 2, where `p` itself is the LCA.

---

### Case 3: Both subtrees find something

We recursively search both sides:

```python id="q8v2m4"
left = fun(root.left)
right = fun(root.right)
```

If both are non-`None`:

```python id="h1s7x9"
if left != None and right != None:
    return root
```

then one target was found on the left and the other on the right.

Therefore, the current node is their **Lowest Common Ancestor**.

---

### Case 4: Only the left subtree finds something

```python id="m7c4p8"
if left != None:
    return left
```

This means the LCA has not been determined yet, but one of the target nodes exists somewhere in the left subtree.

So we pass that result upward.

---

### Case 5: Only the right subtree finds something

```python id="r2x6v9"
if right != None:
    return right
```

Similarly, we return whatever was found in the right subtree.

---

# Understanding the Code

Your solution uses a nested recursive function:

```python id="s4k8p1"
def fun(root):
```

The function returns:

```text id="t9v3q6"
None
```

if neither `p` nor `q` is found in that subtree.

Otherwise, it returns a node that could be:

- `p`
- `q`
- or the LCA

---

# Step 1: Base Case

```python id="c8n5m3"
if root == None:
    return None
```

If we reach an empty position, there is nothing to find.

So we return `None`.

---

# Step 2: Check Whether We Found `p` or `q`

```python id="y6r2k9"
if p == root or q == root:
    return root
```

If the current node is either target, return it.

For example, if:

```text id="x8f3d2"
root = 5
p = 5
```

then:

```text id="v5j7q1"
p == root
```

is true.

So we return node `5`.

This handles the important case where one target is an ancestor of the other.

---

# Step 3: Search the Left and Right Subtrees

```python id="n7m4b8"
left = fun(root.left)
right = fun(root.right)
```

We recursively search both subtrees.

After these calls:

```text id="e2c6p9"
left  = result from left subtree
right = result from right subtree
```

The result can be:

```text id="v8s2l5"
None
p
q
or LCA
```

---

# Step 4: Both Sides Found a Node

```python id="j3k7x1"
if left != None and right != None:
    return root
```

This is the most important condition.

Suppose:

```text id="w4m9z2"
          root
         /    \
        p      q
```

The left recursion finds `p`:

```text id="a7c3f8"
left = p
```

The right recursion finds `q`:

```text id="b6v2n9"
right = q
```

Therefore:

```text id="s1d8k4"
left != None
right != None
```

This means `p` and `q` are located in different subtrees of the current node.

So the current node is their common ancestor.

Because we are returning from the deepest recursive calls upward, this is the **lowest** common ancestor.

---

# Step 5: Only Left Side Found Something

```python id="p6y2m8"
if left != None:
    return left
```

If the left subtree found a target or an LCA, while the right subtree found nothing, we return the left result.

This allows the useful result to travel upward through the recursion.

---

# Step 6: Only Right Side Found Something

```python id="q5x9m3"
if right != None:
    return right
```

Same idea for the right subtree.

---

# Step 7: Return the Recursive Result

Finally:

```python id="k8v3z6"
return fun(root)
```

starts the recursive search from the root of the tree.

---

# Dry Run

Let's use Example 1:

```text id="3h8q1m"
p = 5
q = 1
```

Tree:

```text id="7m4c9x"
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

We start:

```text id="0s6k2p"
fun(3)
```

---

## At Node 3

Node `3` is neither `p` nor `q`.

So we search both sides:

```text id="z9f4r2"
left = fun(5)
right = fun(1)
```

---

## Left Side — Node 5

We reach:

```text id="w2k8m5"
root = 5
```

Since:

```text id="n5c7x3"
p = 5
```

we have:

```python id="x3m8q7"
if p == root or q == root:
    return root
```

So:

```text id="d6v2k9"
fun(5) → 5
```

Therefore:

```text id="m7x4p1"
left = 5
```

---

## Right Side — Node 1

Now we search:

```text id="r9c2v6"
fun(1)
```

Here:

```text id="h3k8q5"
q = 1
```

So:

```text id="f4m7x2"
q == root
```

and we return:

```text id="v8c1n6"
fun(1) → 1
```

Therefore:

```text id="b2m9q4"
right = 1
```

---

## Back at Node 3

Now we have:

```text id="y7c4m1"
left  = 5
right = 1
```

Both are not `None`.

Therefore:

```python id="n6x2p8"
if left != None and right != None:
    return root
```

returns:

```text id="s5k8v3"
3
```

Therefore:

```text id="d1q7m4"
LCA(5,1) = 3
```

---

# Dry Run for Example 2

Now consider:

```text id="h7m2x9"
p = 5
q = 4
```

Tree:

```text id="6q3v8k"
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

We start at `3`.

The left subtree contains `5`, so eventually:

```text id="z4m8c2"
fun(5) → 5
```

The right subtree does not contain `4`:

```text id="p9x5k3"
fun(1) → None
```

So at node `3`:

```text id="w2v7m6"
left  = 5
right = None
```

Therefore:

```python id="y8k4p1"
if left != None:
    return left
```

returns `5`.

So:

```text id="q6m3v9"
LCA(5,4) = 5
```

This works because node `5` itself is one of the targets and `4` is inside its subtree.

---

# The Key Insight

The most important idea is this:

> **If one target is found in the left subtree and the other target is found in the right subtree, the current node is the LCA.**

Visually:

```text id="g8m4q2"
             X
           /   \
          /     \
         p       q
```

At node `X`:

```text id="a6v1k9"
left  → p
right → q
```

Therefore:

```text id="r3x7m5"
X = LCA(p, q)
```

But if both targets are somewhere on the same side:

```text id="u8c2n4"
             X
            /
           Y
          / \
         p   q
```

then `X` cannot be the lowest common ancestor.

The recursion continues deeper and eventually finds `Y`.

That's why the answer is the **lowest** common ancestor.

---

# Why Does It Work?

The recursive function propagates useful information upward.

For every subtree, it returns:

```text id="q4m8v1"
None
```

if neither target exists there.

Otherwise, it returns a target or an already discovered LCA.

Consider a node:

```text id="c7x2m9"
        root
       /    \
    left    right
```

There are three possibilities.

### Neither side contains a target

```text id="f8v3k5"
left  = None
right = None
```

Return `None`.

### Only one side contains a target

```text id="b5m9q2"
left  = p
right = None
```

Return `p`.

The result moves upward so that an ancestor can later determine whether the other target exists on the opposite side.

### Both sides contain a target

```text id="x2c7m4"
left  = p
right = q
```

Now both targets have been found on opposite sides.

Therefore:

```text id="j8v5n1"
root = LCA(p,q)
```

Because the recursion searches deeper before returning to the parent, the first node where both sides provide a result is the **lowest** common ancestor.

---

# Algorithm

1. Start a recursive function from `root`.
2. If the current node is `None`, return `None`.
3. If the current node is `p` or `q`, return the current node.
4. Recursively search the left subtree.
5. Recursively search the right subtree.
6. If both left and right return a node, the current node is the LCA.
7. If only the left side returns a node, return the left result.
8. If only the right side returns a node, return the right result.
9. Return the result from the root call.

---

# Code

```python id="k4m8v2"
class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        def fun(root):
            if root == None:
                return None

            if p == root or q == root:
                return root

            left = fun(root.left)
            right = fun(root.right)

            if left != None and right != None:
                return root

            if left != None:
                return left

            if right != None:
                return right

            return None

        return fun(root)
```

---

# Complexity

Let `n` be the number of nodes in the binary tree.

## Time Complexity

```text id="v9c4m7"
O(n)
```

In the worst case, the recursion may visit every node in the tree.

Each node is processed at most once.

Therefore:

```text id="a3x8k1"
Time Complexity = O(n)
```

---

## Space Complexity

```text id="m6q2v8"
O(h)
```

where `h` is the height of the tree.

This space comes from the recursive call stack.

For a balanced tree:

```text id="k7m3x9"
h = O(log n)
```

so the auxiliary space is:

```text id="p2v8c4"
O(log n)
```

For a completely skewed tree:

```text id="q5m1x7"
h = O(n)
```

so the worst-case auxiliary space is:

```text id="w8c3m6"
O(n)
```

---

# Key Takeaways

- The **Lowest Common Ancestor** is the deepest node containing both `p` and `q` in its subtree.
- A node can be the LCA of itself and another node.
- The main recursive idea is to search both subtrees.
- If both sides return a node:
  ```python
  if left != None and right != None:
      return root
  ```
  then the current node is the LCA.
- If only one side returns a node, propagate that result upward.
- The comparison of:
  ```text
  left ↔ p/q
  right ↔ p/q
  ```
  allows us to determine where the two targets meet.
- If `root == p` or `root == q`, we return `root` immediately.
- Time complexity is `O(n)`.
- Recursive auxiliary space is `O(h)`, with `O(n)` in the worst case.

---

## Author

**Ramit Sarker**
