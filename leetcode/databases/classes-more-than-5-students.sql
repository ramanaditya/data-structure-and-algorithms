/*
## Questions

### 596. [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/)

There is a table World

Create table If Not Exists courses (student varchar(255), class varchar(255))
Truncate table courses
insert into courses (student, class) values ('A', 'Math')
insert into courses (student, class) values ('B', 'English')
insert into courses (student, class) values ('C', 'Math')
insert into courses (student, class) values ('D', 'Biology')
insert into courses (student, class) values ('E', 'Math')
insert into courses (student, class) values ('F', 'Computer')
insert into courses (student, class) values ('G', 'Math')
insert into courses (student, class) values ('H', 'Math')
insert into courses (student, class) values ('I', 'Math')

There is a table courses with columns: student and class
Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+

Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+


Note:
The students should not be counted duplicate in each course.

Solutions

*/

-- Write your MySQL query statement below

SELECT class
FROM (SELECT class, COUNT(DISTINCT(student)) AS number
    FROM courses
    GROUP BY CLASS) AS count_table
WHERE number >= 5;


-- Runtime : 489 ms, faster than 31.03% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL
