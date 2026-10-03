# 196. Delete Duplicate Emails

## Problem

Write a solution to **delete all duplicate emails**, keeping only one unique email with the smallest `id`.

For each email that appears multiple times, the row with the smallest `id` should be kept and all other duplicate rows should be deleted.

## Approach

This problem can be solved using a **Self JOIN** with a `DELETE` statement.

Since we need to compare rows within the same `Person` table, we use the table twice:

- `p1` → represents the row that may be deleted
- `p2` → represents another row with the same email

We first find rows with the same email:

```sql
p1.email = p2.email
```

Then we compare their IDs:

```sql
p1.id > p2.id
```

If `p1.id` is greater than `p2.id`, it means `p1` has a larger ID, so it should be deleted.

This keeps the row with the smallest ID.

## Solution

```sql
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
WHERE p1.id > p2.id;
```

## Complexity

- **Time:** `O(n²)`
- **Space:** `O(n)`

Where `n` is the number of rows in the `Person` table.

## Key Concept

### Self JOIN

A **Self JOIN** is used when we need to compare rows within the same table.

Here:

```text
Person p1              Person p2
---------              ---------
Duplicate row          Another row
p1.email ───────────→  p2.email
```

For example:

```text
id   email
1    john@example.com
3    john@example.com
```

The JOIN identifies that both rows have the same email.

Then:

```text
p1.id = 3
p2.id = 1

3 > 1 → TRUE
```

So `p1` (ID 3) is deleted, while ID 1 is kept.

### Important Takeaway

When you need to **delete duplicate rows while keeping the row with the smallest ID**, think:

```text
Self JOIN
    ↓
Find rows with the same value
    ↓
Compare IDs
    ↓
Delete the row with the larger ID
```

The general pattern is:

```sql
DELETE p1
FROM TableName p1
JOIN TableName p2
ON p1.column = p2.column
WHERE p1.id > p2.id;
```

**Author**

**Ramit Sarker**
