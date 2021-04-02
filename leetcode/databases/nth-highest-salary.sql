/*
## Questions

### 177. [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest
salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Solutions

*/

-- Write your MySQL query statement below

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      -- Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M,1
  );
END


-- Runtime : 304 ms, faster than 58.66% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL
