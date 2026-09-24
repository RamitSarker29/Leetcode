# 183. Customers Who Never Order

## Problem

Write a solution to find all customers who never order anything.

Each customer has:

- `id` — Customer's unique ID
- `name` — Customer's name

The `Orders` table contains the `customerId` of customers who have placed an order.

Return the names of customers who have **no matching order**.

## Approach

This problem can be solved using a **LEFT JOIN** and a **WHERE** condition.

We use `LEFT JOIN` because we need to keep **all customers**, including those who have never placed an order.

We connect the two tables using:

```sql id="g6x6ha"
c.id = o.customerId
```

For customers who have no matching order, the columns from the `Orders` table will contain `NULL`.

So we filter them using:

```sql id="3s2j5c"
WHERE o.customerId IS NULL
```

## Solution

```sql id="e8kq4n"
SELECT name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
```

## Complexity

- **Time:** `O(n + m)`
- **Space:** `O(n + m)`

Where `n` is the number of customers and `m` is the number of orders.

## Key Concept

### LEFT JOIN + IS NULL

A `LEFT JOIN` keeps **all rows from the left table**, even when there is no matching row in the right table.

Here:

```text id="5i7v8u"
Customers c             Orders o
-----------             --------
Joe       ───────────→  Order
Henry     ───────────→  NULL
Sam       ───────────→  Order
Max       ───────────→  NULL
```

Then:

```sql id="q2v8bg"
WHERE o.customerId IS NULL
```

keeps only the customers without an order:

```text id="v4l6p1"
Henry
Max
```

### Important Takeaway

When a problem asks you to find records from one table that have **no matching record** in another table, think:

```sql id="f4cvbi"
FROM A
LEFT JOIN B
ON A.id = B.id
WHERE B.id IS NULL
```

Also remember:

```text id="s2l2kr"
WHERE  → filters rows
HAVING → filters groups
```

Use `WHERE` here because we are filtering the individual rows produced by the `JOIN`, not groups created with `GROUP BY`.

**Author**

**Ramit Sarker**
