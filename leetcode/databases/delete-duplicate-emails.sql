/*
## Questions

### 196. [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

SQL Schema

Write a SQL query to delete all duplicate email entries in a table named Person,
keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Note:
Your output is the whole Person table after executing your sql. Use delete statement.

Solutions

*/

-- Write your MySQL query statement below

DELETE P1
FROM Person P1, Person P2
WHERE P1.Email = P2.Email and P1.Id > P2.Id;


-- Runtime :  2223 ms, faster than 38.84% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL
