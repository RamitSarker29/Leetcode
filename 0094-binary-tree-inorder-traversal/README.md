# 94. Binary Tree Inorder Traversal

## Problem

Given the `root` of a binary tree, return the **inorder traversal** of its nodes' values.

In **inorder traversal**, we visit the nodes in this order:

```text
Left → Root → Right
```

### Example 1

**Input:**
```text
root = [1,null,2,3]
```

**Output:**
```text
[1,3,2]
```

**Explanation:**

![Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

The traversal is:

```text
    1
     \
      2
     /
    3
```

Following **Left → Root → Right**:

```text
1 → 3 → 2
```

---

### Example 2

**Input:**
```text
root = [1,2,3,4,5,null,8,null,null,6,7,9]
```

**Output:**
```text
[4,2,6,5,7,1,3,9,8]
```

**Explanation:**

![Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

Again, we visit every node in:

```text
Left → Root → Right
```

order.

---

### Example 3

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

There are no nodes, so the answer is an empty list.

---

### Example 4

**Input:**
```text
root = [1]
```

**Output:**
```text
[1]
```

A single node is visited directly.

---

# Approach

The natural way to perform inorder traversal is recursively.

The main idea is very simple:

```text
1. Go to the left subtree
2. Add the current node's value
3. Go to the right subtree
```

So for every node:

```text
fun(root)

    ↓

fun(root.left)

    ↓

ans.append(root.val)

    ↓

fun(root.right)
```

We also need a **base case**.

If the current node is `None`, there is nothing to visit, so we simply return.

```python
if root == None:
    return
```

---

# Understanding the Code

First, we create an empty list to store the traversal:

```python
ans = []
```

Then we create a recursive function:

```python
def fun(root):
```

This function receives the current node.

### Step 1: Base Case

```python
if root == None:
    return
```

If there is no node, stop this recursive call.

This is important because eventually we reach the end of a branch.

---

### Step 2: Traverse the Left Subtree

```python
fun(root.left)
```

Before adding the current node, we completely traverse its left subtree.

This follows the **Left** part of:

```text
Left → Root → Right
```

---

### Step 3: Add the Current Node

```python
ans.append(root.val)
```

Once the left subtree is finished, we add the current node's value.

This is the **Root** part.

---

### Step 4: Traverse the Right Subtree

```python
fun(root.right)
```

Finally, we traverse the right subtree.

This is the **Right** part.

So these three lines:

```python
fun(root.left)
ans.append(root.val)
fun(root.right)
```

are the entire idea behind inorder traversal.

---

# Why Does the Order Matter?

Consider this tree:

```text
       1
      / \
     2   3
    / \
   4   5
```

For node `1`:

```text
Left  →  Root  →  Right
```

First, we go to node `2`.

For node `2`:

```text
Left → Root → Right
```

So:

```text
4 → 2 → 5
```

After finishing node `2`, we return to node `1`:

```text
4 → 2 → 5 → 1
```

Then we visit the right subtree:

```text
3
```

Final result:

```text
[4,2,5,1,3]
```

---

# Dry Run

Let's dry run Example 1:

```text
    1
     \
      2
     /
    3
```

We start with:

```python
fun(1)
```

### Call 1

```text
root = 1
```

First:

```python
fun(1.left)
```

`1.left` is `None`.

So:

```python
fun(None)
```

The base case executes:

```python
if root == None:
    return
```

We return to node `1`.

Now:

```python
ans.append(1)
```

So:

```text
ans = [1]
```

Then:

```python
fun(1.right)
```

The right child is `2`.

---

### Call 2

```text
root = 2
```

First:

```python
fun(2.left)
```

Its left child is `3`.

---

### Call 3

```text
root = 3
```

`3.left` is `None`, so return.

Then:

```python
ans.append(3)
```

Now:

```text
ans = [1,3]
```

Then:

```python
fun(3.right)
```

`3.right` is `None`, so return.

We are done with node `3`.

---

We return to node `2`.

Now:

```python
ans.append(2)
```

So:

```text
ans = [1,3,2]
```

Then its right child is `None`, so we return.

Final answer:

```text
[1,3,2]
```

---

# Recursion Flow

For the same tree:

```text
    1
     \
      2
     /
    3
```

The recursive calls look like:

```text
fun(1)
│
├── fun(None)
│
├── append(1)
│
└── fun(2)
    │
    ├── fun(3)
    │   │
    │   ├── fun(None)
    │   ├── append(3)
    │   └── fun(None)
    │
    ├── append(2)
    │
    └── fun(None)
```

Therefore:

```text
1 → 3 → 2
```

---

# Code

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def fun(root):
            if root == None:
                return

            fun(root.left)
            ans.append(root.val)
            fun(root.right)

        fun(root)

        return ans
```

---

# Algorithm

1. Create an empty list `ans`.
2. Define a recursive function `fun(root)`.
3. If `root` is `None`, return.
4. Recursively traverse the left subtree.
5. Add `root.val` to `ans`.
6. Recursively traverse the right subtree.
7. Call `fun(root)` from the main function.
8. Return `ans`.

---

# Why It Works

The recursive function always follows the exact inorder rule:

```text
Left → Root → Right
```

For every node:

- Its entire **left subtree** is processed first.
- Then the **node itself** is added.
- Then its entire **right subtree** is processed.

Because this happens recursively for every node, all nodes are added to `ans` in the correct inorder sequence.

---

# Complexity

Let `n` be the number of nodes in the binary tree.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once.

### Space Complexity

```text
O(h)
```

where `h` is the height of the tree.

This space is used by the recursive call stack.

In the worst case, the tree can be completely skewed:

```text
1
 \
  2
   \
    3
     \
      4
```

Then:

```text
h = n
```

so the worst-case space complexity is:

```text
O(n)
```

---

# Key Takeaways

- **Inorder traversal** means:
  ```text
  Left → Root → Right
  ```
- The base case is:
  ```python
  if root == None:
      return
  ```
- The three important lines are:
  ```python
  fun(root.left)
  ans.append(root.val)
  fun(root.right)
  ```
- Recursion naturally handles the entire tree.
- Every node is visited exactly once.
- The recursive solution uses `O(h)` call-stack space.
- The follow-up asks for an **iterative** solution, which can be implemented using a stack instead of recursion.

---

## Author

**Ramit Sarker**
