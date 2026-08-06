# Meeting Rooms II

## Problem

You are given two arrays:

- `start[]` where `start[i]` is the starting time of the `i`th meeting.
- `end[]` where `end[i]` is the ending time of the `i`th meeting.

Return the **minimum number of meeting rooms** required so that all meetings can be conducted.

> **Note:** If one meeting ends exactly when another starts, they can use the **same room**.

---

## Examples

### Example 1

**Input**

```text
start = [1, 10, 7]
end   = [4, 15, 10]
```

**Output**

```text
1
```

**Explanation**

Meetings do not overlap.

One room is sufficient.

---

### Example 2

**Input**

```text
start = [2, 9, 6]
end   = [4, 12, 10]
```

**Output**

```text
2
```

**Explanation**

At one point, two meetings are running simultaneously.

Therefore, two rooms are required.

---

# Intuition

Instead of comparing meetings directly,

sort all starting times and ending times separately.

Now imagine processing events in chronological order.

- If the next event is a meeting **starting**, one more room becomes occupied.
- If the next event is a meeting **ending**, one room becomes free.

The maximum number of occupied rooms at any moment is the minimum number of meeting rooms required.

---

# Approach

### Step 1

Sort both arrays.

```python
start.sort()
end.sort()
```

---

### Step 2

Initialize two pointers.

```python
i = 0
j = 0
```

- `i` points to the next meeting start.
- `j` points to the next meeting end.

---

### Step 3

Maintain the current number of occupied rooms.

```python
room = 0
```

Also maintain the maximum rooms used.

```python
max_room = 0
```

---

### Step 4

Traverse both arrays.

```python
while i < len(start) and j < len(end):
```

---

### Step 5

If the next meeting starts before the earliest meeting ends,

```python
if start[i] < end[j]:
```

a new room is required.

```python
room += 1
i += 1
```

Update the answer.

```python
max_room = max(max_room, room)
```

---

### Step 6

Otherwise,

the earliest meeting has ended.

A room becomes free.

```python
room -= 1
j += 1
```

If a meeting starts exactly when another ends,

the same room can be reused.

---

### Step 7

Return the maximum number of occupied rooms.

---

# Algorithm

1. Sort the starting times.
2. Sort the ending times.
3. Use two pointers.
4. Increase occupied rooms whenever a meeting starts.
5. Decrease occupied rooms whenever a meeting ends.
6. Track the maximum occupied rooms.
7. Return the maximum.

---

# Code

```python
class Solution:
    def minMeetingRooms(self, start, end):
        room = 0
        max_room = 0

        i = 0
        j = 0

        start.sort()
        end.sort()

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                room += 1
                i += 1
            else:
                room -= 1
                j += 1

            max_room = max(room, max_room)

        return max_room
```

---

# Dry Run

### Example

```text
start = [2,9,6]

end = [4,12,10]
```

After sorting:

```text
start = [2,6,9]

end = [4,10,12]
```

---

Current rooms:

```text
0
```

Meeting starts at `2`.

```text
room = 1
```

Maximum:

```text
1
```

---

Next meeting starts at `6`.

Earliest meeting ends at `4`.

Meeting ends first.

```text
room = 0
```

---

Meeting starts at `6`.

```text
room = 1
```

Maximum:

```text
1
```

---

Meeting starts at `9`.

Earliest ending is `10`.

Meeting starts first.

```text
room = 2
```

Maximum:

```text
2
```

Answer:

```text
2
```

---

# Why Does This Work?

Sorting both arrays allows us to process all meeting starts and ends in chronological order.

Whenever a meeting starts before the earliest current meeting ends,

an additional room is needed.

Whenever a meeting ends,

one room becomes available.

The maximum number of rooms occupied at any instant is exactly the minimum number of meeting rooms required.

---

# Time Complexity

Sorting both arrays:

```text
O(n log n)
```

Two-pointer traversal:

```text
O(n)
```

Overall:

```text
O(n log n)
```

---

# Space Complexity

Ignoring the space used internally by sorting:

```text
O(1)
```

---

# Concepts Used

- Two Pointers
- Sorting
- Greedy
- Arrays

---

# Python Features Used

### Sort

```python
start.sort()
end.sort()
```

---

### Maximum

```python
max(room, max_room)
```

---

# Key Takeaways

- Sort the start and end times separately.
- Treat meeting starts and ends as chronological events.
- Increase the room count when a meeting starts.
- Decrease the room count when a meeting ends.
- The maximum number of occupied rooms is the answer.
- The solution is optimal with **O(n log n)** time complexity.

---

## Author

**Ramit Sarker**
