# 182. Duplicate Emails

## Problem

Write a solution to report all the duplicate emails in the `Person` table.

An email is considered a duplicate if it appears **more than once** in the table.

Return each duplicate email only once.

## Approach

This problem can be solved using **GROUP BY** and **HAVING**.

We group all rows by `email`:

```sql
GROUP BY email
```

This puts identical emails into the same group.

Then we use:

```sql
HAVING COUNT(email) > 1
```

to keep only the email groups that appear more than once.

## Solution

```sql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

Where `n` is the number of rows in the `Person` table.

## Key Concept

### GROUP BY + HAVING

`GROUP BY` combines rows with the same value into groups.

For example:

```text
a@b.com → 2 occurrences
c@d.com → 1 occurrence
```

Then:

```sql
HAVING COUNT(email) > 1
```

keeps only:

```text
a@b.com → 2 > 1 ✅
```

### Important Takeaway

When a problem asks you to find values that occur **more than once**, think:

```text
GROUP BY → group identical values
COUNT()  → count occurrences
HAVING   → filter the groups
```

Also remember:

- `WHERE` filters **individual rows**
- `HAVING` filters **groups**

**Author**

**Ramit Sarker**
