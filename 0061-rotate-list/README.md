# 61. Rotate List

## Problem

Given the `head` of a linked list, rotate the list to the **right by `k` places**.

Rotating to the right means that the last `k` nodes move to the beginning of the linked list.

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4,5], k = 2
```

**Output**

```text
[4,5,1,2,3]
```

**Explanation:**

The original list is:

```text
1 → 2 → 3 → 4 → 5 → None
```

Rotate right by `1`:

```text
5 → 1 → 2 → 3 → 4 → None
```

Rotate right by `2`:

```text
4 → 5 → 1 → 2 → 3 → None
```

![Rotate List Example 1](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

---

### Example 2

**Input**

```text
head = [0,1,2], k = 4
```

**Output**

```text
[2,0,1]
```

**Explanation:**

The list has `3` nodes.

Rotating by `4` is equivalent to rotating by:

```text
4 % 3 = 1
```

So we rotate right by `1`:

```text
0 → 1 → 2
```

becomes:

```text
2 → 0 → 1
```

![Rotate List Example 2](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

---

# Approach

The main idea is to find where the list needs to be **cut**.

Consider:

```text
[1,2,3,4,5]
```

and:

```text
k = 2
```

The last `2` nodes should move to the front:

```text
[4,5] [1,2,3]
```

So we need to split the list between:

```text
3 | 4
```

Then connect:

```text
4 → 5 → 1 → 2 → 3
```

---

# Step 1: Find the Length

First, traverse the linked list to find:

* `n` = number of nodes
* `last` = last node

For:

```text
1 → 2 → 3 → 4 → 5 → None
```

we get:

```text
n = 5
last = 5
```

---

# Step 2: Reduce `k`

The value of `k` can be extremely large.

For example:

```text
k = 2,000,000,000
```

If the list contains only `5` nodes, rotating it `5` times brings it back to the original list.

Therefore, we only need:

```python
k = k % n
```

For example:

```text
k = 7
n = 5

7 % 5 = 2
```

So rotating right by `7` is the same as rotating right by `2`.

---

# Why `k % n` Works

For a list of length `5`:

```text
rotate by 5 → original list
rotate by 10 → original list
rotate by 15 → original list
```

Therefore:

```text
k % 5
```

gives the only amount of rotation that actually matters.

---

# Step 3: Find the New Tail

After rotating right by `k`, the new head will be at position:

```text
n - k
```

using 1-based positioning.

For:

```text
n = 5
k = 2
```

we get:

```text
n - k = 3
```

So the node at position `3` becomes the **new tail**.

```text
1 → 2 → 3 | 4 → 5
          ↑
       new tail
```

The node after it becomes the new head:

```text
4 → 5 → 1 → 2 → 3
↑
new head
```

---

# Step 4: Break and Reconnect the List

We find the node at position `n - k`.

Let:

```python
t
```

point to that node.

Then:

```python
new_head = t.next
```

The node after `t` becomes the new head.

Now break the list:

```python
t.next = None
```

Finally, connect the old last node to the old head:

```python
last.next = head
```

This produces the rotated list.

---

# Code

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Find length and last node
        n = 1
        last = head

        while last.next != None:
            n += 1
            last = last.next

        # Reduce unnecessary rotations
        k = k % n

        if k == 0:
            return head

        # Find the new tail
        t = head
        count = 1

        while count < n - k:
            t = t.next
            count += 1

        # Node after new tail becomes new head
        new_head = t.next

        # Break the list
        t.next = None

        # Connect old tail to old head
        last.next = head

        return new_head
```

---

# Dry Run

Consider:

```text
head = [1,2,3,4,5]
k = 2
```

Initial list:

```text
1 → 2 → 3 → 4 → 5 → None
```

### Step 1: Find Length

We traverse the list:

```text
n = 5
last = 5
```

---

### Step 2: Reduce `k`

```text
k = k % n
```

Therefore:

```text
k = 2 % 5
k = 2
```

---

### Step 3: Find New Tail

Calculate:

```text
n - k = 5 - 2 = 3
```

