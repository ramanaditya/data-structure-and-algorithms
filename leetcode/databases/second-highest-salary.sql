/*
## Questions

### 176. [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

SQL Schema

Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary.
If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Solutions

*/

-- Write your MySQL query statement below

SELECT MAX(E.Salary) AS SecondHighestSalary
FROM Employee E
WHERE E.Salary NOT IN (SELECT MAX(Salary)
                             FROM Employee)


-- Runtime : 136 ms, faster than 97.99% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL