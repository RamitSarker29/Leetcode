# 235. Lowest Common Ancestor of a Binary Search Tree

<h2><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree">235. Lowest Common Ancestor of a Binary Search Tree</a></h2>

## Problem

Given a **Binary Search Tree (BST)** and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**.

The **Lowest Common Ancestor** is the lowest node in the tree that has both `p` and `q` as descendants.

A node can also be considered a descendant of itself.

---

## Example 1

![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```text
Input:
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8

Output:
6

Explanation:
The LCA of nodes 2 and 8 is 6.
```

---

## Example 2

![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```text
Input:
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 4

Output:
2

Explanation:
2 is the LCA because a node can be a descendant of itself.
```

---

## Example 3

```text
Input:
root = [2,1]
p = 2
q = 1

Output:
2
```

---

# Key Idea

The most important thing here is that the tree is a **Binary Search Tree**.

For every node:

```text
        root
       /    \
   smaller  larger
```

That means:

- Everything in the **left subtree** is smaller than `root.val`.
- Everything in the **right subtree** is larger than `root.val`.

So while searching for the LCA:

### Case 1: Both `p` and `q` are smaller

If:

```python
root.val > p.val and root.val > q.val
```

then both nodes must be in the **left subtree**.

So we do:

```python
return fun(root.left)
```

---

### Case 2: Both `p` and `q` are larger

If:

```python
root.val < p.val and root.val < q.val
```

then both nodes must be in the **right subtree**.

So we do:

```python
return fun(root.right)
```

---

### Case 3: They are on different sides

If neither of the above conditions is true, then `root` is the LCA.

For example:

```text
        6
       / \
      2   8
```

For:

```text
p = 2
q = 8
```

At node `6`:

```text
6 > 2  → True
6 > 8  → False
```

They are not both on the left.

Also:

```text
6 < 2  → False
6 < 8  → True
```

They are not both on the right.

Therefore:

```python
return root
```

So the answer is `6`.

---

# Approach

We use **recursion** and the BST property.

At every node:

1. If `root` is `None`, return `None`.
2. If both `p` and `q` are smaller than `root`, search the left subtree.
3. If both `p` and `q` are larger than `root`, search the right subtree.
4. Otherwise, the current `root` is the LCA.
5. Return that node.

The important part is that we **don't need to search the entire tree**.

The BST property tells us exactly which direction to go.

---

# Code

```python
# Definition for a binary tree node.
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def fun(root):
            if root == None:
                return None

            if root.val > p.val and root.val > q.val:
                return fun(root.left)

            if root.val < p.val and root.val < q.val:
                return fun(root.right)

            return root

        return fun(root)
```

---

# Dry Run

Let's use:

```text
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

And:

```text
p = 2
q = 8
```

### Step 1

Start at:

```text
root = 6
```

Check:

```python
6 > 2 and 6 > 8
```

This is:

```text
True and False
```

So we don't go left.

Now check:

```python
6 < 2 and 6 < 8
```

This is:

```text
False and True
```

So we don't go right.

Therefore:

```python
return root
```

`root` is node `6`.

### Answer

```text
6
```

---

# Another Dry Run

Consider:

```text
        6
       / \
      2   8
         ...
```

with:

```text
p = 2
q = 4
```

### At node 6

Check:

```python
6 > 2 and 6 > 4
```

Both are true.

Therefore:

```python
return fun(root.left)
```

We move to:

```text
        2
       / \
      0   4
```

### At node 2

Check:

```python
2 > 2 and 2 > 4
```

False.

Then:

```python
2 < 2 and 2 < 4
```

False.

So:

```python
return root
```

The current root is `2`.

Therefore:

```text
Answer = 2
```

This also demonstrates why a node can be the LCA of itself and one of its descendants.

---

# Why Does It Work?

The solution works because of the **BST ordering property**.

Suppose the current node is `root`.

### Both nodes are smaller

```text
p < root
q < root
```

Since all smaller values are in the left subtree, both `p` and `q` must be there.

So:

```python
fun(root.left)
```

---

### Both nodes are larger

```text
p > root
q > root
```

Since all larger values are in the right subtree, both nodes must be there.

So:

```python
fun(root.right)
```

---

### Otherwise

If neither condition is true, then one of these situations occurs:

```text
p < root < q
```

or:

```text
q < root < p
```

or:

```text
root == p
```

or:

```text
root == q
```

In all these cases, the current node is the **lowest common ancestor**.

Therefore:

```python
return root
```

---

# Why Do We Return `root`?

This is an important part.

When we reach a node where `p` and `q` are separated by the current node, we have found the LCA.

For example:

```text
        6
       / \
      2   8
```

Here:

```text
p = 2
q = 8
```

Node `6` is the first node where:

```text
p is on the left
q is on the right
```

Therefore, `6` is the lowest node that contains both nodes in its subtree.

So:

```python
return root
```

returns the actual `TreeNode` that represents the answer.

---

# Algorithm

```text
Start at root

        ↓

Is root None?
   ↓ Yes → return None
   ↓ No

Are p and q both smaller than root?
   ↓ Yes → search left subtree
   ↓ No

Are p and q both larger than root?
   ↓ Yes → search right subtree
   ↓ No

Current root is the LCA
   ↓
Return root
```

---

# Complexity Analysis

Let `h` be the height of the BST.

### Time Complexity

```text
O(h)
```

At every step, we move only to one child.

For a balanced BST:

```text
O(log n)
```

For a completely skewed BST:

```text
O(n)
```

---

### Space Complexity

Because the solution uses recursion, the recursion stack can contain at most `h` calls.

```text
O(h)
```

For a balanced tree:

```text
O(log n)
```

For a skewed tree:

```text
O(n)
```

---

# Key Takeaways

- This problem becomes much easier because the tree is a **BST**.
- If both `p` and `q` are smaller than the current node, go **left**.
- If both are larger, go **right**.
- Otherwise, the current node is the **LCA**.
- We don't need to find paths from the root to both nodes.
- A node can be the LCA of itself and another node.
- The solution visits only one path from the root.

---

## Author

**Ramit Sarker**
