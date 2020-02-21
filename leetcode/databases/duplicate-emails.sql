/*
## Questions

### 182. [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

SQL Schema

Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (Id, Email) values ('1', 'a@b.com')
insert into Person (Id, Email) values ('2', 'c@d.com')
insert into Person (Id, Email) values ('3', 'a@b.com')

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

Solutions

*/

-- Write your MySQL query statement below

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;


-- Runtime : 249 ms, faster than 83.90% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL