# 145. Binary Tree Postorder Traversal

## Problem

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

In **postorder traversal**, we visit the nodes in this order:

```text
Left → Right → Root
```

The important thing to remember is that the **root is processed last**, after both its left and right subtrees have been completely processed.

---

# Examples

## Example 1

**Input:**

```text
root = [1,null,2,3]
```

**Output:**

```text
[3,2,1]
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
Left → Right → Root
```

we get:

```text
3 → 2 → 1
```

---

## Example 2

**Input:**

```text
root = [1,2,3,4,5,null,8,null,null,6,7,9]
```

**Output:**

```text
[4,6,7,5,2,9,8,3,1]
```

**Explanation:**

![Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

We completely process the left subtree first, then the right subtree, and finally the root.

---

## Example 3

**Input:**

```text
root = []
```

**Output:**

```text
[]
```

The tree is empty, so there are no values to traverse.

---

## Example 4

**Input:**

```text
root = [1]
```

**Output:**

```text
[1]
```

There is only one node, so it is the complete traversal.

---

# Approach

We can solve this problem using **recursion**.

The order for postorder traversal is:

```text
Left → Right → Root
```

So for every node, we do exactly three things:

```text
1. Traverse the left subtree
2. Traverse the right subtree
3. Add the current node's value
```

In code:

```python
fun(root.left)
fun(root.right)
ans.append(root.val)
```

Notice that `root.val` is added **after both recursive calls**.

That is what makes this **postorder** traversal.

---

# Understanding the Code

First, we create an empty list:

```python
ans = []
```

This list will contain the nodes in postorder.

---

## Step 1: Create the Recursive Function

```python
def fun(root):
```

`fun()` receives the current node.

We use this same function to recursively process every node in the tree.

---

## Step 2: Base Case

```python
if root == None:
    return
```

If `root` is `None`, there is no node to process.

So we simply return.

This happens whenever we reach the end of a branch.

---

## Step 3: Traverse the Left Subtree

```python
fun(root.left)
```

We first recursively process the entire left subtree.

This represents the **Left** part of:

```text
Left → Right → Root
```

---

## Step 4: Traverse the Right Subtree

```python
fun(root.right)
```

Once the left subtree is completely finished, we recursively process the right subtree.

This represents the **Right** part.

---

## Step 5: Process the Root

```python
ans.append(root.val)
```

Only after both subtrees are finished do we add the current node's value.

This represents the **Root** part.

So these three lines:

```python
fun(root.left)
fun(root.right)
ans.append(root.val)
```

directly represent:

```text
Left → Right → Root
```

---

# Preorder vs Inorder vs Postorder

These three traversals are very easy to confuse, so the main difference is **when we process the root**.

### Preorder

```text
Root → Left → Right
```

```python
ans.append(root.val)
fun(root.left)
fun(root.right)
```

### Inorder

```text
Left → Root → Right
```

```python
fun(root.left)
ans.append(root.val)
fun(root.right)
```

### Postorder

```text
Left → Right → Root
```

```python
fun(root.left)
fun(root.right)
ans.append(root.val)
```

A simple way to remember them:

```text
Preorder:   Root comes FIRST
Inorder:    Root comes in the MIDDLE
Postorder:  Root comes LAST
```

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

---

## Call 1 — Node 1

```text
root = 1
```

We do:

```python
fun(1.left)
```

`1.left` is `None`, so that call returns.

Then:

```python
fun(1.right)
```

The right child is `2`.

---

## Call 2 — Node 2

```text
root = 2
```

First:

```python
fun(2.left)
```

The left child is `3`.

---

## Call 3 — Node 3

```text
root = 3
```

First:

```python
fun(3.left)
```

`3.left` is `None`, so return.

Then:

```python
fun(3.right)
```

`3.right` is also `None`, so return.

Now both children are finished.

Only now do we execute:

```python
ans.append(3)
```

So:

```text
ans = [3]
```

Node `3` is completely finished.

---

## Back to Node 2

We return to node `2`.

Its left subtree is finished.

Its right child is `None`, so:

```python
fun(2.right)
```

returns immediately.

Now both children of `2` are finished.

So we execute:

```python
ans.append(2)
```

Now:

```text
ans = [3,2]
```

---

## Back to Node 1

We return to node `1`.

Both its left and right subtrees are now finished.

So finally:

```python
ans.append(1)
```

Now:

```text
ans = [3,2,1]
```

Final answer:

```text
[3,2,1]
```

---

# Recursion Flow

The recursion can be visualized like this:

```text
fun(1)
│
├── fun(None)
│
├── fun(2)
│   │
│   ├── fun(3)
│   │   │
│   │   ├── fun(None)
│   │   ├── fun(None)
│   │   └── append(3)
│   │
│   ├── fun(None)
│   └── append(2)
│
└── append(1)
```

Therefore, the values are added in this order:

```text
3 → 2 → 1
```

which is exactly:

```text
Left → Right → Root
```

---

# Another Example

Consider this tree:

```text
       1
      / \
     2   3
    / \
   4   5
```

For postorder traversal:

```text
Left → Right → Root
```

Start at `1`.

First, go to the left subtree:

```text
2
```

For node `2`, visit its left child:

```text
4
```

Add `4`.

Then visit its right child:

```text
5
```

Add `5`.

Now both children of `2` are finished, so add:

```text
2
```

So far:

```text
4 → 5 → 2
```

Now return to `1` and visit the right subtree:

```text
3
```

Add `3`.

Finally, both subtrees of `1` are finished, so add:

```text
1
```

Final traversal:

```text
[4,5,2,3,1]
```

---

# Why Does It Work?

The recursive function follows the exact postorder rule:

```text
Left → Right → Root
```

For every node:

1. `fun(root.left)` processes everything on the left.
2. `fun(root.right)` processes everything on the right.
3. `ans.append(root.val)` processes the current node last.

Because this same process is applied recursively to every subtree, every node is added to `ans` in the correct postorder sequence.

---

# Algorithm

1. Create an empty list `ans`.
2. Define a recursive function `fun(root)`.
3. If `root` is `None`, return.
4. Recursively traverse the left subtree.
5. Recursively traverse the right subtree.
6. Add `root.val` to `ans`.
7. Call `fun(root)`.
8. Return `ans`.

---

# Code

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def fun(root):
            if root == None:
                return

            fun(root.left)
            fun(root.right)
            ans.append(root.val)

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

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```

---

# Key Takeaways

- **Postorder traversal** means:
  ```text
  Left → Right → Root
  ```
- The root is processed **after both children**.
- The base case is:
  ```python
  if root == None:
      return
  ```
- The three important lines are:
  ```python
  fun(root.left)
  fun(root.right)
  ans.append(root.val)
  ```
- The position of `ans.append(root.val)` determines the traversal type.
- Every node is visited exactly once.
- Recursion naturally handles the entire tree.
- The follow-up asks for an **iterative** solution, where a stack can be used instead of recursion.

---

## Author

**Ramit Sarker**
