# 144. Binary Tree Preorder Traversal

## Problem

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

In **preorder traversal**, we visit the nodes in this order:

```text
Root → Left → Right
```

The important difference from inorder traversal is that we process the **root first**.

---

## Examples

### Example 1

**Input:**
```text
root = [1,null,2,3]
```

**Output:**
```text
[1,2,3]
```

**Explanation:**

![Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

The tree is:

```text
    1
     \
      2
     /
    3
```

Following:

```text
Root → Left → Right
```

we get:

```text
1 → 2 → 3
```

---

### Example 2

**Input:**
```text
root = [1,2,3,4,5,null,8,null,null,6,7,9]
```

**Output:**
```text
[1,2,4,5,6,7,3,8,9]
```

**Explanation:**

![Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

We visit the root first, then recursively visit its left subtree, and finally its right subtree.

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

The tree is empty, so the result is an empty list.

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

There is only one node, so we simply return its value.

---

# Approach

The idea is to use **recursion**.

For preorder traversal, the order is:

```text
Root → Left → Right
```

So for every node, we do exactly three things:

```text
1. Add the current node's value
2. Traverse the left subtree
3. Traverse the right subtree
```

In code:

```python
ans.append(root.val)
fun(root.left)
fun(root.right)
```

This is the entire logic of preorder traversal.

---

# Understanding the Code

First, we create an empty list:

```python
ans = []
```

This list will store the values in preorder.

---

## Step 1: Create the Recursive Function

```python
def fun(root):
```

`fun()` takes the current tree node as input.

We use the same function to process every node in the tree.

---

## Step 2: Base Case

```python
if root == None:
    return
```

If there is no node, there is nothing to process.

So we simply stop that recursive call.

This is what prevents the recursion from continuing forever.

---

## Step 3: Process the Root

```python
ans.append(root.val)
```

This is the most important difference between **preorder** and **inorder**.

In preorder, the root is processed **before** its children.

So:

```text
Root
 ↓
append(root.val)
```

---

## Step 4: Traverse the Left Subtree

```python
fun(root.left)
```

After processing the current node, we recursively visit the entire left subtree.

---

## Step 5: Traverse the Right Subtree

```python
fun(root.right)
```

Once the left subtree is finished, we recursively visit the right subtree.

Therefore:

```python
ans.append(root.val)
fun(root.left)
fun(root.right)
```

represents:

```text
Root → Left → Right
```

---

# Preorder vs Inorder

Since the previous problem was **Binary Tree Inorder Traversal**, the main difference is worth remembering.

### Inorder

```text
Left → Root → Right
```

Code:

```python
fun(root.left)
ans.append(root.val)
fun(root.right)
```

### Preorder

```text
Root → Left → Right
```

Code:

```python
ans.append(root.val)
fun(root.left)
fun(root.right)
```

The only thing that changed is **where we append the root value**.

---

# Dry Run

Let's use Example 1:

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

`root` is not `None`.

First:

```python
ans.append(1)
```

Now:

```text
ans = [1]
```

Then:

```python
fun(1.left)
```

`1.left` is `None`.

So this call returns immediately.

Next:

```python
fun(1.right)
```

The right child is `2`.

---

### Call 2

```text
root = 2
```

First, add the root:

```python
ans.append(2)
```

Now:

```text
ans = [1,2]
```

Then:

```python
fun(2.left)
```

The left child is `3`.

---

### Call 3

```text
root = 3
```

Add `3`:

```python
ans.append(3)
```

Now:

```text
ans = [1,2,3]
```

Then both children of `3` are `None`, so both recursive calls return.

We are finished.

Final result:

```text
[1,2,3]
```

---

# Recursion Flow

The recursive calls can be visualized as:

```text
fun(1)
│
├── append(1)
│
├── fun(None)
│
└── fun(2)
    │
    ├── append(2)
    │
    ├── fun(3)
    │   │
    │   ├── append(3)
    │   ├── fun(None)
    │   └── fun(None)
    │
    └── fun(None)
```

Therefore the values are added in this order:

```text
1 → 2 → 3
```

---

# Another Example

Consider:

```text
       1
      / \
     2   3
    / \
   4   5
```

Preorder means:

```text
Root → Left → Right
```

Start at `1`:

```text
1
```

Then go to the left subtree:

```text
2
```

Then its left subtree:

```text
4
```

Back to `2`, then its right subtree:

```text
5
```

Finally return to `1` and visit the right subtree:

```text
3
```

Final traversal:

```text
[1,2,4,5,3]
```

---

# Why Does It Work?

At every node, the function follows exactly the preorder rule:

```text
Root → Left → Right
```

For a node:

1. `ans.append(root.val)` processes the **root**.
2. `fun(root.left)` processes everything in the **left subtree**.
3. `fun(root.right)` processes everything in the **right subtree**.

Since the same process is recursively applied to every subtree, all nodes are placed into `ans` in the correct preorder sequence.

---

# Algorithm

1. Create an empty list `ans`.
2. Define a recursive function `fun(root)`.
3. If `root` is `None`, return.
4. Add `root.val` to `ans`.
5. Recursively call `fun(root.left)`.
6. Recursively call `fun(root.right)`.
7. Start the recursion with `fun(root)`.
8. Return `ans`.

---

# Code

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def fun(root):
            if root == None:
                return

            ans.append(root.val)
            fun(root.left)
            fun(root.right)

        fun(root)

        return ans
```

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

The recursive calls use the call stack.

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

Then the height is `n`, giving a worst-case space complexity of:

```text
O(n)
```

For a balanced tree, the recursion depth is approximately:

```text
O(log n)
```

---

# Key Takeaways

- **Preorder traversal** means:
  ```text
  Root → Left → Right
  ```
- The root value is added **before** making recursive calls.
- The base case is:
  ```python
  if root == None:
      return
  ```
- The three important lines are:
  ```python
  ans.append(root.val)
  fun(root.left)
  fun(root.right)
  ```
- Every node is visited exactly once.
- Recursion automatically handles all subtrees.
- The follow-up asks for an **iterative** solution, where a stack can replace the recursive call stack.

---

## Author

**Ramit Sarker**
