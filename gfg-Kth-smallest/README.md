# Kth Smallest

## Problem

Given an integer array `arr[]` and an integer `k`, find and return the **kth smallest element** in the array.

The kth smallest element is determined according to the **sorted order** of the array.

---

## Examples

### Example 1

**Input**

```text
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
```

**Output**

```text
5
```

**Explanation**

After sorting:

```text
[2, 3, 4, 5, 6, 10, 10, 33, 48, 53]
             ↑
           4th
```

Therefore, the 4th smallest element is `5`.

---

### Example 2

**Input**

```text
arr = [7, 10, 4, 3, 20, 15]
k = 3
```

**Output**

```text
7
```

**Explanation**

After sorting:

```text
[3, 4, 7, 10, 15, 20]
       ↑
      3rd
```

Therefore, the 3rd smallest element is `7`.

---

# Approach

We use a **heap** to keep track of the `k` smallest elements.

However, instead of using a normal min heap, we use a **max heap**.

Python's `heapq` provides a **min heap**, so we simulate a max heap by inserting the negative of every value:

```python
heapq.heappush(heap, -i)
```

For example, instead of inserting:

```text
10, 5, 8
```

we insert:

```text
-10, -5, -8
```

The smallest negative value corresponds to the **largest original value**.

---

# Why Use a Max Heap?

We want to keep only the **k smallest elements**.

Suppose:

```text
arr = [10, 5, 4, 3, 48, 6]
k = 3
```

The 3 smallest elements are:

```text
3, 4, 5
```

If we maintain a max heap containing these three elements:

```text
[5, 3, 4]
 ↑
largest
```

the largest among the `k` smallest elements is always at the top.

When a new smaller candidate comes in, we can remove the largest element.

---

# Why Negative Values?

Python's `heapq` is a **min heap**.

Normally:

```python
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)
```

gives a heap whose top is:

```text
5
```

But we want the **largest original value** at the top.

So we store:

```text
10 → -10
5  → -5
8  → -8
```

Now the min heap sees:

```text
-10 < -8 < -5
```

Therefore, `-10` comes to the top.

When converted back:

```text
-(-10) = 10
```

So the top represents the **largest original value**.

---

# Algorithm

For every element in the array:

1. Push its negative value into the heap.
2. If the heap contains more than `k` elements:

   * Remove the heap's smallest value.
3. After processing all elements, the heap contains exactly the `k` smallest elements.
4. The largest among these `k` elements is at the top.
5. Negate the top value to get the kth smallest element.

---

# Code

```python
import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        heap = []

        for i in arr:
            heapq.heappush(heap, -i)

            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]
```

---

# Dry Run

Consider:

```text
arr = [10, 5, 4, 3, 48, 6]
k = 3
```

We maintain a max heap using negative values.

Initial:

```text
heap = []
```

---

### Element `10`

Push:

```text
heap = [-10]
```

Size is `1`, which is not greater than `k`.

---

### Element `5`

Push:

```text
heap = [-10, -5]
```

Size is `2`.

---

### Element `4`

Push:

```text
heap = [-10, -5, -4]
```

Size is `3`.

The three smallest elements seen so far are:

```text
4, 5, 10
```

---

### Element `3`

Push:

```text
heap = [-10, -5, -4, -3]
```

Now:

```text
len(heap) > k
```

because:

```text
4 > 3
```

So we pop:

```python
heapq.heappop(heap)
```

The smallest heap value is:

```text
-10
```

which represents the largest original value:

```text
10
```

So `10` is removed.

Now the heap represents:

```text
3, 4, 5
```

---

### Element `48`

Push:

```text
-48
```

The heap temporarily contains four elements.

The largest original value among them is `48`, so it gets removed.

The heap still represents:

```text
3, 4, 5
```

---

### Element `6`

Push:

```text
-6
```

Now there are four elements.

The largest original value is `6`, so it gets removed.

We are left with:

```text
3, 4, 5
```

Therefore:

```text
heap = [-5, -3, -4]
```

The top is:

```text
heap[0] = -5
```

Convert it back:

```text
-heap[0] = 5
```

Final answer:

```text
5
```

---

# Understanding the Important Part

The most important part of the code is:

```python
heapq.heappush(heap, -i)

if len(heap) > k:
    heapq.heappop(heap)
```

Let's understand why this works.

We allow the heap to temporarily contain:

```text
k + 1
```

elements.

Then we remove the largest original element.

Therefore, after every iteration:

```text
heap contains the k smallest elements seen so far
```

This invariant is what makes the algorithm work.

---

# Why Does Popping Remove the Largest Original Element?

Remember that we store negative values.

Suppose the heap represents:

```text
3, 5, 10
```

We actually store:

```text
-3, -5, -10
```

Python's min heap puts:

```text
-10
```

at the top.

But:

```text
-10
```

corresponds to:

```text
10
```

which is the **largest original value**.

Therefore:

```python
heapq.heappop(heap)
```

removes the largest original value.

This is exactly what we want when the heap grows beyond `k`.

---

# Why Does `-heap[0]` Give the Answer?

After processing the entire array, the heap contains exactly the `k` smallest elements.

For example, if:

```text
k = 3
```

and the three smallest elements are:

```text
3, 4, 5
```

the heap contains:

```text
-3, -4, -5
```

The top is:

```text
-5
```

which represents the **largest of the 3 smallest elements**.

That is exactly the:

```text
3rd smallest
```

element.

Therefore:

```python
return -heap[0]
```

returns `5`.

---

# Why Not Use a Min Heap?

A min heap would give us the smallest element, but we need the **kth smallest**.

We could keep all elements and extract `k` times, but that would require more work and potentially more space.

Instead, using a max heap of size `k` allows us to continuously remove elements that are too large.

---

# Comparison

Suppose:

```text
arr = [7, 10, 4, 3, 20, 15]
k = 3
```

Sorted array:

```text
[3, 4, 7, 10, 15, 20]
       ↑
      kth
```

Our heap only needs to maintain:

```text
[3, 4, 7]
```

It does not need to store all six elements after processing.

---

# Complexity

Let:

```text
n = len(arr)
```

The heap contains at most `k` elements.

For each of the `n` elements:

```python
heapq.heappush()
```

takes:

```text
O(log k)
```

and when the heap exceeds `k`, `heappop()` also takes:

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

* Use a **heap** to find the kth smallest element efficiently.
* Python's `heapq` is a **min heap**.
* Store negative values to simulate a **max heap**.
* Keep the heap size at most `k`.
* When the heap becomes larger than `k`, remove the largest original element.
* After processing the array, the heap contains the `k` smallest elements.
* The largest element among those `k` elements is the **kth smallest overall**.
* `heap[0]` stores its negative value, so return:

```python
-heap[0]
```

* **Time Complexity:** `O(n log k)`
* **Space Complexity:** `O(k)`

---

## Author

**Ramit Sarker**
