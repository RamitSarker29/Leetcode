# 783. Search in a Binary Search Tree

## Problem

You are given the `root` of a **Binary Search Tree (BST)** and an integer `val`.

Your task is to find the node whose value is equal to `val`.

If the node exists:

- Return that node.
- The entire **subtree rooted at that node** is considered the answer.

If the node does not exist, return `null`.

---

# What Is a Binary Search Tree?

A **Binary Search Tree (BST)** follows an important property:

```text
          root
         /    \
   smaller    larger
```

For every node:

```text
Left subtree  → values smaller than the node
Right subtree → values larger than the node
```

For example:

```text id="v5s7c2"
        4
       / \
      2   7
     / \
    1   3
```

At node `4`:

```text
1, 2, 3 < 4
7 > 4
```

This property allows us to eliminate half of the possible search paths at every step.

---

# Examples

## Example 1

![Example 1](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

**Input:**

```text id="g3x8m1"
root = [4,2,7,1,3]
val = 2
```

**Output:**

```text id="m7q2v9"
[2,1,3]
```

The tree is:

```text id="0y4k8s"
        4
       / \
      2   7
     / \
    1   3
```

We are searching for:

```text id="7c1m5x"
val = 2
```

Starting at `4`:

```text id="4r8n2k"
2 < 4
```

Therefore, we move to the **left**.

We reach node `2`:

```text id="5m9q3v"
2 == 2
```

So we return node `2` and its subtree:

```text id="x7k4p2"
    2
   / \
  1   3
```

Therefore:

```text id="s8m1q6"
[2,1,3]
```

---

## Example 2

![Example 2](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

**Input:**

```text id="n2v8c4"
root = [4,2,7,1,3]
val = 5
```

**Output:**

```text id="p6x3m9"
[]
```

The tree is:

```text id="k7q2v5"
        4
       / \
      2   7
     / \
    1   3
```

We start at `4`.

Since:

```text id="m4c8y1"
5 > 4
```

we move to the right:

```text id="z6p3n8"
7
```

Now:

```text id="w9k2v4"
5 < 7
```

so we move left.

But `7` has no left child:

```text id="a8x1m6"
None
```

Therefore, `5` does not exist in the tree.

We return:

```text id="b3q7v9"
[]
```

---

# Approach

Since the given tree is a **Binary Search Tree**, we don't need to search every node.

At each node, compare `val` with `root.val`.

There are three possibilities:

### Case 1: `val > root.val`

The target is larger than the current node.

In a BST, larger values are on the **right**.

So:

```python id="f4m8q2"
return fun(root.right)
```

---

### Case 2: `val < root.val`

The target is smaller than the current node.

In a BST, smaller values are on the **left**.

So:

```python id="y7c3p9"
return fun(root.left)
```

---

### Case 3: `val == root.val`

We found the required node.

So:

```python id="k2v9m5"
return root
```

Because returning `root` returns the entire subtree rooted at that node.

---

# Understanding the Code

Your solution uses recursion:

```python id="p8x4m1"
def fun(root):
```

The function searches for `val` starting from the current node.

---

# Step 1: Check for `None`

```python id="a5q9v2"
if root == None:
    return None
```

If the current node is `None`, there is nowhere else to search.

This means the target does not exist in this path.

So we return:

```text id="j3m7x8"
None
```

---

# Step 2: Store the Children

Your code stores:

```python id="c8v2k5"
left = root.left
right = root.right
```

So we can easily use them in the recursive calls.

```text id="z6q4m1"
left  → left child
right → right child
```

---

# Step 3: Target Is Greater

```python id="r7m3x9"
if val > root.val:
    return fun(right)
```

Suppose:

```text id="v4c8p2"
root.val = 4
val = 7
```

Since:

```text id="h5n1q6"
7 > 4
```

we know the target cannot be in the left subtree.

So we move right:

```text id="m8x3v7"
        4
         \
          7
```

This is one of the main advantages of a BST.

---

# Step 4: Target Is Smaller

```python id="q2k6m8"
if val < root.val:
    return fun(left)
```

Suppose:

```text id="n7c4x1"
root.val = 4
val = 2
```

Since:

```text id="p8m3v6"
2 < 4
```

we know the target must be in the left subtree.

So:

```text id="a4q9k2"
        4
       /
      2
```

and we recursively search the left child.

---

# Step 5: Target Found

If neither of the previous conditions is true, then:

```text id="w6m2p8"
val == root.val
```

So your `else` executes:

```python id="c3x7n1"
else:
    return root
```

We have found the required node.

Returning `root` gives the complete subtree rooted at that node.

For example:

```text id="u9k4m7"
        4
       /
      2
     / \
    1   3
```

If:

```text id="r5x2c8"
val = 2
```

we return the node `2`, which represents:

```text id="v7m1q3"
    2
   / \
  1   3
```

---

# Why Does Returning `root` Return the Subtree?

The problem asks us to return the **subtree rooted at the target node**.

When we return:

```python id="y3c8m5"
return root
```

we return the actual `TreeNode`.

That node still has its:

```text id="m6q2v9"
left child
right child
```

attached.

Therefore, returning the node automatically represents its entire subtree.

For example:

```text id="p8x4k1"
        4
       / \
      2   7
     / \
    1   3
```

If we find node `2`:

```text id="s3m7q9"
return root
```

the returned node is:

```text id="f5v2c8"
    2
   / \
  1   3
```

which is exactly the required subtree.

---

# Dry Run

Let's dry run Example 1:

```text id="q7m3x9"
root = [4,2,7,1,3]
val = 2
```

Tree:

```text id="v5c8n2"
        4
       / \
      2   7
     / \
    1   3
```

We start:

```python id="x4m9p7"
fun(4)
```

---

## Call 1

Current node:

```text id="j8q2v5"
root.val = 4
```

Target:

```text id="c6m1x9"
val = 2
```

Compare:

```text id="n3k7p4"
2 < 4
```

Therefore:

```python id="h5v8m2"
return fun(left)
```

We move to:

```text id="b7x3q1"
2
```

---

## Call 2

Current node:

```text id="w4m9c6"
root.val = 2
```

Target:

```text id="z8p2v5"
val = 2
```

Compare:

```text id="k3x7m1"
2 == 2
```

So neither:

```text id="m5q8v2"
val > root.val
```

nor:

```text id="c1n6x9"
val < root.val
```

is true.

Therefore, we execute:

```python id="f7m2q4"
return root
```

We return node `2`:

```text id="p9x4v7"
    2
   / \
  1   3
```

Final answer:

```text id="a2m8k5"
[2,1,3]
```

---

# Dry Run When the Value Does Not Exist

Now:

```text id="q8m3v1"
root = [4,2,7,1,3]
val = 5
```

Tree:

```text id="c7x2m9"
        4
       / \
      2   7
     / \
    1   3
```

Start:

```text id="v4m8q2"
fun(4)
```

Compare:

```text id="k6x1p9"
5 > 4
```

Move right:

```text id="m3v7c5"
fun(7)
```

Now:

```text id="a9q2k6"
5 < 7
```

Move left:

```text id="x8m4p1"
fun(None)
```

Since:

```python id="z5c7v3"
root == None
```

we return:

```text id="n2q8m6"
None
```

So the final result is:

```text id="r7v3k1"
None
```

which LeetCode represents as:

```text id="h4m9x2"
[]
```

---

# Visualizing the Search

For:

```text id="b8q3m7"
val = 2
```

we search:

```text id="x6v1k9"
        4
       / \
      2   7
     / \
    1   3
```

Start at `4`:

```text id="m3c8q5"
2 < 4
```

Go left:

```text id="p7x2v9"
        4
       /
      2
```

At `2`:

```text id="k4m8c1"
2 == 2
```

Found!

```text id="a9v3q6"
Return subtree rooted at 2
```

---

# Why Does It Work?

The BST property guarantees:

```text id="x7m2c9"
Left subtree  < Root < Right subtree
```

Therefore, at every node we can eliminate one entire subtree.

If:

```text id="0q5v8m"
val > root.val
```

the target cannot be anywhere in the left subtree.

If:

```text id="m4x9c2"
val < root.val
```

the target cannot be anywhere in the right subtree.

If:

```text id="v6k1p8"
val == root.val
```

we have found the required node.

Therefore, the recursive search always moves toward the only subtree that can contain the target.

---

# Why We Don't Search Both Sides

In a normal binary tree, we might have to search both left and right subtrees because there is no ordering guarantee.

For example:

```text id="j7m3x9"
        4
       / \
      8   2
```

We cannot determine where a value belongs.

But in a BST:

```text id="n5c8v2"
        4
       / \
      2   7
```

we know:

```text id="q3m6x1"
Values < 4 → left
Values > 4 → right
```

So if we're searching for `7`, there is no reason to inspect the left subtree.

This makes the search much more efficient.

---

# Algorithm

1. Start at the root.
2. If the current node is `None`, return `None`.
3. If `val > root.val`, recursively search the right subtree.
4. If `val < root.val`, recursively search the left subtree.
5. Otherwise, `val == root.val`, so return the current node.
6. Continue until the value is found or the search reaches `None`.

---

# Code

```python id="r4m8x2"
class Solution:
    def searchBST(
        self,
        root: Optional[TreeNode],
        val: int
    ) -> Optional[TreeNode]:

        def fun(root):
            if root == None:
                return None

            left = root.left
            right = root.right

            if val > root.val:
                return fun(right)

            if val < root.val:
                return fun(left)

            else:
                return root

        return fun(root)
```

---

# Complexity

Let `h` be the height of the BST.

### Time Complexity

```text id="x7m2q9"
O(h)
```

At each step, we move to only **one** subtree.

For a balanced BST:

```text id="c4v8n1"
h = O(log n)
```

Therefore:

```text id="p6m3x8"
Time = O(log n)
```

For a completely skewed BST:

```text id="k9q2v5"
h = O(n)
```

Therefore, the worst-case time is:

```text id="a3x7m1"
O(n)
```

---

### Space Complexity

Because the solution is recursive, the recursion stack uses:

```text id="m8c4q2"
O(h)
```

space.

For a balanced tree:

```text id="j6v1p9"
O(log n)
```

For a skewed tree:

```text id="q5m3x8"
O(n)
```

So the worst-case auxiliary space is:

```text id="z2c7v4"
O(n)
```

---

# Key Takeaways

- A **Binary Search Tree** lets us search efficiently using its ordering property.
- If `val > root.val`, go **right**.
- If `val < root.val`, go **left**.
- If `val == root.val`, return the current node.
- Returning the target `TreeNode` returns the entire subtree rooted at that node.
- We never need to search both subtrees.
- The recursive solution takes `O(h)` time and `O(h)` auxiliary space.
- For a balanced BST, this becomes approximately `O(log n)`.
- For a skewed BST, the worst case is `O(n)`.

---

## Author

**Ramit Sarker**
