# 175. Combine Two Tables

## Problem

Write a solution to report the first name, last name, city, and state of each person in the `Person` table.

If the address of a person is not present in the `Address` table, return `NULL` for the city and state.

## Approach

This problem can be solved using a **LEFT JOIN**.

Since we need information about **every person**, even if they don't have an address, `Person` should be the left table.

We connect the two tables using:

```sql
p.personId = a.personId
```

The `LEFT JOIN` ensures that all people from the `Person` table are included. If a matching address doesn't exist, the columns from `Address` automatically become `NULL`.

## Solution

```sql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
```

## Complexity

- **Time:** `O(n + m)`
- **Space:** `O(n + m)`

Where `n` is the number of rows in `Person` and `m` is the number of rows in `Address`.

## Key Concept

### LEFT JOIN

A **LEFT JOIN** keeps all rows from the left table, even when there is no matching row in the right table.

Here:

```text
Person p                Address a
---------               ---------
Person                  Address
p.personId  ─────────→  a.personId
```

If a matching address exists, its `city` and `state` are returned.

If there is no match:

```text
Person → Address
Allen  → NULL
```

So `city` and `state` become `NULL`.

### Important Takeaway

When a problem asks you to:

```text
keep ALL rows from one table
+
include matching information from another table
+
return NULL when there is no match
```

a **LEFT JOIN** is often the natural solution.

**Author**

**Ramit Sarker**
