# 739. Daily Temperatures

## Problem

Given an array `temperatures` representing daily temperatures, return an array `answer` where:

```text
answer[i] = number of days you have to wait after day i
            to get a warmer temperature
````

If there is no future day with a warmer temperature, `answer[i]` should remain `0`.

---

## Examples

### Example 1

**Input**

```text
temperatures = [73,74,75,71,69,72,76,73]
```

**Output**

```text
[1,1,4,2,1,1,0,0]
```

For example:

```text
73 → 74
```

The next warmer temperature is the next day, so:

```text
answer[0] = 1
```

For:

```text
75 → 76
```

we have to wait 4 days, so:

```text
answer[2] = 4
```

---

### Example 2

**Input**

```text
temperatures = [30,40,50,60]
```

**Output**

```text
[1,1,1,0]
```

---

### Example 3

**Input**

```text
temperatures = [30,60,90]
```

**Output**

```text
[1,1,0]
```

---

# Approach

We use a **monotonic decreasing stack**.

The stack stores the **indices of days that are still waiting for a warmer temperature**.

For example:

```text
temperatures = [73,74,75,71,69,72,76,73]
```

When we encounter a warmer temperature, we can resolve the days waiting in the stack.

---

## How the Stack Works

Suppose:

```text
73
```

is in the stack.

Then we encounter:

```text
74
```

Since:

```text
74 > 73
```

we know that `74` is the first warmer temperature for `73`.

So we:

1. Pop the index of `73`.
2. Calculate the number of days waited.
3. Store the answer.
4. Continue checking the next index in the stack.

---

## Why Store Indices?

We need to know **how many days apart** the temperatures are.

If:

```text
prev = 3
i = 5
```

then:

```text
i - prev = 5 - 3 = 2
```

So the answer for index `3` is `2`.

Therefore, the stack stores **indices**, not temperatures.

---

# Algorithm

For every index `i`:

### 1. Check the stack

While:

```python
stack
```

is not empty and the current temperature is warmer than the temperature at the stack's top index:

```python
temperatures[i] > temperatures[stack[-1]]
```

we have found the warmer day for the top index.

---

### 2. Remove the waiting index

```python
prev = stack.pop()
```

---

### 3. Calculate the number of days

```python
res[prev] = i - prev
```

---

### 4. Add the current index

After resolving all previous temperatures that are smaller than the current temperature:

```python
stack.append(i)
```

The current day now waits for a future warmer day.

---

# Code

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return res
```

---

# Dry Run

Consider:

```text
temperatures = [73,74,75,71,69,72,76,73]
```

Initially:

```text
stack = []
res = [0,0,0,0,0,0,0,0]
```

### Day 0 → 73

Nothing is in the stack.

```text
stack = [0]
```

---

### Day 1 → 74

`74 > 73`

So index `0` gets its answer:

```text
res[0] = 1 - 0 = 1
```

Then push index `1`:

```text
stack = [1]
```

---

### Day 2 → 75

`75 > 74`

```text
res[1] = 2 - 1 = 1
```

Stack:

```text
[2]
```

---

### Day 3 → 71

`71 < 75`

So we cannot resolve `75`.

```text
stack = [2,3]
```

---

### Day 4 → 69

`69 < 71`

```text
stack = [2,3,4]
```

---

### Day 5 → 72

Now `72 > 69`.

So:

```text
res[4] = 5 - 4 = 1
```

Pop index `4`.

Then:

```text
72 > 71
```

So:

```text
res[3] = 5 - 3 = 2
```

Pop index `3`.

Now:

```text
72 < 75
```

Stop.

Stack:

```text
[2,5]
```

---

### Day 6 → 76

`76 > 72`:

```text
res[5] = 6 - 5 = 1
```

Then:

```text
76 > 75
```

So:

```text
res[2] = 6 - 2 = 4
```

After that, the stack is empty.

Push `6`.

---

### Day 7 → 73

```text
73 < 76
```

So index `6` remains unanswered.

Push `7`.

The final result is:

```text
[1,1,4,2,1,1,0,0]
```

---

# Why Does This Work?

The stack contains indices whose warmer temperature has **not been found yet**.

Whenever the current temperature is greater than the temperature at the top of the stack:

```text
current > waiting temperature
```

we have found the first warmer day for that waiting index.

If the current temperature isn't warmer, we simply leave the previous index in the stack.

Days that never find a warmer temperature remain in the stack, and their answers stay `0`.

---

# Time Complexity

Each index is:

* pushed onto the stack exactly once
* popped from the stack at most once

Therefore:

```text
O(n)
```

overall.

---

# Space Complexity

The stack can contain up to `n` indices.

The result array is required output and is not counted as extra space for this problem.

Therefore:

```text
O(n)
```

extra space.

---

# Key Takeaways

* This is a **Next Greater Element** type of problem.
* Use a **monotonic decreasing stack**.
* Store **indices**, not temperatures.
* The stack contains days still waiting for a warmer temperature.
* When a warmer temperature arrives, pop the waiting indices and calculate:

```text
current_index - previous_index
```

* Each index is pushed and popped at most once.
* Final complexity: **O(n) time, O(n) extra space**.

```
```
**Author**
**Ramit Sarker**
