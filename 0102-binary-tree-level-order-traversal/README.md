# 102. Binary Tree Level Order Traversal

## Problem

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values.

Level order traversal means:

```text
Left to Right → Level by Level
```

Instead of completely exploring one branch before another, we visit **every node at the current level first**, then move to the next level.

This is also known as **Breadth-First Search (BFS)** on a tree.

---

# Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
[[3],[9,20],[15,7]]
```

**Tree:**

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

The tree looks like:

```text
        3
       / \
      9   20
         /  \
        15   7
```

We visit it level by level:

```text
Level 0:       3
              ↓
Level 1:      9  20
              ↓
Level 2:     15   7
```

Therefore:

```text
[[3],[9,20],[15,7]]
```

---

# Example 2

**Input:**

```text
root = [1]
```

**Output:**

```text
[[1]]
```

There is only one level containing one node.

---

# Example 3

**Input:**

```text
root = []
```

**Output:**

```text
[]
```

The tree is empty, so we return an empty list.

---

# Approach

For level order traversal, we use a **queue**.

A queue follows:

```text
FIFO
First In → First Out
```

This is exactly what we need because we want to process nodes in the same order that we discover them.

Python provides a very efficient queue structure called `deque`:

```python
from collections import deque
```

---

# Main Idea

We start by putting the root into the queue:

```text
Queue:
[3]
```

Then repeatedly:

1. Process all nodes currently in the queue.
2. Store their values in a temporary `level` list.
3. Add their children to the queue.
4. Add the completed `level` to `ans`.
5. Repeat until the queue becomes empty.

The important part is:

```python
for i in range(len(queue)):
```

We use the **current size of the queue** to determine exactly how many nodes belong to the current level.

---

# Why Do We Need `len(queue)`?

This is the key idea in the solution.

Suppose the tree is:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Initially:

```text
Queue = [3]
```

So:

```python
len(queue) = 1
```

We process exactly **1 node**.

While processing `3`, we add its children:

```text
Queue = [9,20]
```

Now the next iteration starts.

At this point:

```python
len(queue) = 2
```

So we process exactly **2 nodes**.

While processing them, their children are added:

```text
Queue = [15,7]
```

Next:

```python
len(queue) = 2
```

So we process exactly those two nodes.

This is how the code separates the tree into levels.

---

# Understanding the Code

## Step 1: Handle an Empty Tree

```python
if root == None:
    return []
```

If there is no root, there is no tree to traverse.

So we immediately return:

```text
[]
```

---

## Step 2: Create the Queue

```python
queue = deque()
```

We create an empty queue.

Then add the root:

```python
queue.append(root)
```

For Example 1:

```text
Queue = [3]
```

---

## Step 3: Create the Answer List

```python
ans = []
```

This will store the values of every level.

Eventually it will look like:

```text
[[3],[9,20],[15,7]]
```

---

# Step 4: Continue While the Queue Is Not Empty

```python
while queue:
```

As long as there are nodes waiting to be processed, we continue.

Once the queue becomes empty, all levels have been processed.

---

# Step 5: Create a List for the Current Level

```python
level = []
```

This temporary list stores only the nodes belonging to the current level.

For example:

```text
level = [9,20]
```

---

# Step 6: Process Exactly One Level

```python
for i in range(len(queue)):
```

This is the most important line.

`len(queue)` tells us how many nodes are currently waiting from the current level.

We process exactly that many nodes.

---

# Step 7: Remove a Node From the Queue

```python
node = queue.popleft()
```

`popleft()` removes the first element of the queue.

For example:

```text
Queue before:
[9,20]

popleft()

Queue after:
[20]
```

The removed node is stored in:

```python
node
```

---

# Step 8: Add the Node's Value

```python
level.append(node.val)
```

We add the current node's value to the current level.

For example:

```text
level = [9]
```

Then after processing `20`:

```text
level = [9,20]
```

---

# Step 9: Add the Left Child

```python
if node.left:
    queue.append(node.left)
```

If the node has a left child, we add it to the queue.

---

# Step 10: Add the Right Child

```python
if node.right:
    queue.append(node.right)
