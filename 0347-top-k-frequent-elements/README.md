# 347. Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

The answer can be returned in **any order**.

The solution should have a time complexity better than:

```text
O(n log n)
```

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,1,2,2,3]
k = 2
```

**Output**

```text
[1,2]
```

**Explanation**

The frequencies are:

```text
1 → 3 times
2 → 2 times
3 → 1 time
```

The two most frequent elements are:

```text
[1,2]
```

---

### Example 2

**Input**

```text
nums = [1]
k = 1
```

**Output**

```text
[1]
```

---

### Example 3

**Input**

```text
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
```

**Output**

```text
[1,2]
```

**Explanation**

Frequencies:

```text
1 → 4
2 → 4
3 → 2
```

Therefore, the two most frequent elements are:

```text
[1,2]
```

---

# Approach

We use **two data structures**:

1. A **Hash Map** to count the frequency of every number.
2. A **Min Heap** of size `k` to keep the `k` most frequent elements.

---

# Step 1: Count Frequencies

First, we create a dictionary:

```python
hash_map = {}
```

For every number in `nums`, increase its frequency.

For example:

```text
nums = [1,1,1,2,2,3]
```

The hash map becomes:

```text
1 → 3
2 → 2
3 → 1
```

The code:

```python
for i in nums:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
```

---

# Step 2: Use a Min Heap

Now we need the `k` elements with the **highest frequencies**.

We use a **min heap**.

Each heap element contains:

```text
[frequency, number]
```

For example:

```text
[3, 1]
[2, 2]
[1, 3]
```

The heap compares the first value:

```text
frequency
```

So the element with the smallest frequency stays at the top.

---

# Why a Min Heap?

Suppose:

```text
k = 2
```

and we have:

```text
1 → 5
2 → 4
3 → 2
```

We only want:

```text
1 → 5
2 → 4
```

So we maintain a heap of size `2`:

```text
[4,2]
[5,1]
```

The smallest frequency is `4`.

If we encounter another element with frequency `6`, temporarily:

```text
[4,2]
[5,1]
[6,3]
```

Now there are `3` elements, but we only need `2`.

We remove the smallest frequency:

```text
[4,2]
```

After removal:

```text
[5,1]
[6,3]
```

Now the heap contains the two most frequent elements.

---

# Heap Structure

The important part of the code is:

```python
heapq.heappush(heap, [hash_map[i], i])

if len(heap) > k:
    heapq.heappop(heap)
```

We push:

```text
[frequency, number]
```

The heap automatically keeps the smallest frequency at the top.

Whenever the heap becomes larger than `k`, we remove that smallest-frequency element.

Therefore:

> The heap always contains the `k` most frequent elements seen so far.

---

# Why Store `[frequency, number]`?

We need the frequency to decide which element should be removed.

For example:

```text
[3, 1]
[2, 2]
[1, 3]
```

The first value represents frequency:

```text
3
2
1
```

The second value represents the actual number:

```text
1
2
3
```

So:

```python
[hash_map[i], i]
```

means:

```text
[frequency, element]
```

---

# Algorithm

1. Create an empty hash map.
2. Count the frequency of every number.
3. Create an empty min heap.
4. For every unique number:

   * Push `[frequency, number]` into the heap.
   * If heap size becomes greater than `k`, remove the smallest element.
5. Extract the numbers from the heap.
6. Return them.

---

# Code

```python
import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        heap = []

        # Count frequencies
        for i in nums:

            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        # Keep k most frequent elements
        for i in hash_map:

            heapq.heappush(heap, [hash_map[i], i])

            if len(heap) > k:
                heapq.heappop(heap)

        # Extract elements
        return [i[1] for i in heap]
```

---

# Dry Run

Consider:

```text
nums = [1,1,1,2,2,3]
k = 2
```

---

## Step 1: Frequency Map

Process the array:

```text
1 → 1
1 → 2
1 → 3
2 → 1
2 → 2
3 → 1
```

Final hash map:

```text
{
    1: 3,
    2: 2,
    3: 1
}
```

---

## Step 2: Build the Heap

### Number `1`

Frequency:

```text
3
```

Push:

```text
heap = [[3,1]]
```

Size is `1`.

---

### Number `2`

Frequency:

```text
2
```

Push:

```text
heap = [[2,2], [3,1]]
```

Size is `2`.

The heap contains:

```text
1 → 3
2 → 2
```

These are currently the two most frequent elements.

---

### Number `3`

Frequency:

```text
1
```

Push:

```text
heap = [[1,3], [3,1], [2,2]]
```

Now:

```text
len(heap) = 3
k = 2
```

So we remove the smallest frequency:

```text
[1,3]
```

The heap becomes:

```text
[[2,2], [3,1]]
```

Therefore, the final elements are:

```text
2
1
```

Return:

```text
[2,1]
```

The order doesn't matter, so this is a valid answer.

---

# Understanding the Heap

The heap is **not necessarily sorted**.

For example:

```text
heap = [[2,2], [3,1]]
```

doesn't mean the final answer must be returned in frequency order.

The problem explicitly allows:

```text
any order
```

Therefore:

```python
return [i[1] for i in heap]
```

is completely valid.

---

# Why Does It Work?

We maintain a heap containing at most `k` elements.

Whenever a new element is added:

```python
heapq.heappush(heap, [frequency, number])
```

if there are more than `k` elements, we remove:

```python
heapq.heappop(heap)
```

Since the heap is a **min heap**, the element with the smallest frequency is removed.

Therefore, the less frequent elements are continuously discarded.

At the end:

```text
heap = k elements with the highest frequencies
```

So extracting the second value from each heap element gives the answer.

---

# Important Pattern

This problem follows an important heap pattern:

```text
Top K Largest / Most Frequent
        ↓
Use Min Heap
        ↓
Keep heap size = K
        ↓
Remove the smallest
```

For this problem:

```text
[frequency, element]
```

The frequency determines which element is removed.

---

# Why Not Sort?

We could sort all unique elements by frequency:

```text
frequency:
5
4
3
2
1
```

But sorting would take:

```text
O(n log n)
```

The problem asks for better than `O(n log n)`.

Using a heap of size `k` gives:

```text
O(n log k)
```

which is better when `k` is much smaller than `n`.

---

# Complexity

Let:

```text
n = len(nums)
```

and let `u` be the number of unique elements.

### Building the Frequency Map

We traverse the array once:

```text
O(n)
```

### Building the Heap

There can be at most `u` unique elements.

Each heap operation costs:

```text
O(log k)
```

Therefore:

```text
O(u log k)
```

Since:

```text
u <= n
```

overall:

```text
O(n log k)
```

### Space Complexity

The hash map stores all unique elements:

```text
O(n)
```

in the worst case.

The heap stores at most `k` elements:

```text
O(k)
```

Therefore overall:

```text
O(n + k)
```

Since `k <= n`, this is commonly written as:

```text
O(n)
```

---

# Key Takeaways

* First use a **Hash Map** to count frequencies.
* Store elements in the heap as:

```python
[frequency, element]
```

* Use a **Min Heap**.
* Keep the heap size at most `k`.
* When the heap becomes larger than `k`, remove the element with the smallest frequency.
* At the end, the heap contains the `k` most frequent elements.
* Extract the element using:

```python
[i[1] for i in heap]
```

* The answer can be returned in **any order**.
* **Time Complexity:** `O(n log k)`
* **Space Complexity:** `O(n)`

---

## Author

**Ramit Sarker**