So we need the node at position `3`.

```text
1 → 2 → 3 → 4 → 5
          ↑
          t
```

Therefore:

```text
t = 3
```

---

### Step 4: Find New Head

The node after `t` becomes the new head:

```python
new_head = t.next
```

Therefore:

```text
new_head = 4
```

---

### Step 5: Break the List

Execute:

```python
t.next = None
```

The list becomes:

```text
1 → 2 → 3 → None

4 → 5 → None
```

---

### Step 6: Connect Old Tail to Old Head

The old last node is `5`.

Execute:

```python
last.next = head
```

Now:

```text
4 → 5 → 1 → 2 → 3 → None
```

Finally:

```python
return new_head
```

Result:

```text
[4,5,1,2,3]
```

---

# Understanding `n - k`

This is the most important part of the solution.

Suppose:

```text
n = 5
k = 2
```

The last `2` elements need to move to the front:

```text
[1,2,3] [4,5]
        ↑
      split
```

Therefore, the new tail is the node at:

```text
n - k = 3
```

The node after it becomes the new head.

In general:

```text
New Tail Position = n - k
New Head = New Tail.next
```

---

# Why Do We Use `count < n - k`?

The code uses:

```python
count = 1

while count < n - k:
    t = t.next
    count += 1
```

We start at position `1`.

For:

```text
n = 5
k = 2
```

we need position:

```text
n - k = 3
```

So:

```text
count = 1 → node 1
count = 2 → node 2
count = 3 → node 3
```

The loop stops when `count == 3`.

Therefore `t` points to the new tail.

---

# Another Example

Consider:

```text
head = [0,1,2]
k = 4
```

Length:

```text
n = 3
```

Reduce `k`:

```text
k = 4 % 3
k = 1
```

So we only need one rotation.

Calculate:

```text
n - k = 3 - 1 = 2
```

The node at position `2` is the new tail:

```text
0 → 1 | 2
      ↑
   new tail
```

New head:

```text
2
```

Break:

```text
0 → 1 → None

2 → None
```

Connect old tail to old head:

```text
2 → 0 → 1 → None
```

Result:

```text
[2,0,1]
```

---

# Edge Cases

### Empty List

```text
head = None
```

The function immediately returns:

```text
None
```

because:

```python
if head is None:
    return head
```

---

### Single Node

```text
1 → None
```

Rotating a single-node list changes nothing.

The function returns the same head.

---

### `k = 0`

After:

```python
k = k % n
```

if:

```text
k == 0
```

we simply return the original head.

No changes are required.

---

### `k` Greater Than `n`

For example:

```text
n = 3
k = 4
```

We reduce it:

```text
4 % 3 = 1
```

This prevents unnecessary rotations.

---

# Why Does It Work?

A right rotation by `k` means the final `k` nodes move to the beginning.

Therefore, the list can be divided into:

```text
First n-k nodes | Last k nodes
```

For:

```text
[1,2,3,4,5]
k = 2
```

we get:

```text
[1,2,3] | [4,5]
```

After rotation:

```text
[4,5] | [1,2,3]
```

The algorithm performs exactly this operation by:

1. Finding the new tail (`n-k`).
2. Saving the node after it as `new_head`.
3. Breaking the connection.
4. Connecting the old tail to the old head.
5. Returning `new_head`.

---

# Complexity

Let:

```text
n = number of nodes
```

### Time Complexity

We traverse the linked list to find its length and then traverse again to find the new tail.

Therefore:

```text
O(n)
```

Even though there are two traversals, this is still `O(n)`.

### Space Complexity

Only a few pointers are used:

```text
n
last
t
new_head
```

No additional data structure is required.

Therefore:

```text
O(1)
```

---

# Key Takeaways

* Find the **length** of the linked list first.
* Keep track of the **last node**.
* Use `k % n` to handle very large `k`.
* The **new tail** is at position `n - k`.
* `new_head = new_tail.next`.
* Break the list using:

```python
t.next = None
```

* Connect the old tail to the old head:

```python
last.next = head
```

* Return `new_head`.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