```

If the node has a right child, we add it too.

Notice that we add:

```text
Left child → Right child
```

So nodes at the next level are automatically stored from left to right.

---

# Step 11: Add the Completed Level

After processing all nodes from the current level:

```python
ans.append(level)
```

For example:

```text
level = [9,20]
```

becomes:

```text
ans = [[3],[9,20]]
```

Then we move on to the next level.

---

# Dry Run

Let's perform a complete dry run using:

```text
root = [3,9,20,null,null,15,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

## Initial State

```text
Queue = [3]
ans = []
```

---

## Level 1

Current queue:

```text
[3]
```

Therefore:

```python
len(queue) = 1
```

We process one node.

### Remove 3

```text
node = 3
```

Add its value:

```text
level = [3]
```

Node `3` has:

```text
left  = 9
right = 20
```

Add both:

```text
Queue = [9,20]
```

Now the level is complete.

Add it to `ans`:

```text
ans = [[3]]
```

---

## Level 2

Current queue:

```text
[9,20]
```

Therefore:

```python
len(queue) = 2
```

We process exactly two nodes.

### First node: 9

Remove `9`:

```text
Queue = [20]
```

Add its value:

```text
level = [9]
```

Node `9` has no children.

---

### Second node: 20

Remove `20`:

```text
Queue = []
```

Add its value:

```text
level = [9,20]
```

Node `20` has:

```text
left  = 15
right = 7
```

Add them:

```text
Queue = [15,7]
```

The level is complete.

Add it:

```text
ans = [[3],[9,20]]
```

---

## Level 3

Current queue:

```text
[15,7]
```

Again:

```python
len(queue) = 2
```

Process exactly two nodes.

### Node 15

```text
level = [15]
```

It has no children.

### Node 7

```text
level = [15,7]
```

It has no children.

Queue becomes:

```text
[]
```

Add the level:

```text
ans = [[3],[9,20],[15,7]]
```

---

## Finish

The queue is now empty:

```text
Queue = []
```

Therefore:

```python
while queue:
```

stops.

Return:

```text
[[3],[9,20],[15,7]]
```

---

# Visualizing the Queue

The queue changes like this:

```text
Start

Queue: [3]

        ↓

Process 3

Queue: [9,20]

        ↓

Process 9, 20

Queue: [15,7]

        ↓

Process 15, 7

Queue: []

        ↓

Done
```

And the answer grows like this:

```text
After level 1:
[[3]]

After level 2:
[[3],[9,20]]

After level 3:
[[3],[9,20],[15,7]]
```

---

# Why Does It Work?

The queue guarantees that nodes are processed in **FIFO order**.

When we process a node, we add its:

```text
Left child
Right child
```

to the back of the queue.

Therefore, all nodes from the current level are processed before their children.

The line:

```python
for i in range(len(queue)):
```

is what separates one level from the next.

It captures the number of nodes currently in the queue **before their children are added**.

Therefore, every iteration of the `while` loop processes exactly one level.

---

# Algorithm

1. If `root` is `None`, return `[]`.
2. Create an empty queue using `deque`.
3. Add `root` to the queue.
4. Create an empty answer list `ans`.
5. While the queue is not empty:
   - Create an empty `level` list.
   - Get the current number of nodes in the queue.
   - Process exactly that many nodes.
   - Remove each node using `popleft()`.
   - Add its value to `level`.
   - Add its left child to the queue if it exists.
   - Add its right child to the queue if it exists.
   - Add `level` to `ans`.
6. Return `ans`.

---

# Code

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque()
        ans = []

        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
```

---

# Complexity

Let `n` be the number of nodes in the binary tree.

### Time Complexity

```text
O(n)
```

Every node is:

- added to the queue once
- removed from the queue once
- processed once

Therefore, the total work is `O(n)`.

### Space Complexity

```text
O(n)
```

The queue can contain up to `O(n)` nodes in the worst case.

The `ans` list also stores all `n` node values, so the overall space used is `O(n)`.

---

# Key Takeaways

- **Level order traversal = Breadth-First Search (BFS).**
- Use a **queue** because it follows FIFO order.
- `deque` provides efficient `append()` and `popleft()` operations.
- `len(queue)` tells us how many nodes belong to the current level.
- Process exactly that many nodes before moving to the next level.
- Add children to the queue from **left to right**.
- The traversal order is:
  ```text
  Level 1 → Level 2 → Level 3 → ...
  ```
- Time complexity is `O(n)`.
- Space complexity is `O(n)`.

---

## Author

**Ramit Sarker**
