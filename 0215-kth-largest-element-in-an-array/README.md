# 215. Kth Largest Element in an Array

## Problem

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

The kth largest element is based on the **sorted order**, not the kth distinct element.

The problem asks us to solve it **without sorting**.

---

## Examples

### Example 1

**Input**

```text
nums = [3,2,1,5,6,4]
k = 2
```

**Output**

```text
5
```

**Explanation**

If we sort the array in descending order:

```text
[6,5,4,3,2,1]
   ↑
  2nd
```

Therefore, the 2nd largest element is `5`.

---

### Example 2

**Input**

```text
nums = [3,2,3,1,2,4,5,5,6]
k = 4
```

**Output**

```text
4
```

**Explanation**

Sorted in descending order:

```text
[6,5,5,4,3,3,2,2,1]
      ↑
     4th
```

Therefore, the 4th largest element is `4`.

---

# Approach

We use a **min heap of size `k`**.

The idea is to maintain the **k largest elements seen so far**.

For example, if:

```text
k = 3
```

we only need to keep the three largest elements.

We don't need to store every element permanently.

---

# Why a Min Heap?

Suppose the three largest elements we have seen are:

```text
[5, 8, 10]
```

Using a min heap:

```text
     5
    / \
   8  10
```

The smallest among these three elements is at the top:

```text
heap[0] = 5
```

If a new element comes in:

```text
12
```

then the four candidates are:

```text
5, 8, 10, 12
```

We only want the three largest:

```text
8, 10, 12
```

So we remove the smallest:

```text
5
```

This is exactly what a min heap allows us to do efficiently.

---

# Core Idea

For every element:

```python
heapq.heappush(heap, i)
```

Add it to the heap.

If the heap becomes larger than `k`:

```python
if len(heap) > k:
    heapq.heappop(heap)
```

The min heap removes the **smallest element**.

Therefore, after every iteration:

```text
heap contains the k largest elements seen so far
```

At the end:

```text
heap[0]
```

is the smallest among those `k` largest elements.

That element is exactly the **kth largest element**.

---

# Algorithm

1. Create an empty min heap.
2. Traverse every element in `nums`.
3. Push the current element into the heap.
4. If the heap size becomes greater than `k`:

   * Remove the smallest element.
5. After processing all elements, return `heap[0]`.

---

# Code

```python
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for i in nums:

            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
```

---

# Dry Run

Consider:

```text
nums = [3,2,1,5,6,4]
k = 2
```

We need the **2 largest elements**.

So we maintain a min heap of size `2`.

---

### Element `3`

Push:

```text
heap = [3]
```

Size:

```text
1 <= 2
```

Nothing is removed.

---

### Element `2`

Push:

```text
heap = [2,3]
```

Size:

```text
2
```

The heap contains the two largest elements seen so far:

```text
2, 3
```

---

### Element `1`

Push:

```text
heap = [1,3,2]
```

Now:

```text
len(heap) = 3 > k
```

So pop the smallest:

```text
1
```

Heap becomes:

```text
[2,3]
```

Now the two largest elements seen so far are:

```text
2,3
```

---

### Element `5`

Push:

```text
heap = [2,3,5]
```

Size is `3`, so remove the smallest:

```text
2
```

Heap becomes:

```text
[3,5]
```

Now the two largest elements seen so far are:

```text
3,5
```

---

### Element `6`

Push:

```text
heap = [3,5,6]
```

Remove the smallest:

```text
3
```

Heap becomes:

```text
[5,6]
```

Now:

```text
5,6
```

are the two largest elements.

---

### Element `4`

Push:

```text
heap = [4,6,5]
```

Remove the smallest:

```text
4
```

Heap becomes:

```text
[5,6]
```

Therefore:

```text
heap[0] = 5
```

Final answer:

```text
5
```

---

# Why Does `heap[0]` Give the Kth Largest?

This is the most important part.

Suppose:

```text
k = 3
```

and after processing the entire array, the heap contains:

```text
[7, 10, 15]
```

These are the **three largest elements** in the entire array.

Among them:

```text
7
```

is the smallest.

Therefore:

```text
15 → largest
10 → 2nd largest
7  → 3rd largest
```

So:

```python
heap[0]
```

gives the **kth largest element**.

---

# Why Do We Remove the Smallest?

Suppose:

```text
k = 3
```

and currently:

```text
heap = [5,8,10]
```

These are our three largest elements so far.

Now we encounter:

```text
12
```

Temporarily:

```text
[5,8,10,12]
```

We only want three elements.

Which one should we remove?

Obviously:

```text
5
```

because it is the smallest.

The min heap gives us `5` immediately:

```python
heapq.heappop(heap)
```

After removal:

```text
[8,10,12]
```

which are the three largest elements.

---

# Why Not Use a Max Heap?

For the **kth largest** problem, a min heap of size `k` is convenient.

We want to remove the **smallest** element whenever we have more than `k` candidates.

A min heap gives us the smallest element at:

```python
heap[0]
```

So:

```text
Kth Largest → Min Heap of size K
```

Similarly:

```text
Kth Smallest → Max Heap of size K
```

This is a very important heap pattern.

---

# Important Heap Pattern

Remember:

### Kth Largest

```text
Min Heap
Size = k
```

Keep the `k` largest elements.

```python
if len(heap) > k:
    heapq.heappop(heap)
```

Answer:

```python
heap[0]
```

---

### Kth Smallest

```text
Max Heap
Size = k
```

Keep the `k` smallest elements.

Since Python only provides a min heap, we use negative values.

Answer:

```python
-heap[0]
```

---

# Dry Run With Duplicates

Consider:

```text
nums = [3,2,3,1,2,4,5,5,6]
k = 4
```

We maintain a min heap of size `4`.

At the end, the four largest elements are:

```text
[4,5,5,6]
```

The smallest among these is:

```text
4
```

Therefore:

```text
heap[0] = 4
```

Final answer:

```text
4
```

Notice that duplicates are counted.

The problem asks for the kth element in sorted order, **not the kth distinct element**.

---

# Why Does the Algorithm Work?

We maintain this invariant:

> After processing every element, the heap contains the `k` largest elements encountered so far.

Whenever the heap has more than `k` elements:

```python
heapq.heappop(heap)
```

removes the smallest one.

Therefore, only the `k` largest elements remain.

After processing the entire array:

```text
heap = k largest elements in the entire array
```

The smallest element among them must be the kth largest element overall.

---

# Complexity

Let:

```text
n = len(nums)
```

The heap contains at most `k` elements.

For every element, we perform:

```python
heappush()
```

which takes:

```text
O(log k)
```

When the heap exceeds `k`, we also perform:

```python
heappop()
```

which takes:

```text
O(log k)
```

Therefore:

### Time Complexity

```text
O(n log k)
```

### Space Complexity

The heap contains at most `k` elements:

```text
O(k)
```

---

# Key Takeaways

* Use a **min heap of size `k`** for the kth largest element.
* Add every element to the heap.
* If the heap grows beyond `k`, remove the smallest element.
* This ensures the heap always contains the **k largest elements seen so far**.
* At the end, `heap[0]` is the smallest among those `k` elements.
* Therefore, `heap[0]` is the **kth largest element**.
* Duplicates are counted.
* No sorting is required.

### Complexity

```text
Time:  O(n log k)
Space: O(k)
```

---

## Author

**Ramit Sarker**
