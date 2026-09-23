# 181. Employees Earning More Than Their Managers

**Difficulty:** Easy

## Problem

Write a solution to find the employees who earn more than their managers.

Each employee has:
- `id` — Employee's unique ID
- `name` — Employee's name
- `salary` — Employee's salary
- `managerId` — ID of the employee's manager

Return the names of employees whose salary is greater than their manager's salary.

## Approach

This problem can be solved using a **Self JOIN**.

Since the manager is also an employee in the same `Employee` table, we use the table twice:

- `e` → represents the employee
- `m` → represents the manager

We connect them using:

```sql
e.managerId = m.id
```

Then compare their salaries:

```sql
e.salary > m.salary
```

Finally, return the employee's name.

## Solution

```sql
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

Where `n` is the number of employees.

## Key Concept

### Self JOIN

A **Self JOIN** is used when we need to compare rows within the same table.

Here:

```text
Employee e              Employee m
-----------             -----------
Employee                Manager
e.managerId  ────────→  m.id
```

This allows us to compare an employee's salary with their manager's salary.

### Important Takeaway

When a table contains a relationship between its own rows, such as:

```text
employee → manager
employee → supervisor
employee → parent
```

a **Self JOIN** is often the natural solution.

**Author**
**Ramit Sarker**
